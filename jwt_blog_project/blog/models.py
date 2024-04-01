# models.py

from django.db import models
# from django.contrib.auth.models import User
#
# class UserDetails(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.CharField(max_length=50)
#     phone_number = models.IntegerField()
#     def __str__(self):
#         return f"User Details for {self.user.username}"
#
#
#
# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#
#
#
#     def __str__(self):
#         return f"Profile for {self.user.username}"

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ManyToManyField(Author)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





