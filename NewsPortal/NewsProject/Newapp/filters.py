from django_filters import FilterSet, CharFilter
from .models import Post
from django.contrib.auth.models import User


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {

            'time_wr': ['date'],
            'post_author': ['exact'],
            'rating_post': ['gt']
        }