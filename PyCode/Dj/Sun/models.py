from django.db import models

# Create your models here.

# 创建模型类
class BookInfo(models.Model):
    """图书模型类"""
    # char是character的缩写
    # 定义了一个书名的属性
    btitle = models.CharField(max_length=20)  # CharField指定为字符类型，max_length指定最大长度
    # 定义一个出版时间属性
    bpublish_date = models.DateField()  # DateField指定为日期(年月日)属性
    # DateTimeField指定的是时间(年月日+时分秒)属性

