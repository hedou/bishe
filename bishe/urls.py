"""bishe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bo import views as bo_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_in/', bo_views.login_in),
    path('sign_up/', bo_views.sign_up),
    path('baoming/', bo_views.baoming),

    path('updatepwd/', bo_views.updatepwd),
    path('edit/', bo_views.edit),

    path('user/verifycode/', bo_views.verifycode),
    path('gonggao/', bo_views.gonggao),
    path('chengnuoshu/', bo_views.chengnuoshu),
    path('zhuye/', bo_views.zhuye),
    path('list/', bo_views.list),
    path('list_dayin/', bo_views.list_dayin),
    path('zhunkaozheng/', bo_views.zhunkaozheng),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
