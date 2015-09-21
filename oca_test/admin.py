from django.contrib import admin

# Register your models here.
from .forms import UserForm, QuestionForm, ResultsForm
from .models import User, Question, Results

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "age", "sex"]
    form = UserForm


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["number", "text", "yes", "do_not_know", "no", "character"]
    form = QuestionForm


class ResultsAdmin(admin.ModelAdmin):
    list_display = ["user", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "timestamp"]
    form = ResultsForm


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Results, ResultsAdmin)
