from django.shortcuts import render

from .forms import contact_form
from blog_posts.models import post_model
# Create your views here.
def home(request):
    qs = post_model.objects.published()
    context={
     'title':'home' ,
     'query':qs
    }
    return render(request , 'home.html' ,context)

def about (request):
    return render(request , 'about.html' , {'title':'about'})

def contact(request):
    form = contact_form(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        descrption = form.cleaned_data['descrption']
        form = contact_form()
    return render(request , 'form.html' ,{'form':form ,'title':'contact us'})
