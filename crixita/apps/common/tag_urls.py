from django.urls import path

from . import views

urlpatterns = [
    path('', views.TagView.as_view(), name='tag'),
    path('add/', views.TagCreateView.as_view(), name='tag-add'),
    path('<slug:slug>/edit/', views.TagUpdateView.as_view(), name='tag-edit'),
    path('<slug:url>/edit_father/', views.TagEditFatherView.as_view(), name='tag-edit-father'),
    path('<slug:slug>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('<slug:slug>/', views.TagDetailView.as_view(), name='tag-detail'),
]
