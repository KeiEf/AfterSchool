from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, PostEditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#from django.db.models import Count
from taggit.models import Tag
#from formtools.preview import FormPreview


# Create your views here.
#def home(request):
#    return render(request, 'home.html',{})

class TestView(ListView):
    model = Post
    template_name = 'test.html'
    
    
def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:       
       post.likes.add(request.user)
       liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
  #  ordering = ['-id']
    ordering = ['-post_date']
    paginate_by = 10

 #   def get_context_data(self, *args, **kwargs):
 #       cat_menu = Category.objects.all()
 #       context = super(HomeView, self).get_context_data(*args, **kwargs)
 #       context["cat_menu"] = cat_menu
 #       return context

class TagIndexView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

        
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})        

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})
      
###

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
           liked = True
                
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
  #  fields = '__all__'

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'preview_post.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'add_post.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'update_post.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'preview_post_update.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'update_post.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))

#        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})


####

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html' 
    fields = '__all__'
  #  success_url =reverse_lazy('home')


####

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url =reverse_lazy('home')
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    # fields = '__all__'

    def form_valid(self, form):
        ctx = {'form': form}
        form.instance.post_id = self.kwargs['pk']
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'preview_comment.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'add_comment.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))

  #  def form_valid(self, form):
  #      form.instance.post_id = self.kwargs['pk']
  #      return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})

class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
  #  success_url =reverse_lazy('home')

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'preview_comment_update.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'update_comment.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('home'))


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url =reverse_lazy('home')



