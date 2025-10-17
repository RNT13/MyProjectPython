from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
