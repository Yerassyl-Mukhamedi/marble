# Generated by Django 3.0.7 on 2020-06-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200630_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='server',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='12F9B4waZR6QlUjDLB7NpXX73GeidFTD', max_length=200, verbose_name='12F9B4waZR6QlUjDLB7NpXX73GeidFTD'),
        ),
    ]
