from django import forms
from .models import User, Question, Results

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "age", "sex"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["number", "text", "yes", "no", "do_not_know"]


class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ["user", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
