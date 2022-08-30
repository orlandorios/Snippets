from dataclasses import fields
from importlib.abc import ExecutionLoader
from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('code', 'description', 'language', 'users')
        
class SnippetDelete(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ()