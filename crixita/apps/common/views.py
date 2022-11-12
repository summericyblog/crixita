from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Tag
from .utils import get_father


class TagView(generic.ListView):
    model = Tag
    paginate_by = 100
    template_name = 'tag/tag.html'
    context_object_name = 'tag_list'


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/tag_edit.html'
    success_url = reverse_lazy('tag')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/tag_edit.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])


def edit_tag_father():
    pass


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'tag/tag_edit.html'
    success_url = reverse_lazy('tag')

    def get_object(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'tag/tag_detail.html'

    def get_object(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        ctx = super(TagDetailView, self).get_context_data(**kwargs)
        this_tag = ctx['object']
        ctx['direct_fathers'] = this_tag.fathers.all()
        ctx['fathers'] = get_father(this_tag)
        return ctx