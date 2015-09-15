# coding=utf-8
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from oca_test.forms import UserForm, LoginForm
from oca_test.models import Results, User, Question
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
    title = "Oxford Capacity analysis - Тест"
    user_form = UserForm(request.POST or None)
    questions = Question.objects.all()

    context = {
        "title": title,
        "user_form": user_form,
        "questions": questions,
    }

    if user_form.is_valid():
        a_score = 0
        b_score = 0
        c_score = 0
        d_score = 0
        e_score = 0
        f_score = 0
        g_score = 0
        h_score = 0
        i_score = 0
        j_score = 0
        do_not_know_answer = 0
        try:
            for q in questions:
                if request.POST[str(q.number)] == 'y':
                    if q.number in [1, 8, 15, 17, 42, 46, 52, 58, 83, 87, 93, 96, 124, 128, 131, 138, 165, 169,
                                    173,176]:
                        a_score += q.yes
                    if q.number in [21, 27, 33, 36, 62, 68, 71, 78, 101, 106, 113, 116, 141, 148, 151, 158, 181, 188,
                                    192,196]:
                        b_score += q.yes
                    if q.number in [2, 6, 11, 18, 43, 47, 53, 56, 81, 86, 91, 97, 122, 130, 132, 136, 164, 166, 171,
                                    177]:
                        c_score += q.yes
                    if q.number in [22, 26, 32, 40, 61, 67, 73, 76, 102, 108, 111, 117, 142, 146, 153, 156, 184, 186,
                                    191, 197]:
                        d_score += q.yes
                    if q.number in [3, 7, 12, 16, 41, 48, 51, 57, 85, 90, 92, 99, 121, 127, 134, 137, 162, 168, 175,
                                    179]:
                        e_score += q.yes
                    if q.number in [23, 29, 31, 38, 65, 66, 72, 79, 103, 107, 114, 120, 145, 147, 154, 159, 185, 187,
                                    195, 199]:
                        f_score += q.yes
                    if q.number in [4, 10, 13, 20, 45, 49, 55, 60, 82, 89, 95, 100, 123, 126, 133, 140, 161, 167, 172,
                                    180]:
                        g_score += q.yes
                    if q.number in [24, 30, 35, 37, 63, 70, 74, 80, 105, 109, 115, 119, 143, 150, 152, 157, 182, 189,
                                    194, 198]:
                        h_score += q.yes
                    if q.number in [5, 9, 14, 19, 44, 50, 54, 59, 84, 88, 94, 98, 125, 129, 135, 139, 163, 170, 174,
                                    178]:
                        i_score += q.yes
                    if q.number in [25, 28, 34, 39, 64, 69, 75, 77, 104, 110, 112, 118, 144, 149, 155, 160, 183, 190,
                                    193, 200]:
                        j_score += q.yes
                if request.POST[str(q.number)] == 'm':
                    if q.number in [1, 8, 15, 17, 42, 46, 52, 58, 83, 87, 93, 96, 124, 128, 131, 138, 165, 169,
                                    173,176]:
                        do_not_know_answer += 1
                        a_score += q.do_not_know
                    if q.number in [21, 27, 33, 36, 62, 68, 71, 78, 101, 106, 113, 116, 141, 148, 151, 158, 181, 188,
                                    192,196]:
                        do_not_know_answer += 1
                        b_score += q.do_not_know
                    if q.number in [2, 6, 11, 18, 43, 47, 53, 56, 81, 86, 91, 97, 122, 130, 132, 136, 164, 166, 171,
                                    177]:
                        c_score += q.do_not_know
                    if q.number in [22, 26, 32, 40, 61, 67, 73, 76, 102, 108, 111, 117, 142, 146, 153, 156, 184, 186,
                                    191, 197]:
                        do_not_know_answer += 1
                        d_score += q.do_not_know
                    if q.number in [3, 7, 12, 16, 41, 48, 51, 57, 85, 90, 92, 99, 121, 127, 134, 137, 162, 168, 175,
                                    179]:
                        e_score += q.do_not_know
                    if q.number in [23, 29, 31, 38, 65, 66, 72, 79, 103, 107, 114, 120, 145, 147, 154, 159, 185, 187,
                                    195, 199]:
                        do_not_know_answer += 1
                        f_score += q.do_not_know
                    if q.number in [4, 10, 13, 20, 45, 49, 55, 60, 82, 89, 95, 100, 123, 126, 133, 140, 161, 167, 172,
                                    180]:
                        do_not_know_answer += 1
                        g_score += q.do_not_know
                    if q.number in [24, 30, 35, 37, 63, 70, 74, 80, 105, 109, 115, 119, 143, 150, 152, 157, 182, 189,
                                    194, 198]:
                        do_not_know_answer += 1
                        h_score += q.do_not_know
                    if q.number in [5, 9, 14, 19, 44, 50, 54, 59, 84, 88, 94, 98, 125, 129, 135, 139, 163, 170, 174,
                                    178]:
                        do_not_know_answer += 1
                        i_score += q.do_not_know
                    if q.number in [25, 28, 34, 39, 64, 69, 75, 77, 104, 110, 112, 118, 144, 149, 155, 160, 183, 190,
                                    193, 200]:
                        do_not_know_answer += 1
                        j_score += q.do_not_know
                if request.POST[str(q.number)] == 'n':
                    if q.number in [1, 8, 15, 17, 42, 46, 52, 58, 83, 87, 93, 96, 124, 128, 131, 138, 165, 169,
                                    173,176]:
                        do_not_know_answer += 1
                        a_score += q.no
                    if q.number in [21, 27, 33, 36, 62, 68, 71, 78, 101, 106, 113, 116, 141, 148, 151, 158, 181, 188,
                                    192,196]:
                        b_score += q.no
                    if q.number in [2, 6, 11, 18, 43, 47, 53, 56, 81, 86, 91, 97, 122, 130, 132, 136, 164, 166, 171,
                                    177]:
                        c_score += q.no
                    if q.number in [22, 26, 32, 40, 61, 67, 73, 76, 102, 108, 111, 117, 142, 146, 153, 156, 184, 186,
                                    191, 197]:
                        d_score += q.no
                    if q.number in [3, 7, 12, 16, 41, 48, 51, 57, 85, 90, 92, 99, 121, 127, 134, 137, 162, 168, 175,
                                    179]:
                        e_score += q.no
                    if q.number in [23, 29, 31, 38, 65, 66, 72, 79, 103, 107, 114, 120, 145, 147, 154, 159, 185, 187,
                                    195, 199]:
                        f_score += q.no
                    if q.number in [4, 10, 13, 20, 45, 49, 55, 60, 82, 89, 95, 100, 123, 126, 133, 140, 161, 167, 172,
                                    180]:
                        g_score += q.no
                    if q.number in [24, 30, 35, 37, 63, 70, 74, 80, 105, 109, 115, 119, 143, 150, 152, 157, 182, 189,
                                    194, 198]:
                        h_score += q.no
                    if q.number in [5, 9, 14, 19, 44, 50, 54, 59, 84, 88, 94, 98, 125, 129, 135, 139, 163, 170, 174,
                                    178]:
                        i_score += q.no
                    if q.number in [25, 28, 34, 39, 64, 69, 75, 77, 104, 110, 112, 118, 144, 149, 155, 160, 183, 190,
                                    193, 200]:
                        j_score += q.no

            B_circle, E_circle, not_confident = False, False, False

            # if request.POST['197'] is 'y':
            #     B_circle = True
            # if request.POST['22'] is 'y':
            #     E_circle = True
            if do_not_know_answer >= 100:
                not_confident = True

            instance = user_form.save(commit=False)
            sex = user_form.cleaned_data.get("sex")
            age = user_form.cleaned_data.get("age")
            email = user_form.cleaned_data.get("email")
            instance.save()

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

            u1 = User.objects.get(email=email)

            r = Results(user=u1, A=a_percent, B=b_percent, C=c_percent, D=d_percent, E=e_percent, F=f_percent,
                        G=g_percent, H=h_percent, I=i_percent, J=j_percent, B_circle=B_circle, E_circle=E_circle,
                        not_confident=not_confident)
            r.save()

            context = {
                "title": "Результаты теста отправлены на обработку - мы с Вами свяжемся.",
                "thank_you": "Спасибо за Ваши ответы, Мы с Вами свяжемся в ближайшее время."
            }
        except:
            checked = []
            for n in range(1, 201):
                try:
                    if str(n) in request.POST:
                        checked.append([n, request.POST[str(n)]])
                except:
                    pass
            context = {
                "title": "Результаты не засчитаны - ответьте на все вопросы",
                "warning": "Вы не ответили на все вопросы. Результыты не засчитаны. Ответьте пожалуйста на все "
                           "вопросы.",
                "user_form": user_form,
                "questions": questions,
                "checked": checked
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
