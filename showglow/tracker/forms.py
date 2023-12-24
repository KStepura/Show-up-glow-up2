from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Привычка'}),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цель'}),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'}),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Прогресс'}),
        }