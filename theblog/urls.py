from django.urls import path 
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView, UpdateCommentView, DeleteCommentView, TestView, TagIndexView
from . import views

#, PreviewPostView, 

urlpatterns = [
  #  path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('test', TestView.as_view(), name="test"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"), # int: integer, pk: primary key
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('add_post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('add_post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),   
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('tags/<slug:tag_slug>/', views.TagIndexView.as_view(), name='posts_by_tag'),
 #   path('tags/<str:tagname>/', views.TagIndexView.as_view(), name='posts_by_tag'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('article/<int:pk>/comment/edit', UpdateCommentView.as_view(), name="update_comment"),
    path('article/<int:pk>/comment/remove', DeleteCommentView.as_view(), name="delete_comment"),
####    path("ckeditor/", include('ckeditor_uploader.urls')), 
]
