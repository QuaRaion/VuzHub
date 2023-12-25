"""
Definition of views.
"""

from datetime import datetime
from pickle import GET
from django.shortcuts import render
from django.http import HttpRequest
from .forms import ExamScoresForm

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
    return render(request, 'exams.html', )
# def exams(request):
#     """Renders the exams page."""
#     assert isinstance(request, HttpRequest)
#     global score
#     score = 0
#     if request.method == 'POST':
#         form = ExamScoresForm(request.POST)
#         print(form)
#         if form.is_valid():
#             russian = request.POST['russian']
#             physics = form.cleaned_data['physics']
#             literature = form.cleaned_data['literature']
#             history = form.cleaned_data['history']
#             math = form.cleaned_data['math']
#             chemistry = form.cleaned_data['chemistry']
#             geography = form.cleaned_data['geography']
#             socialstudies = form.cleaned_data['socialstudies']
#             informatics = form.cleaned_data['informatics']
#             biology = form.cleaned_data['biology']
#             english = form.cleaned_data['english']
#             score = int(russian) + int(physics) + int(literature) + int(history) + int(math) + int(chemistry) + int(
#                 geography) + int(socialstudies) + int(informatics) + int(biology) + int(english)
#             forms = [russian, physics, literature, history, math, chemistry, geography, socialstudies, informatics,
#                      biology, english]
#             # for exam in forms:
#             #     score+= exam
#             if score > 300 or score < 0:
#                 form = ExamScoresForm()
#                 return render(
#                     request,
#                     'templates/exams.html',
#                     {
#                         'form': form,
#                         'message': 'Your application description page.',
#                         'year': datetime.now().year,
#                     }
#                 )
#             else:
#                 form = ExamScoresForm()
#                 return render(
#                     request,
#                     'templates/universities.html',
#                     {
#                         'form': form,
#                     }
#                 )
#
#
#
#
#     else:
#         form = ExamScoresForm()
#         return render(
#             request,
#             'templates/exams.html',
#             {
#                 'form': form,
#                 'message': 'Your application description page.',
#                 'year': datetime.now().year,
#             }
#         )


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

posts1 = [
    {"number": "09.03.03",
    "name": "Прикладная информатика",
    "probability": 43,
    "chance": "средняя",
    "min_score_1": 237,
    "min_score_2": 243,
    "exams": "РМИ/РМФ",
    }
]
posts2 = [
    {"number": "09.03.04",
    "name": "Программная инженерия",
    "probability": 27,
    "chance": "очень низкая",
    "min_score_1": 235,
    "min_score_2": 262,
    "exams": "РМИ/РМФ",
    }
]
posts3 = [
    {"number": "09.03.02",
    "name": "Инф. системы и технологии",
    "probability": 44,
    "chance": "средняя",
    "min_score_1": 231,
    "min_score_2": 247,
    "exams": "РМИ/РМФ",
    }
]
posts4 = [
    {"number": "09.03.01",
    "name": "Прикладная информатика",
    "probability": 45,
    "chance": "средняя",
    "min_score_1": 231,
    "min_score_2": 244,
    "exams": "РМИ/РМФ",
    }
]
posts5 = [
    {"number": "10.03.01",
    "name": "Информационная безопасность",
    "probability": 44,
    "chance": "средняя",
    "min_score_1": 235,
    "min_score_2": 244,
    "exams": "РМИ/РМФ",
    }
]
posts6 = [
    {"number": "11.03.02",
    "name": "Информационная безопасность",
    "probability": 72,
    "chance": "средняя",
    "min_score_1": 195,
    "min_score_2": 193,
    "exams": "РМИ/РМФ",
    }
]

def specialties(request):
    """Renders the specialties page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'specialties.html',
        {"specs": posts6
         }
    )