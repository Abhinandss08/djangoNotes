from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.notesList),
    path('notes/<str:pk>/', views.singleNote)
]
