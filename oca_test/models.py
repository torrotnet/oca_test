from django.db import models


class Question(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    yes = models.IntegerField()
    no = models.IntegerField()
    do_not_know = models.IntegerField()

    def __str__(self):
        return self.number


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.CharField(max_length=1, choices=[(u'1', u"14-18"), (u'2', u"18+")])
    sex = models.CharField(max_length=1, choices=[(u'1', u"female"), (u'2', u"male")])

    def __str__(self):
        return "%s" % self.name


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

    def __str__(self):
        return "Results for %s" % self.user.name
