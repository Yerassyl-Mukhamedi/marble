from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from .choices import *
from django.utils.crypto import get_random_string


class Laptop(models.Model):
    name = models.CharField('Модель', max_length=200, default='')
    company = models.CharField('Компания',
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField('Инвентаризационный Номер', max_length=200, default='')
    serialNumber = models.CharField('Серийный Номер', max_length=200, default='')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') '


class Printer(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber


class Shredder(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Television(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Condition(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Telephone(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Camera(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Dispenser(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Microwave(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Display(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Computer(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber


class Document(models.Model):
    name = models.CharField(max_length=200, default='name')
    section = models.CharField(
        max_length=3,
        choices=sectionChoice,
        default='s1',
    )
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)
    reading = models.BooleanField('Чтение', default=False)
    adding = models.BooleanField('Добавление', default=False)
    change = models.BooleanField('Изменение', default=False)
    delete = models.BooleanField('Удаление', default=False)
    lead = models.BooleanField('Проведение', default=False)
    unlead = models.BooleanField('Отмена проведения', default=False)
    watch = models.BooleanField('Просмотр', default=False)
    edit = models.BooleanField('Редактирование', default=False)
    lead_redact = models.BooleanField('Изменение проведенных', default=False)
    check_delete = models.BooleanField('Пометка на удаление', default=False)
    uncheck_delete= models.BooleanField('Снятие пометки на удаление', default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' ' + str(self.owner)

class Worker(models.Model):
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    workerID = models.IntegerField(default=1)
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )

    job = models.CharField(
        max_length=2,
        choices=jobChoice,
        default='pd',
    )


    def publish(self):
        self.save()

    def __str__(self):
        return  self.name +' '+ self.surname

class Zapros(models.Model):
    name = models.CharField('Почта',max_length=200, default='')
    problem = models.TextField('Опишите проблему',max_length=200, default='')
    unique_id = get_random_string(length=32)
    verification = models.CharField(unique_id, max_length=200, default = unique_id)
    status = models.CharField('Статус', max_length=200, default = 'new')
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Finished(models.Model):
    name = models.CharField(max_length=200, default='name')
    problem = models.CharField(max_length=200, default='problem')


    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' ' + self.problem