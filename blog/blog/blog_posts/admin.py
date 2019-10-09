from django.contrib import admin

from .models import post_model

class post_admin(admin.ModelAdmin):
    list_display = ('title' , 'content' , 'slug' , 'published_data' ,'updated_data')

# Register your models here.
admin.site.register(post_model , post_admin)
