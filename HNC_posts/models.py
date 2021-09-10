from django.db import models
from django.contrib.auth.models import User

# A model to store Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=0)

    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-number_of_votes']

    def __str__(self):
        return '{}'.format(self.title)

# A model to store votes    
class Vote(models.Model):
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.CASCADE)

    author = models.ForeignKey(User, related_name="votes", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.post.number_of_votes = self.post.number_of_votes + 1
        self.post.save()

        super(Vote, self).save(*args, **kwargs)

# A model to store comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
