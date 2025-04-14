from django.shortcuts import render, redirect
from .models import Question, QuizResult
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from django.db import models
def home(request):
    return render(request, 'quizapp/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'quizapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('quiz')
    return render(request, 'quizapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, QuizResult
import random

@login_required
def quiz(request):
    if request.method == 'POST':
        question_ids = request.session.get('questions', [])
        questions_dict = {q.id: q for q in Question.objects.filter(id__in=question_ids)}

        score = 0
        for i, qid in enumerate(question_ids):  # maintain original order
            selected = request.POST.get(f'q{i}')
            question = questions_dict.get(qid)
            if question and selected and int(selected) == question.correct_option:
                score += 1

        total_questions = len(question_ids)
        percentage = int((score / total_questions) * 100) if total_questions > 0 else 0

        QuizResult.objects.create(
            user=request.user,
            score=score,
            percentage=percentage
        )

        request.session['last_score'] = score
        request.session['last_percentage'] = percentage

        return redirect('result')

    else:
        questions = random.sample(list(Question.objects.all()), 5)
        request.session['questions'] = [q.id for q in questions]
        return render(request, 'quizapp/quiz.html', {'questions': questions})

@login_required
def result(request):
    score = request.session.get('last_score', 0)
    percentage = request.session.get('last_percentage', 0)
    message = "Please try again!" if score <= 2 else "Good job!" if score == 3 else "Excellent work!" if score == 4 else "You are a genius!"
    allow_retry = score <= 2
    return render(request, 'quizapp/result.html', {
        'score': score,
        'percentage': percentage,
        'message': message,
        'allow_retry': allow_retry,
    })

@login_required
def history(request):
    results = QuizResult.objects.filter(user=request.user)
    avg = results.aggregate(models.Avg('score'))['score__avg'] or 0
    high = results.aggregate(models.Max('score'))['score__max'] or 0
    low = results.aggregate(models.Min('score'))['score__min'] or 0
    return render(request, 'quizapp/history.html', {
        'results': results,
        'avg': avg,
        'high': high,
        'low': low,
    })
