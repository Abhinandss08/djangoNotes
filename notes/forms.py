from django.forms import ModelForm
from .models import Notes


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
