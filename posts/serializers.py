from rest_framework import serializers

from posts.models import User, Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'content')

    def create(self, data):
        return Post.objects.create(**data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user')

    def create(self, data):
        return Like.objects.create(**data)
