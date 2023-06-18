from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'time': forms.TextInput(attrs={'class': 'input'}),
        }
        labels = {
            'title': '할 일',
            'time': '시간(ex, 13:10)',
        }