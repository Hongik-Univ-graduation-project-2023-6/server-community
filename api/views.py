from django.shortcuts import render
from .models import *
from .serializers import *
from .pagination import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import filters as df_filters
from django_filters.rest_framework import DjangoFilterBackend


class PostFilter(FilterSet):
	username = df_filters.CharFilter(field_name='username')
	class Meta:
		model = Post
		fields = ['username']

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPageNumberPagination
    serializer_class = PostSerializer
    serializer_action_classes = {
        'retrieve': PostDetailSerializer,
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
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        try:
            uploaded_data = request.data.pop('post_images')
            for uploaded_item in uploaded_data:
                new_post_image = Image.objects.create(image_post=post, image_file=uploaded_item)
        except:
            pass
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
