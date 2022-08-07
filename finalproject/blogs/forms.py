from django import forms
from .models import video

class Video_form(forms.ModelForm):
    class Meta:
        model=video
        fields=("caption","video")