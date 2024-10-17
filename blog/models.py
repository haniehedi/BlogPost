from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.title


