from django import forms
from .models import Post, Category, Comment
#from tinymce.widgets import TinyMCE
#from formtools.preview import FormPreview
#from django.shortcuts import redirect


choices = Category.objects.all().values_list('name','name')
choice_list = []
#genre_list = [('質問','質問'),('雑談','雑談'), ('その他','その他')]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author',  'tags', 'body',  'header_image')
        
      #  body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
        #    'author': forms.Select(attrs={'class': 'form-control'}),
         #   'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        #    'genre': forms.Select(choices=genre_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id':'inp_bd', 'placeholder':'改行は<br>'}),
         #   'snippet': forms.Textarea(attrs={'class': 'form-control'}),
          #   'tags': forms.TextInput(attrs={'class': 'form-control'})

        }
        

        
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'tags', 'body' ,  'header_image')
        widgets = {
         #   'header_image' : forms.FileInput(attrs={'class': 'input-image-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトル'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
         #   'snippet': forms.Textarea(attrs={'class': 'form-control'}), 
          #  'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'category', 'body' )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title PlaceHolder'}),
        #    'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
         #   'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
       #     'genre': forms.Select(choices=genre_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
         #   'snippet': forms.Textarea(attrs={'class': 'form-control'}),       
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body' , 'comment_image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
#            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id':'phrase'}),
        }