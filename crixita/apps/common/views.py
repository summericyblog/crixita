from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Tag


class TagView(generic.ListView):
    model = Tag
    paginate_by = 100
    template_name = 'tag/tag.html'
    context_object_name = 'tag_list'


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/tag_edit.html'


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/tag_edit.html'

    def get_object(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])
