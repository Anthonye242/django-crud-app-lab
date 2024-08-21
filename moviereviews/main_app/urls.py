from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('reviews/', views.review_index, name='review-index'),
    path('reviews/<int:review_id>/', views.review_detail, name='review-detail'),
    path('reviews/create/', views.review_create, name='review-create'),
    path('reviews/<int:review_id>/update/', views.review_update, name='review-update'),
    path('reviews/<int:review_id>/delete/', views.review_delete, name='review-delete'),
    path('comments/<int:comment_id>/update/', views.comment_update, name='comment-update'),
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='comment-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
