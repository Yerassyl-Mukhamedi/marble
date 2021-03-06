# Generated by Django 2.0.13 on 2019-07-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.BooleanField(default=False, verbose_name='Чтение')),
                ('adding', models.BooleanField(default=False, verbose_name='Добавление')),
                ('change', models.BooleanField(default=False, verbose_name='Изменение')),
                ('watch', models.BooleanField(default=False, verbose_name='Просмотр')),
                ('delete', models.BooleanField(default=False, verbose_name='Удаление')),
                ('edit', models.BooleanField(default=False, verbose_name='Редактирование')),
            ],
        ),
        migrations.CreateModel(
            name='FileName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('section', models.CharField(choices=[('s1', 'Справочник'), ('s2', 'Документы'), ('s3', 'Константа'), ('s4', 'План обмена'), ('s5', 'Журнал документов'), ('s6', 'Отчет'), ('s7', 'Обработка'), ('s8', 'План счетов'), ('s9', 'Регистр сведений'), ('s10', 'Регистр накоплений'), ('s11', 'Регистр бухгалтерий')], default='s1', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Microwave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shredder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Television',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('inventNumber', models.CharField(default='name', max_length=200)),
                ('serialNumber', models.CharField(default='name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('surname', models.CharField(default='name', max_length=200)),
                ('workerID', models.IntegerField(default=1)),
                ('company', models.CharField(choices=[('pd', 'Planeta Doors'), ('ar', 'ИП Арынов'), ('bt', 'Beltaus Trading'), ('ts', 'ИП Таишев'), ('ki', 'ТОО Kendala Impex'), ('co', 'ЦО'), ('un', 'undefined')], default='pd', max_length=2)),
                ('job', models.CharField(choices=[('j1', 'Оператор'), ('j2', 'Менеджер по продажам'), ('j3', 'Фин отдел'), ('j4', 'Бухгалтер'), ('j5', 'Логисты'), ('j6', 'Продакт Менеджер'), ('j7', 'Оператор 1С'), ('j8', 'Специалист по кадрам'), ('j9', 'Экономист'), ('k1', 'Коммерческий директор'), ('k2', 'Руководитель отдела продаж'), ('k3', 'Оператор по закупкам'), ('k4', 'Региональный менеджер'), ('k5', 'Кассир'), ('k6', 'Руководитель'), ('k7', 'Руководитель департамента отдела поддержки'), ('k8', 'IT')], default='pd', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='television',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='telephone',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='shredder',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='printer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='microwave',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='document',
            name='fileName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.FileName'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='display',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='dispenser',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='condition',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
        migrations.AddField(
            model_name='camera',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Worker'),
        ),
    ]
