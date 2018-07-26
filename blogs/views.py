from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name='blogs/index.html'
    context_object_name='blogs_list'
    #queryset = .objects.all