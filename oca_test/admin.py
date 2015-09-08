from django.contrib import admin

# Register your models here.
from .forms import UserForm, QuestionForm, ResultsForm
from .models import User, Question, Results

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "age", "sex"]
    form = UserForm


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["number", "text", "yes", "no", "do_not_know"]
    form = QuestionForm


class ResultsAdmin(admin.ModelAdmin):
    list_display = ["user", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    form = ResultsForm


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Results, ResultsAdmin)
