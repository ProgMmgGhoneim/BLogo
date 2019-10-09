from django.shortcuts import render ,get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import post_model
from .forms import post_form

# Create your views here.
def post_list(request):
    post_qs = post_model.objects.published()
    if request.user.is_authenticated:
        qs =post_model.objects.filter(user=request.user)
        post_qs = (qs|post_qs).distinct()
    return render(request , 'blog_post/post_list_template.html' , {'posts':post_qs ,'title':'post'})

def post_details(request ,slug):
    spe_post = get_object_or_404(post_model , slug=slug)
    template_name='blog_post/post_details_template.html'
    context ={
    'posts_details':spe_post
    }
    return render(request , template_name ,context)

@staff_member_required
def post_create(request):
    form = post_form(request.POST or None ,request.FILES or None)
    if form.is_valid():
        obj = form.save(commit =False)
        obj.user = request.user
        obj.save()
        form.save()
        form =post_form()
    template_name = 'blog_post/post_create_template.html'
    context ={'form':form}
    return render(request , template_name ,context)

@staff_member_required
def post_update(request ,slug):
    obj = get_object_or_404(post_model , slug=slug)
    form = post_form(request.POST or None  ,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog_post/post_update_template.html'
    context ={'form':form}
    return render(request , template_name ,context)

@staff_member_required
def post_delete(request , slug):
    obj = get_object_or_404(post_model , slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog/posts')
    template_name = 'blog_post/post_delete_template.html'
    context ={
    'object':obj
    }
    return render(request , template_name ,context)
