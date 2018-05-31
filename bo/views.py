from django.shortcuts import render,redirect
from .models import Login, Student
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import random
import urllib
import http
import json
import datetime
import sys
import requests
import qrcode

def sign_up(request):
    ctx = {}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        zhengjian_number = request.POST.get('zhengjian_number', '')
        telephone = request.POST.get('phone', '')
        # request.session['zhengjian_number'] = zhengjian_number
        # yzm = request.POST.get('yzm', '')

        ctx['validation_code'] = validation_code = request.POST.get('validation_code', '')
        if not validation_code:
            ctx['error'] = '验证码不能为空'
            return render(request, 'login/sign_up.html', ctx)

        vcode = request.session.get('vcode')
        if validation_code != str(vcode):
            ctx['error'] = '您输入的验证码不正确，请重新输入'
            return render(request, 'login/sign_up.html', ctx)


        password = request.POST.get('password', '')

        Login.objects.create(name=name, zhengjian_number=zhengjian_number, telephone=telephone, password=password)
        ctx['haoma'] = Login.objects.filter()

        return render(request, 'login/login_in.html')
    return render(request, 'login/sign_up.html')

def login_in(request):

    if request.method == 'POST':
        telephone = request.POST.get('telephone', '')
        password = request.POST.get('password', '')
        request.session['telephone'] = telephone
        flag = Login.objects.filter(telephone=telephone, password=password).first()
        if flag:

            return render(request, 'login/index.html')
        else:
            return render(request, 'login/login_in.html')
    return render(request, 'login/login_in.html')
@csrf_exempt 
def baoming(request):
    ctx = {}
    huixianphone = request.session['telephone']
    ctx['huixianphone'] = huixianphone
    if request.method == 'POST':
        name = request.POST.get('name','')
        name_pinyin = request.POST.get('name_pinyin', '')
        zhengjian_type = request.POST.get('zhengjian_type', '')
        zhengjian_number = request.POST.get('zhengjian_number', '')
        zhaopian = request.FILES.get('zhaopian', '')
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
        graduation_time = datetime.datetime.strptime(graduation_time,"%Y/%m/%d").strftime("%Y-%m-%d")
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

        Student.objects.create(name=name, name_pinyin=name_pinyin, zhengjian_type=zhengjian_type, zhengjian_number=zhengjian_number, zhaopian=zhaopian,
            xianyijunren=xianyijunren, minzu=minzu, sex=sex, hunyin=hunyin, zhengzhimianmao=zhengzhimianmao, address=address,
            postcode=postcode, fixphone=fixphone,
            telephone=telephone, email=email, laiyuan=laiyuan, graduation_type=graduation_type, graduation_time=graduation_time, studentId=studentId,
            graduation_school=graduation_school, graduation_zhuanye=graduation_zhuanye, baokao_type=baokao_type, nativePlace=nativePlace,
            registerLocation=registerLocation, registerLocationDetail=registerLocationDetail, bornLocation=bornLocation,
            archivesLocation=archivesLocation, archivesLocationZip=archivesLocationZip, departmentsName=departmentsName,
            professionalName=professionalName, researchDirection=researchDirection, examCourse=examCourse, examProvince=examProvince,
            examSchool=examSchool)
        return redirect(list)
    return render(request, 'login/baoming.html', ctx)
@csrf_exempt 
def edit(request):
    ctx = {}
    telephone = request.session['telephone']
    xinxi = Student.objects.filter(telephone=telephone).first()
    ctx['xinxi'] = xinxi
    if request.method == 'POST':
        name = request.POST.get('name','')
        name_pinyin = request.POST.get('name_pinyin', '')
        zhengjian_type = request.POST.get('zhengjian_type', '')
        zhengjian_number = request.POST.get('zhengjian_number', '')
        zhaopian = request.FILES.get('zhaopian', '')
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

        Student.objects.filter(zhengjian_number=zhengjian_number).update(name=name, name_pinyin=name_pinyin, zhengjian_type=zhengjian_type, zhengjian_number=zhengjian_number,zhaopian=zhaopian,
            xianyijunren=xianyijunren, minzu=minzu, sex=sex, hunyin=hunyin, zhengzhimianmao=zhengzhimianmao, address=address,
            postcode=postcode, fixphone=fixphone,
            telephone=telephone, email=email, laiyuan=laiyuan, graduation_type=graduation_type, graduation_time=graduation_time, studentId=studentId,
            graduation_school=graduation_school, graduation_zhuanye=graduation_zhuanye, baokao_type=baokao_type, nativePlace=nativePlace,
            registerLocation=registerLocation, registerLocationDetail=registerLocationDetail, bornLocation=bornLocation,
            archivesLocation=archivesLocation, archivesLocationZip=archivesLocationZip, departmentsName=departmentsName,
            professionalName=professionalName, researchDirection=researchDirection, examCourse=examCourse, examProvince=examProvince,
            examSchool=examSchool)
        return redirect(list)
    return render(request, 'login/edit.html', ctx)


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
    ctx = {}
    telephone = request.session['telephone']
    if request.method == 'POST':
        password = request.POST.get('new_password2', '')
        Login.objects.filter(telephone=telephone).update(password=password)
        chenggong = 1
        ctx['chenggong'] = chenggong

    return render(request, 'login/updatepwd.html', ctx)


def list(request):
    ctx = {}
    telephone = request.session['telephone']
    xinxi_list = Student.objects.filter(telephone=telephone)
    ctx['xinxi_list'] = xinxi_list

    return render(request, 'login/list.html', ctx)


def list_dayin(request):

    ctx = {}
    telephone = request.session['telephone']
    xinxi_list = Student.objects.filter(telephone=telephone)
    ctx['xinxi_list'] = xinxi_list

    return render(request, 'login/list_dayin.html', ctx)



def gonggao(request):
    

    return render(request, 'login/gonggao.html')

def chengnuoshu(request):

    return render(request, 'login/chengnuoshu.html')

def zhuye(request):

    return render(request, 'login/zhuye.html')


def zhunkaozheng(request):

    ctx = {}
    telephone = request.session['telephone']
    xinxi_list = Student.objects.filter(telephone=telephone)
    ctx['xinxi_list'] = xinxi_list

    return render(request, 'login/zhunkaozheng.html', ctx)


@csrf_exempt
def checkPhone(request):

    phone = request.POST.get('phone', '')
    print(phone)
    flag = Login.objects.filter(telephone=phone)
    if flag:
        jj = 0;
    else:
        jj =1;
    return HttpResponse(jj)
        

def erweima(request):
    ctx = {}
    # img=qrcode.make("已付款")  
    # img.save("E:Some.png")  
    return render(request, 'login/erweima.html', ctx)


