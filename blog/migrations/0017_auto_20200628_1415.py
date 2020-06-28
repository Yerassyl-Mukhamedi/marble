# Generated by Django 3.0.7 on 2020-06-28 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20200628_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toner',
            name='overall',
            field=models.IntegerField(default=1, verbose_name='Итого'),
        ),
        migrations.AlterField(
            model_name='toner',
            name='remained_loads',
            field=models.IntegerField(default=1, verbose_name='Осталось заправок'),
        ),
        migrations.AlterField(
            model_name='toner',
            name='used_loads',
            field=models.IntegerField(default=0, verbose_name='Использовано сейчас'),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='verification',
            field=models.CharField(default='oOIAtTQBg9eoKIi2aWqOAUy2MqzgNAkq', max_length=200, verbose_name='oOIAtTQBg9eoKIi2aWqOAUy2MqzgNAkq'),
        ),
        migrations.CreateModel(
            name='HistoricalToner',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(choices=[('t1', 'F217'), ('t2', 'ANB-12'), ('t3', '75zD')], default='t1', max_length=2, verbose_name='Тонер')),
                ('remained_loads', models.IntegerField(default=1, verbose_name='Осталось заправок')),
                ('used_loads', models.IntegerField(default=0, verbose_name='Использовано сейчас')),
                ('overall', models.IntegerField(default=1, verbose_name='Итого')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical toner',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
