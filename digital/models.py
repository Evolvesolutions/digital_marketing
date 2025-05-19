# from django.db import models

# # Create your models here.
# class BlogPost(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog_images/')
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

