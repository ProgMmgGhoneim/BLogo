from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


User = settings.AUTH_USER_MODEL
# Create your models here.
class post_model_Query_Set(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_data__lte=now)
    def search (self , query):
        lookup=(Q(title__icontains=query) |
                Q(content__icontains =query))
        return self.filter(lookup)

class post_modelManager(models.Manager):
    def get_queryset(self):
        return post_model_Query_Set(self.model ,using=self.db)

    def published(self):
        return self.get_queryset().published()
    def search(self , query):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class post_model(models.Model):
    user = models.ForeignKey(User , null =True ,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='image/' , null=True ,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    published_data = models.DateTimeField(auto_now=False, auto_now_add=False ,null=True ,blank=True)
    timestap = models.DateTimeField(auto_now_add=True ,null=True)
    updated_data = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = post_modelManager()

    class Meta:
        ordering =['-published_data' , '-updated_data']
    def __str__(self):
        return self.title
