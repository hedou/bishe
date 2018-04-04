from django.shortcuts import render
from .models import Login, Student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def login_in(request):

    return render(request, 'login/login_in.html')

def sign_up(request):
    ctx = {}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        zhengjian_number = request.POST.get('zhengjian_number', '')
        telephone = request.POST.get('telephone', '')
        yzm = request.POST.get('yzm', '')
        password = request.POST.get('password', '')

        Login.objects.create(name=name, zhengjian_number=zhengjian_number, telephone=telephone, password=password)
        ctx['haoma'] = Login.objects.filter()
    return render(request, 'login/sign_up.html')

def login_in(request):
    if request.method == 'POST':
        telephone = request.POST.get('telephone', '')
        password = request.POST.get('password', '')
        flag = Login.objects.filter(telephone=telephone, password=password).first()
        if flag:
            return render(request, 'login/index.html')
        else:
            return render(request, 'login/login_in.html')
    return render(request, 'login/login_in.html')

def baoming(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        name_pinyin = request.POST.get('name', '')
        zhengjian_type = request.POST.get('zhengjian_type', '')
        zhengjian_number = request.POST.get('zhengjian_number', '')
        xianyijunren = request.POST.get('xianyijunren', '')
        minzu = request.POST.get('minzu', '')
        sex = request.POST.get('sex', '')
        hunyin = request.POST.get('hunyin', '')
        zhengzhimianmao = request.POST.get('zhengzhimianmao', '')
        address = request.POST.get('address', '')
        postcode = request.POST.get('postcode', '')
        fixphone = request.POST.get('fixphone', '')
        telephone = request.POST.get('telephone', '')
        email = request.POST.get('email', '')
        laiyuan = request.POST.get('laiyuan', '')
        graduation_type = request.POST.get('graduation_type', '')
        graduation_time = request.POST.get('graduation_time', '')
        studentId = request.POST.get('studentId' , 'studentId')
        graduation_school = request.POST.get('graduation_school', '')
        graduation_zhuanye = request.POST.get('graduation_zhuanye', '')
        baokao_type = request.POST.get('baokao_type', '')
        nativePlace = request.POST.get('nativePlace', '')
        registerLocation = request.POST.get('registerLocation', '')
        registerLocationDetail = request.POST.get('registerLocationDetail', '')
        bornLocation = request.POST.get('bornLocation', '')
        archivesLocation = request.POST.get('archivesLocation', '')
        archivesLocationZip = request.POST.get('archivesLocationZip', '')
        departmentsName = request.POST.get('departmentsName', '')
        professionalName = request.POST.get('professionalName', '')
        researchDirection = request.POST.get('researchDirection', '')
        examCourse = request.POST.get('examCourse', '')
        examProvince = request.POST.get('examProvince', '')
        examSchool = request.POST.get('examSchool', '')

        Student.objects.create(name=name, name_pinyin=name_pinyin, zhengjian_type=zhengjian_type, zhengjian_number=zhengjian_number,
            xianyijunren=xianyijunren, minzu=minzu, sex=sex, hunyin=hunyin, zhengzhimianmao=zhengzhimianmao, address=address,
            postcode=postcode, fixphone=fixphone,
            telephone=telephone, email=email, laiyuan=laiyuan, graduation_type=graduation_type, graduation_time=graduation_time, studentId=studentId,
            graduation_school=graduation_school, graduation_zhuanye=graduation_zhuanye, baokao_type=baokao_type, nativePlace=nativePlace,
            registerLocation=registerLocation, registerLocationDetail=registerLocationDetail, bornLocation=bornLocation,
            archivesLocation=archivesLocation, archivesLocationZip=archivesLocationZip, departmentsName=departmentsName,
            professionalName=professionalName, researchDirection=researchDirection, examCourse=examCourse, examProvince=examProvince,
            examSchool=examSchool)
        return render(request, 'login/update.html')
    return render(request, 'login/baoming.html')


@csrf_exempt
def verifycode(request):

    # ssl._create_default_https_context = ssl._create_unverified_contex

    num = random.randint(1000,9999)
    mobile = request.POST.get('mobile','')

    dic = {
        'num':num
    }

    request.session['vcode'] = num

    apikey = "3134abe67a8f44702a59ed156fc4bd1b"
    text = "亲爱的用户，您的验证码是%d。有效期为24小时，请尽快验证" % num
    print(text)
    sms_host = "sms.yunpian.com"
    port = 443
    sms_send_uri = "/v2/sms/single_send.json"

    params = urllib.parse.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    conn = http.client.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    print(response_str.decode('utf-8'))
    conn.close()

    return HttpResponse(json.dumps(dic), content_type='application/json')

def updatepwd(request):

    return render(request, '')


