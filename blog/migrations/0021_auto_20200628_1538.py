# Generated by Django 3.0.7 on 2020-06-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200628_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='new',
            new_name='new_text',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='old',
            new_name='old_text',
        ),
        migrations.AddField(
            model_name='history',
            name='new_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='history',
            name='old_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='CSjTkc0mPXalaKFLQ597jVjEe1VPGbNG', max_length=200, verbose_name='CSjTkc0mPXalaKFLQ597jVjEe1VPGbNG'),
        ),
    ]
