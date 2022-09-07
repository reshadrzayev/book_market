from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="comments")
    # commentator = models.CharField(max_length=255)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )


    def __str__(self):
        return str(self.commentator)


