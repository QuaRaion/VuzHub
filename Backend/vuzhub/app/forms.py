"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class ExamScoresForm(forms.Form):
    russian = forms.IntegerField(min_value=0, max_value = 100, label='Russian')
    physics = forms.IntegerField(label='physics')
    literature = forms.IntegerField(label='literature')
    history = forms.IntegerField(label='history')
    math = forms.IntegerField(label='math')
    chemistry = forms.IntegerField(label='chemistry')
    geography = forms.IntegerField(label='geography')
    socialstudies = forms.IntegerField(label='socialstudies')
    informatics = forms.IntegerField(label='informatics')
    biology = forms.IntegerField(label='biology')
    english = forms.IntegerField(label='english')