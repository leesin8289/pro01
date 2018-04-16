from django.db import models


# Create your models here.
class Area(models.Model):
    """地区类"""
    title = models.CharField(max_length=50, verbose_name='区域名称')
    # 外键： 自关联
    parent = models.ForeignKey('self', null=True, blank=True)

    def parent_area(self):
        if self.parent is None:
            return ""
        return self.parent.title

    # 指定列名称
    parent_area.short_description = '上级区域'
    # 指定方法列按id进行排序
    parent_area.admin_order_field = 'id'

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=20)
    # 头像上传到哪里
    avent = models.ImageField(upload_to='app01')
