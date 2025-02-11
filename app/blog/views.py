from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from app.blog.forms import CommentForm
from app.blog.models import Blog, Comment

class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_all'] = Blog.objects.all()
        return context

class BlogDetailView(CreateView,DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog_detail'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_all'] = Comment.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            Comment.objects.create(
                name=name,
                email=email,
                message=message
            )

        return redirect("blog")