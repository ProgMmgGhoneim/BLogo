from django.shortcuts import render

from .models import search_model
from blog_posts.models import post_model
# Create your views here.
def search (request):
    q =request.GET.get('query' , None)
    user=None
    context ={'query':q}
    if request.user.is_authenticated:
        user = request.user
        search_model.objects.create(user=user ,query=q)
        blog_list = post_model.objects.search(query=q)
        context['blog_list'] =blog_list

    return render(request ,'search.html' ,context)
