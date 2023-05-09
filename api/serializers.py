from django.db.models import fields
from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_file']

class PostSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'images', 'created_at']
    
    # def get_username(self, obj):
    #     return obj.user.username

class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'comment_post', 'username', 'content', 'created_at']
