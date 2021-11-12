from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
#from taggit.models import Tag
# Create your models here.


class Tag(models.Model):
    tagname = models.CharField(max_length=50)
#    slug = models.SlugField(blank=True)
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
       return self.name
             
    def get_absolute_url(self):
       return reverse('home')
       
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank = True)
    facebook_url = models.CharField(max_length=255, null=True, blank = True)
    twitter_url = models.CharField(max_length=255, null=True, blank = True)
    instagram_url = models.CharField(max_length=255, null=True, blank = True)
    
    def __str__(self):
       return str(self.user)
       
    def get_absolute_url(self):
       return reverse('home') 

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='タイトル')
    header_image = models.ImageField(null=True, blank=True, upload_to="images/post/", verbose_name='画像')
    #title_tag = models.CharField(max_length=255, default="MyBlog")
    #title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 #   body = RichTextField(blank=True, null=True)
    body = models.TextField(default='' , verbose_name='内容')
  #  body = models.CharField()
   # post_date = models.DateField(auto_now_add=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
  #  genre = models.CharField(max_length=255, default='...', verbose_name='カテゴリ')
  #  snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    solved = models.BooleanField(default=False)
    tags = TaggableManager(verbose_name='タグ')

    def total_likes(self):
       return self.likes.count()
    
    def __str__(self):
       return self.title + ' | ' + str(self.author)
       
    def get_absolute_url(self):
#       return reverse('article-detail', args=(str(self.id)) )
       return reverse('home')
       
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment_image = models.ImageField(null=True, blank=True, upload_to="images/comment/", verbose_name='画像')
#    name = models.CharField(max_length=255)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='内容')
 #   body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
        
    def get_absolute_url(self):
#        return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')


