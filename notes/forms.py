from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Notes


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ['owner']
