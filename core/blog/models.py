from django.db import models

class User(models.Model):
    name = models.CharField('用户名', max_length=16, null=True)
    pwd = models.CharField('密码', max_length=36, null=True)

    class Meta:
        verbose_name_plural = '用户表'
        verbose_name = '用户'

    def __str__(self):
        return self.name