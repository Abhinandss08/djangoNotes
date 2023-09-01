from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('notes/', views.notes, name="notes"),
    path('single-note/<str:pk>/', views.single_note, name="single-note"),
    path('create-note/', views.create_note, name="create-note"),
    path('update-note/<str:pk>/', views.update_note, name="update-note"),
    path('delete-note/<str:pk>/', views.delete_note, name="delete-note"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
