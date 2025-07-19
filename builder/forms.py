from django import forms
from .models import Resume, ResumeSection

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'template', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'template': forms.Select(attrs={'class': 'form-select'}),
        }

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
