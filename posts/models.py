from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Post(models.Model):

    class Meta:
        db_table = 'posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-created',)

    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):

    class Meta:
        db_table = 'likes'
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        unique_together = ('user_id', 'post_id')

    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
