from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('detele/<int:person_id>/', views.delete, name='delete'),
]