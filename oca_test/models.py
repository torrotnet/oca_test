# coding: utf-8

from django.db import models
from .choices import *


class User(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Адрес электронной почты', unique=True)
    age = models.CharField('Возраст', max_length=1, choices=USER_AGE_CHOICES)
    sex = models.CharField('Пол', max_length=1, choices=USER_SEX_CHOICES)

    def __str__(self):
        return "%s" % self.name


class Question(models.Model):
    number = models.IntegerField(unique=True)
    text = models.TextField()
    yes = models.IntegerField()
    no = models.IntegerField()
    do_not_know = models.IntegerField()
    character = models.CharField(max_length=1, choices=QUESTION_CHOICES,
                                 default="A")

    def __str__(self):
        return str(self.number)


class Results(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    A = models.IntegerField()
    B = models.IntegerField()
    C = models.IntegerField()
    D = models.IntegerField()
    E = models.IntegerField()
    F = models.IntegerField()
    G = models.IntegerField()
    H = models.IntegerField()
    I = models.IntegerField()
    J = models.IntegerField()
    B_circle = models.BooleanField(default=False)
    E_circle = models.BooleanField(default=False)

    def __str__(self):
        return "Results for %s" % self.user.name
