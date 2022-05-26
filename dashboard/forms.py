from dataclasses import fields
from django import forms
import django
from matplotlib.pyplot import title
from matplotlib.widgets import Widget
from . models import *
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm


class NotesForm(forms.ModelForm):
    class  Meta:
        model = Notes
        fields=['title','description']




class HomeworkForm(forms.ModelForm):
    class  Meta:
        model = Homework
        widgets = {
            'due': DateInput(attrs={'type': 'date'})
        }
        fields=['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter your search  ")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']