from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import get_object_or_404

from rest_framework import permissions
from .permissions import IsAdminOrReadOnly, IsCommentatorOrReadOnly
from rest_framework.exceptions import ValidationError


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes =[IsAdminOrReadOnly]


class CommentAdd(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user = self.request.user
        comment = Comment.objects.filter(book=book, commentator = user)
        if comment.exists():
            raise ValidationError('You have already commented this book.')
        serializer.save(book=book, commentator=user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes=[IsCommentatorOrReadOnly]

# class BookList(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)