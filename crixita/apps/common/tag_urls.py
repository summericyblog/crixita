from django.urls import path

from . import views

urlpatterns = [
    path('', views.TagView.as_view(), name='tag'),
]