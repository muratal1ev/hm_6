from django import forms
from app.settings.models import Form

class Forms(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'info', 'comment']