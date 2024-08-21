from django.db import models
from django.contrib.auth.models import User

class MovieReview(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    review_text = models.TextField()
    reviewer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(MovieReview, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure User model is imported

    def __str__(self):
        return f'Comment by {self.author} on {self.review}'
