# Generated by Django 2.1.1 on 2019-06-25 10:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190625_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='商品详情'),
        ),
    ]
