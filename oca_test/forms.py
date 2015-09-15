# coding: utf-8
from .models import User, Question, Results
from django import forms
from .choices import *


# class QuestionsForm(forms.Form):
#     question = Question.objects.all
#     answers = forms.ChoiceField(widget=forms.RadioSelect, choices=ANSWERFORM_CHOICES, required=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "sex"]


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["number", "text", "yes", "do_not_know", "no", "character"]


class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ["user", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


class LoginForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
