from django.db import models


class Statistic(models.Model):

    post_id = models.CharField('Post ID', max_length=17, blank=False, null=False)
    user_id = models.CharField('User ID', max_length=10, blank=False, null=False)
    likes = models.IntegerField('Likes', blank=False, null=False, default=0)

    created_at = models.DateTimeField('Created at')

    def __str__(self):
        return f'User ID: {self.user_id}, Post ID: {self.post_id}, Likes: {self.likes}'

    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'
