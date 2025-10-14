from django.http import HttpResponse
from django.views import generic


class PostListView(generic.ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world. You're at the blog index.")
