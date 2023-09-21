from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes.models import Notes
from .serializers import NotesSerializer
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def notesList(request):
    if request.method == 'GET':
        notes = Notes.objects.all()
        # owner_name = request.owner.Notes
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        owner_id = data['owner']
        owner = User.objects.get(id=owner_id)
        note = Notes.objects.create(
            owner=owner,
            title=request.data['title'],
            content=request.data['content']
        )
        note.save()
        serializer = NotesSerializer(note, many=False)
        return Response("Note is created!")


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def singleNote(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'GET':
        serializer = NotesSerializer(note, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        note.title = request.data['title']
        note.content = request.data['content']
        note.save()
        serializer = NotesSerializer(note, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        note.delete()
        return Response('Note was deleted!')
