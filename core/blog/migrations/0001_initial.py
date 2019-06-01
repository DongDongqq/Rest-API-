# Generated by Django 2.0.6 on 2019-06-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, null=True, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=36, null=True, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户表',
            },
        ),
    ]
