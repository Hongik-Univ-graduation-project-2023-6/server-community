from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import filters as df_filters
from django_filters.rest_framework import DjangoFilterBackend


class PostFilter(FilterSet):
	username = df_filters.CharFilter(field_name='username')
	class Meta:
		model = Post
		fields = ['username']

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostDetailSerializer
    serializer_action_classes = {
        'list': PostSerializer,
    }
    queryset = Post.objects.all().order_by('-created_at')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilter

    search_fields = ['title', 'content']
    
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
