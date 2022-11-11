from django.urls import path

from . import views

urlpatterns = [
    path('', views.TagView.as_view(), name='tag'),
    path('add/', views.TagCreateView.as_view(), name='tag-add'),
    path('edit/<slug:url>/', views.TagUpdateView.as_view(), name='tag-edit'),
]
