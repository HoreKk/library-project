
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

class Editor(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  def __str__(self):
    return self.first_name + ' ' + self.last_name

class Collection(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Genre(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Library(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class CustomUser(AbstractUser):
  library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
  collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
  library = models.ForeignKey(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Loan(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  date = models.DateField()
  return_date = models.DateField()

  def __str__(self):
    return self.book.title + '-' + self.user.username

class Reading_Group(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Reading_Group_User(models.Model):

  class Status(models.TextChoices):
      PENDING = 'pending'
      REJECTED = 'rejected'
      ACCEPTED = 'accepted'

  status = models.CharField(
      max_length=10,
      choices=Status.choices
  )

  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  reading_group = models.ForeignKey(Reading_Group, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username + '-' + self.reading_group.name

class Session(models.Model):
  date = models.DateField()
  reading_group = models.ForeignKey(Reading_Group, on_delete=models.CASCADE)

  def __str__(self):
    return self.reading_group.name + '-' + self.date

admin.site.register(Editor)
admin.site.register(Collection)
admin.site.register(Genre)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Reading_Group)
admin.site.register(Reading_Group_User)
admin.site.register(Session)