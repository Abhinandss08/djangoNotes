from django.shortcuts import render, redirect
from .forms import NotesForm
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def notes(request):
    notes = Notes.objects.all()
    context = {'notes': notes}
    return render(request, 'notes.html', context)


@login_required(login_url='login')
def single_note(request, pk):
    note_obj = Notes.objects.get(id=pk)
    return render(request, 'single_note.html', {'note_obj': note_obj})


@login_required(login_url='login')
def create_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            return redirect('notes')
    context = {'form': form}
    return render(request, 'notes_form.html', context)


@login_required(login_url='login')
def update_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        if note.owner == request.user:
            form = NotesForm(request.POST, request.FILES, instance=note)
            if form.is_valid():
                form.save()
                return redirect('notes')
        else:
            messages.error(request, 'Access denied!')
    context = {'form': form}
    return render(request, 'notes_form.html', context)


@login_required(login_url='login')
def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        if note.owner == request.user:
            note.delete()
            return redirect('notes')
        else:
            messages.error(request, 'Access denied!')
    context = {'note': note}
    return render(request, 'delete_note.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('notes')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notes')
        else:
            messages.error(request, 'Username or password is incorrect!')
    context = {'page': page}
    return render(request, 'login_register.html', context)


def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account is created!')
            login(request, user)
            return redirect('notes')
        else:
            messages.error(request,
                           'An error has occurred during registration')
    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')
