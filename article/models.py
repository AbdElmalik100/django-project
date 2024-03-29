from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")


