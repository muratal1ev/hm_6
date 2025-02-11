from django.urls import path
from app.blog.views import BlogView, BlogDetailView

urlpatterns = [
    path("blog/", BlogView.as_view(), name='blog'),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name='blog_detail')
]
