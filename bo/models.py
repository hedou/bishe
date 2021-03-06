from django.db import models

# Create your models here.

STATUS_MAP = {
    (0, '正常'),
    (1, '已删除')
}
zhengjian_type_MAP = {
    (0, '第二代居民身份证'),
    (1, '居民户口簿'),
}
xianyijunren_MAP = {
    (0, '否'),
    (1, '是')
}
minzu_MAP = {
    (0, '汉族'),
    (1, '少数民族')
}
sex_MAP = {
    (0, '男'),
    (1, '女')
}
hunyin_MAP = {
    (0, '已婚'),
    (1, '未婚')
}
zhengzhimianmao_MAP = {
    (0, '团员'),
    (1, '群众'),
    (2, '党员'),
    (3, '预备党员'),
    (4, '无党派人士')
}
laiyuan_MAP = {
    (0, '普通全日制应届本科毕业生'),
    (1, '普通全日制往届本科毕业生'),
}
graduation_type_MAP = {
    (0, '普通全日制')
}
graduation_school_MAP = {
    (0, '中北大学'),
    (1, '山西财经大学'),
    (2, '山西大学'),
    (3, '太原理工大学'),
    (4, '太原工业大学'),
    (5, '山西师范大学'),
    (6, '太原大学'),
}
graduation_zhuanye = {
    (0, '应用物理'),
    (1, '计算机科学与技术'),
    (2, '网络工程'),
    (3, '软件工程'),
    (4, '物联网工程'),
    (5, '国际经济与贸易'),


}
baokao_type_MAP = {
    (0, '非定向就业'),
    (1, '定向就业'),
}
departmentsNameMAP = {
    (0, '大数据学院'),
    (1, '体育学院'),
    (2, '软件学院'),
    (3, '经济与管理学院'),
    (4, '理学院'),
    (5, '艺术学院'),
    (6, '仪器与电子学院'),
    (7, '材料科学与工程学院'),
    (8, '机械工程学院'),
    (9, '人文社会科学学院'),
}
professionalNameMAP = {
    (0, '计算机科学与技术'),
    (1, '网络工程'),
    (2, '软件工程'),
    (3, '物联网工程'),
    (4, '数字媒体技术'),
    (5, '数据科学与大数据技术'),
}
researchDirectionMAP = {
    (0, '人工智能'),
    (1, '虚拟仿真与可视化'),
    (2, '大数据与网络安全'),
    (3, '大数据与视觉计算'),
}
examCourseMAP = {
    (0, '政治 英语 专业课 数学')
}
examProvinceMAP = {
    (0, '山西省'),
    (1, '河南省'),
    (2, '陕西省'),
    (3, '山东省'),
    (4, '河北省'),

}
examSchoolMAP = {
    (0, '中北大学'),
    (1, '山西财经大学'),
    (2, '山西大学'),
    (3, '太原理工大学'),
    (4, '太原工业大学'),
    (5, '山西师范大学'),
    (6, '太原大学'),
}
baokao_schoolMAP = {
    (0, '中北大学'),
    (1, '山西财经大学'),
    (2, '山西大学'),
    (3, '太原理工大学'),
    (4, '太原工业大学'),
    (5, '山西师范大学'),
    (6, '太原大学'),
    
}
class Student(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = '学生'

    # wechat_id = models.CharField(max_length=100, verbose_name='微信ID')
    
    name = models.CharField(max_length=100, verbose_name='考生姓名')
    name_pinyin = models.CharField(max_length=100, verbose_name="姓名拼音")
    zhengjian_type = models.IntegerField(default=0, choices=zhengjian_type_MAP, verbose_name='证件类型')
    zhengjian_number = models.CharField(max_length=300, verbose_name='证件号码')
    zhaopian = models.ImageField(max_length=100, verbose_name='个人近期照片')
    xianyijunren = models.IntegerField(default=0, choices=xianyijunren_MAP, verbose_name='现役军人')
    minzu = models.IntegerField(default=0, choices=minzu_MAP, verbose_name='考生民族')
    sex = models.IntegerField(default=0, choices=sex_MAP, verbose_name='考生性别')
    hunyin = models.IntegerField(default=0, choices=hunyin_MAP, verbose_name='婚姻状况')
    zhengzhimianmao = models.IntegerField(default=0, choices=zhengzhimianmao_MAP, verbose_name='政治面貌')
    address = models.CharField(max_length=500, verbose_name='地址')
    postcode = models.CharField(max_length=300, verbose_name='邮政编码')
    fixphone = models.CharField(max_length=300, verbose_name='固定电话')
    telephone = models.CharField(max_length=11, verbose_name='移动电话')


    email = models.CharField(max_length=30, verbose_name='电子信箱', blank=True)
    laiyuan = models.IntegerField(default=0, choices=laiyuan_MAP, verbose_name='考生来源')
    graduation_type = models.IntegerField(default=0, choices=graduation_type_MAP,verbose_name='取得最后学历的学习形式')
    graduation_time = models.DateField(verbose_name='获得最后学历的毕业年月')


    studentId = models.CharField(max_length=300, verbose_name='注册学号')
    graduation_school = models.IntegerField(default=0, choices=graduation_school_MAP, verbose_name='毕业学校')
    graduation_zhuanye = models.IntegerField(default=0, choices=graduation_zhuanye, verbose_name='毕业专业')
    baokao_type = models.IntegerField(default=0, choices=baokao_type_MAP, verbose_name='报考类别')
    nativePlace = models.CharField(max_length=300, verbose_name='考生籍贯')
    registerLocation = models.CharField(max_length=300, verbose_name='户口所在地')
    registerLocationDetail = models.CharField(max_length=300, verbose_name='户口所在地详细地址')
    bornLocation = models.CharField(max_length=300, verbose_name='出生地省市')
    archivesLocation = models.CharField(max_length=300, verbose_name='档案所在地')
    archivesLocationZip = models.CharField(max_length=300, verbose_name='考生档案所在单位邮编')

    baokao_school = models.IntegerField(default=0, choices=baokao_schoolMAP, verbose_name='报考学校名称')
    departmentsName = models.IntegerField(default=0, choices=departmentsNameMAP, verbose_name='报考院系的名称')
    professionalName = models.IntegerField(default=0, choices=professionalNameMAP, verbose_name='报考专业名称')
    researchDirection = models.IntegerField(default=0, choices=researchDirectionMAP, verbose_name='研究方向')
    examCourse = models.IntegerField(default=0, choices=examCourseMAP, verbose_name='考试科目')
    examProvince = models.IntegerField(default=0, choices=examProvinceMAP, verbose_name='报考点所在省份')   
    examSchool = models.IntegerField(default=0, choices=examSchoolMAP, verbose_name='报考点')

    
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    status = models.IntegerField(default=0, choices=STATUS_MAP, verbose_name='状态')
    

    def __str__(self):
        return self.name
    

class Login(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '注册表'
    name = models.CharField(max_length=100, verbose_name='考生姓名')
    zhengjian_number = models.CharField(max_length=300, verbose_name='证件号码')
    telephone = models.CharField(max_length=11, verbose_name='移动电话')
    password = models.CharField(max_length=30, verbose_name='密码')

    # student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name