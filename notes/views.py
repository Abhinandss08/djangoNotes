from django.shortcuts import render, redirect
from .forms import NotesForm
from .models import Notes


def notes(request):
    notes = Notes.objects.all()
    context = {'notes': notes}
    return render(request, 'notes.html', context)


def single_note(request, pk):
    note_obj = Notes.objects.get(id=pk)
    return render(request, 'single_note.html', {'note_obj': note_obj})


def create_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = {'form': form}
    return render(request, 'notes_form.html', context)


def update_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = {'form': form}
    return render(request, 'notes_form.html', context)


def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {'note': note}
    return render(request, 'delete_note.html', context)
