# coding=utf-8
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from oca_test.forms import UserForm, QuestionsForm, LoginForm
from oca_test.models import Results, User
from oca_test.result_analyse import res_analyse
from oca_test.score_to_percent import *


def home(request):
    title = "Oxford Capacity analysis - Coloris"
    r = Results.objects.first()
    context = {
        "title": title,
        "r": r
    }
    return render(request, "home.html", context)


def test(request):
    questions_form = QuestionsForm(request.POST or None)

    title = "Oxford Capacity analysis - Тест"
    user_form = UserForm(request.POST or None)

    context = {
        "title": title,
        "user_form": user_form,
        "questions_form": questions_form,
    }
    if user_form.is_valid():
        instance = user_form.save(commit=False)
        sex = user_form.cleaned_data.get("sex")
        age = user_form.cleaned_data.get("age")
        instance.save()

        # TODO: check quantity do not know % of all answers. if >50% - person is not confident
        a_score = 100
        b_score = 100
        c_score = 100
        d_score = 100
        e_score = 100
        f_score = 100
        g_score = 100
        h_score = 100
        i_score = 100
        j_score = 100
        a_percent = 200
        b_percent = 200
        c_percent = 200
        d_percent = 200
        e_percent = 200
        f_percent = 200
        g_percent = 200
        h_percent = 200
        i_percent = 200
        j_percent = 200

        if sex is "1" and age is "2":
            a_percent = a_score_to_percent_female_old(a_score)
            b_percent = b_score_to_percent_female_old(b_score)
            c_percent = c_score_to_percent_female_old(c_score)
            d_percent = d_score_to_percent_female_old(d_score)
            e_percent = e_score_to_percent_female_old(e_score)
            f_percent = f_score_to_percent_female_old(f_score)
            g_percent = g_score_to_percent_female_old(g_score)
            h_percent = h_score_to_percent_female_old(h_score)
            i_percent = i_score_to_percent_female_old(i_score)
            j_percent = j_score_to_percent_female_old(j_score)

        if sex is "2" and age is "2":
            a_percent = a_score_to_percent_male_old(a_score)
            b_percent = b_score_to_percent_male_old(b_score)
            c_percent = c_score_to_percent_male_old(c_score)
            d_percent = d_score_to_percent_male_old(d_score)
            e_percent = e_score_to_percent_male_old(e_score)
            f_percent = f_score_to_percent_male_old(f_score)
            g_percent = g_score_to_percent_male_old(g_score)
            h_percent = h_score_to_percent_male_old(h_score)
            i_percent = i_score_to_percent_male_old(i_score)
            j_percent = j_score_to_percent_male_old(j_score)

        u1 = User.objects.first()
        B_circle = True
        E_circle = False
        r = Results(user=u1, A=a_percent, B=b_percent, C=c_percent, D=d_percent, E=e_percent, F=f_percent,
                    G=g_percent, H=h_percent, I=i_percent, J=j_percent, B_circle=B_circle, E_circle=E_circle)
        r.save()

        context = {
            "title": "Успех",
            "r": r
        }
    return render(request, "oca_test.html", context)


def instructions(request):
    return render(request, "instructions.html", {"title": "Инструкции"})


@login_required(login_url='/login/')
def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def log_in(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.data["name"]
        password = form.data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/results/")
            else:
                context = {
                    "warning": "Данной пары логина и пароля не существует, введите корректные данные.",
                    "form": form
                }
        else:
            context = {
                    "warning": "Данной пары логина и пароля не существует, введите корректные данные.",
                    "form": form
            }
    return render(request, "login.html", context)


@login_required(login_url='/login/')
def results(request):
    r = Results.objects.all()

    context = {
        "title": "Результаты",
        "r": r,
    }
    return render(request, "results.html", context)


@login_required(login_url='/login/')
def result(request, id):
    r = Results.objects.get(user_id=id)
    text = res_analyse(r)

    context = {
        "title": "Результат для "+r.user.name+' ('+r.user.email+')',
        "r": r,
        "text": text,
    }
    return render(request, "result.html", context)
