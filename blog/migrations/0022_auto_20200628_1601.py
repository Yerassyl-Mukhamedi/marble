# Generated by Django 3.0.7 on 2020-06-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200628_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='new_amount',
        ),
        migrations.RemoveField(
            model_name='history',
            name='old_amount',
        ),
        migrations.AddField(
            model_name='history',
            name='new_over',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='new_rem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='old_over',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='old_rem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history',
            name='used',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='Q9hxLd88SlzhiIRVTsU54gcwIyAJnsds', max_length=200, verbose_name='Q9hxLd88SlzhiIRVTsU54gcwIyAJnsds'),
        ),
    ]