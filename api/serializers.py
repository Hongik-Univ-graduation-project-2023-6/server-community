from django.db.models import fields
from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_file']

class PostSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    post_images = ImageSerializer(many=True, required=False)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'post_images', 'comments_count', 'created_at']
    
    def get_comments_count(self, obj):
        return obj.post_comments.count()

class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'comment_post', 'username', 'content', 'created_at']

class PostDetailSerializer(PostSerializer):
    post_comments = CommentSerializer(many=True)

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['post_comments']
