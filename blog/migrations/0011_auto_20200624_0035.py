# Generated by Django 3.0.7 on 2020-06-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200624_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapros',
            name='status',
            field=models.CharField(default='new', max_length=200, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='JhvXeNQVhBJba55RBAQNLYzes7ldIHHp', max_length=200, verbose_name='JhvXeNQVhBJba55RBAQNLYzes7ldIHHp'),
        ),
    ]