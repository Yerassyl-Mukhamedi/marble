# Generated by Django 3.0.7 on 2020-06-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200625_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='toner',
            name='overall',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='toner',
            name='used_loads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='Gl8KSGcewL1zfDFm8Hnr6Kp68umNekPB', max_length=200, verbose_name='Gl8KSGcewL1zfDFm8Hnr6Kp68umNekPB'),
        ),
    ]
