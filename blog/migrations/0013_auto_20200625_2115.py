# Generated by Django 3.0.7 on 2020-06-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200624_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('t1', 'F217'), ('t2', 'ANB-12'), ('t3', '75zD')], default='t1', max_length=2, verbose_name='Тонер')),
                ('remained_loads', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='laptop',
            name='company',
            field=models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='inventNumber',
            field=models.CharField(default='', max_length=200, verbose_name='Инвентаризационный Номер'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='serialNumber',
            field=models.CharField(default='', max_length=200, verbose_name='Серийный Номер'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='worker',
            name='surname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='problem',
            field=models.TextField(default='', max_length=200, verbose_name='Опишите проблему'),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='SijTChk7Spe5bVRRe4lZQChXcTOH6pey', max_length=200, verbose_name='SijTChk7Spe5bVRRe4lZQChXcTOH6pey'),
        ),
    ]
