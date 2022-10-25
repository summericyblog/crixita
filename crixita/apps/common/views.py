from django.shortcuts import render
from django.views import generic

from .models import Tag


class TagView(generic.ListView):
    model = Tag
    paginate_by = 100
    template_name = 'tag/tag.html'
