from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sensors/<int:id>/log', views.api_log, name='index'),
]
