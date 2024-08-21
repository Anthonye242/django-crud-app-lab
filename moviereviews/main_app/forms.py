from django import forms
from .models import MovieReview, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'release_date', 'genre', 'rating', 'review_text', 'reviewer_name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']  
