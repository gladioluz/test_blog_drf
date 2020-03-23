from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer


class PostsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = Post.objects.filter(user_id=request.user.id).all()
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data})


class PostView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        post = request.data
        post['user'] = request.user.id
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response({"success": f"Post '{post_saved.content}' created successfully"})


class PostLikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        like = request.data
        like['user'] = request.user.id
        message = None
        try:
            like = Like.objects.get(post=like['post'], user=like['user'])
            like.delete()
            message = 'unliked'
        except Like.DoesNotExist:
            serializer = LikeSerializer(data=like)
            if serializer.is_valid(raise_exception=True):
                like_saved = serializer.save()
                message = 'liked'

        return Response({'success': message})
