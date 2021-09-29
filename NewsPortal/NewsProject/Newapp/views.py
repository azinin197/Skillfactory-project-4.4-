from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Category, Post, PostCategory, Comment
from django.contrib.auth.models import User
from datetime import *
from .filters import PostFilter
from .forms import PostForm

class PostView(ListView):
    model = Post
    template_name = 'postlist.html'
    context_object_name = 'postlist'
    ordering = ['-id']
    paginate_by = 8


    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = self.get_filter()
        return context

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        title = request.POST['title']
        post_text = request.POST['post_text']
        post_category = request.POST['category']

        post = Post(title=title, post_text=post_text)
        post.save()
        cat = Category.objects.get(pk=post_category)
        post.post_category.add(cat)
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostDetailView(DetailView):
    template_name = "flatpages/post_detail.html"
    queryset = Post.objects.all()

class PostCreateView(CreateView):
    template_name = "flatpages/post_create.html"
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = "flatpages/post_create.html"
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'flatpages/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/postlist/'