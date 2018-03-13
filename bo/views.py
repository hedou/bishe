from django.shortcuts import render

# Create your views here.

def wechat_login(request):
    ctx = {}

    if request.method == 'GET':
        code = request.GET.get('code')
        ctx['next'] = url_back = request.GET.get('state')

        cache = WechatCache.objects.filter(code=code).first()
        if cache:
            wechat_response = json.loads(cache.api_response)
        else:
            wechat_token_api = 'https://api.weixin.qq.com/sns/oauth2/access_token'
            wechat_token_params = {
                'appid': settings.APP_ID,
                'secret': settings.APP_SECRET,
                'code': code,
                'grant_type': 'authorization_code',
            }
            wechat_response = requests.get(wechat_token_api, params=wechat_token_params).json()
            WechatCache.objects.create(code=code, api_response=json.dumps(wechat_response))
            
        access_token = wechat_response['access_token']
        ctx['wechat_id'] = wechat_id = wechat_response['openid']

        try:
            student = Student.objects.get(wechat_id=wechat_id, status=0)
            request.session['student_id'] = student.id
            return redirect(url_back)

        except Student.DoesNotExist:
            wechat_profile_api = 'https://api.weixin.qq.com/sns/userinfo'
            wechat_profile_params = {
                'access_token': access_token,
                'openid': wechat_id,
                'lang': 'zh_CN',
            }
            wechat_response = requests.get(wechat_profile_api, params=wechat_profile_params).content
            wechat_profile = json.loads(wechat_response.decode('utf-8'))

            ctx['name'] = wechat_profile['nickname']
            ctx['headimg'] = wechat_profile['headimgurl']

            return render(request, 'student/login.html', ctx)

    if request.method == 'POST':
        ctx['phone'] = phone = request.POST.get('phone', '')
        ctx['name'] = name = request.POST.get('name', '')
        ctx['wechat_id'] = wechat_id = request.POST.get('wechat_id', '')
        ctx['headimg'] = headimg = request.POST.get('headimg', '')
        ctx['next'] = url_back = request.POST.get('next', '/student/event/list')

        validation_code = request.POST.get('validation_code', '')

        if Student.objects.filter(wechat_id=wechat_id, status=0).exists():
            ctx['error'] = '微信ID已绑定'
            return render(request, 'student/login.html', ctx)

        if Student.objects.filter(phone=phone, status=0).exists():
            ctx['error'] = '手机已绑定'
            return render(request, 'student/login.html', ctx)

        if validation_code != '123456':
            ctx['error'] = '验证码错误'
            return render(request, 'student/login.html', ctx)

        if not name:
            ctx['error'] = '姓名不能为空'
            return render(request, 'student/login.html', ctx)            

        student = Student.objects.create(wechat_id=wechat_id, phone=phone, name=name)
        request.session['student_id'] = student.id
        return redirect(url_back)