from django.shortcuts import render
from .models import Login, Student
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
    
    return render(request, 'login/baoming.html')