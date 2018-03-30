from django.contrib import admin
from django.contrib.auth.models import User as AdminUser, Group
from .models import Student
# Register your models here.

admin.site.site_header = '研究生报名系统'
admin.site.site_title = '研究生报名系统'

admin.site.unregister(AdminUser)
admin.site.unregister(Group)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_pinyin', 'zhengjian_type', 'zhengjian_number', 'xianyijunren', 'minzu', 'sex', 'hunyin', 'zhengzhimianmao', 'address', 'postcode', 'fixphone', 'telephone', 'password', 'email', 'laiyuan', 'graduation_type', 'graduation_time', 'studentId', 'graduation_school', 'graduation_zhuanye', 'baokao_type', 'nativePlace', 'registerLocation', 'registerLocationDetail', 'bornLocation', 'archivesLocation', 'archivesLocationZip', 'departmentsName', 'professionalName', 'researchDirection', 'examCourse', 'examProvince', 'examSchool')

# @admin.register(TarGetSchool)
# class TarGetSchoolAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'departmentsName', 'professionalName', 'researchDirection', 'examCourse', 'examProvince', 'examSchool')
