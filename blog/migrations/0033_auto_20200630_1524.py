# Generated by Django 3.0.7 on 2020-06-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200630_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='inventNumber',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='Инвентаризационный Номер'),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='d3JmqsFxpOKeqj5g3IbmTtX7aPjaOBOl', max_length=200, verbose_name='d3JmqsFxpOKeqj5g3IbmTtX7aPjaOBOl'),
        ),
    ]
