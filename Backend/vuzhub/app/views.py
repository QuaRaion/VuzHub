"""
Definition of views.
"""

from datetime import datetime
from pickle import GET
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ExamScoresForm
from .models import universities, specialties

russian: int = 0


def chance_of_admission(p1: int, p2: int, s: int):
    p: float = ((s - p1) / (300 - p1) + (s - p2) / (300 - p2) + 0.2) / 2 * 100
    if p > 0 and p < 100:
        return p
    elif p > 100:
        return 100
    elif p < 0:
        return 0



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def exams (request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'exams.html',
        {
            'title': 'Exam Page',
            'year': datetime.now().year,
        })



def universities(request):
    """Renders the universities page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'universities.html',
        {
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def calendar(request):
    """Renders the calendar page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'calendar.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def specialtiespage(request):
    """Отображает страницу специальностей."""
    assert isinstance(request, HttpRequest)

    # Получаем значение параметра запроса 'university'
    university_name = request.GET.get('university', '')

    # Получаем все специальности для выбранного университета из базы данных
    spec = specialties.objects.filter(university=university_name)

    return render(request, 'specialties.html', {'specialties_list': spec, 'probability': 50})


