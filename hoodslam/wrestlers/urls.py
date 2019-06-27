from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<name>/', views.detail, name='wrestler-details'),
    path('match/<int:id>', views.match, name='match'),
]
