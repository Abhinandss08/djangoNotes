from rest_framework import serializers
from notes.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Notes
        # fields = '__all__'
        exclude = ['upload_image']
