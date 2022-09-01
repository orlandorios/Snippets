from dataclasses import fields
from importlib.abc import ExecutionLoader
from django import forms
from .models import Language, Snippet

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('code', 'description', 'language')
        
class SnippetDelete(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ()
        
class LanguageForm(forms.ModelForm):
    
        class Meta:
            model = Language
            fields = ('name', 'version')