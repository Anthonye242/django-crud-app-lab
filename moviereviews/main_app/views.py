from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views import View
from .models import MovieReview, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.forms import UserCreationForm

# Home view using LoginView
class Home(LoginView):
    template_name = 'home.html'

# Review index view
@login_required
def review_index(request):
    reviews = MovieReview.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

# Review detail view with comment form handling
@login_required
def review_detail(request, review_id):
    review = MovieReview.objects.get(id=review_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.review = review
            new_comment.user = request.user  # Associate the comment with the logged-in user
            new_comment.save()
            return redirect('review-detail', review_id=review.id)
    else:
        comment_form = CommentForm()
    return render(request, 'reviews/detail.html', {
        'review': review,
        'comment_form': comment_form,
        'comments': review.comments.all()
    })

# Review create view
@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review-index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html', {'form': form})

# Review update view
@login_required
def review_update(request, review_id):
    review = MovieReview.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review-detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/update.html', {'form': form, 'review': review})

# Review delete view
@login_required
def review_delete(request, review_id):
    review = MovieReview.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('review-index')
    return render(request, 'reviews/delete.html', {'review': review})

# Comment update view
@login_required
def comment_update(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('review-detail', review_id=comment.review.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/update.html', {'form': form, 'comment': comment})

# Comment delete view
@login_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    review_id = comment.review.id
    if request.method == 'POST':
        comment.delete()
        return redirect('review-detail', review_id=review_id)
    return render(request, 'comments/delete.html', {'comment': comment})

# Sign up view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('review-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
