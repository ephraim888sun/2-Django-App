from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

# def portfolio(request):
#     return render(request, 'home/portfolio.html')

class portfolio(generic.ListView):
    model = Post
    template_name = 'home/portfolio.html'

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = ''
# #
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'home/post_detail.html'
