from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', api_views.BookDetail.as_view(), name='book-detail'),
    path('books/<int:book_id>/add_comment', api_views.CommentAdd.as_view(), name='add-comment'),
    path('comments/<int:pk>', api_views.CommentDetail.as_view(), name='comment-detail'),
]