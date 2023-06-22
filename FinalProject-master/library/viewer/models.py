from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Person(models.Model):
	user = models.OneToOneField(User, on_delete=CASCADE)
	pay_to = models.DateField()


class Genre(models.Model):
	name = models.CharField(max_length=32, unique=True)

	class Meta:
		verbose_name_plural = "Genres"
		ordering = ['name']

	def __str__(self):
		return f"{self.name}"


class Author(models.Model):
	name = models.CharField(max_length=32, null=False)
	birth_date = models.DateField(null=True)
	country = models.CharField(max_length=32, null=True)
	biography = models.TextField

	class Meta:
		ordering = ['name', 'birth_date']

	def __str__(self):
		return f"{self.name} - {self.country} ({self.birth_date})"


class Language(models.Model):
	language = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.language}"


class Book(models.Model):
	name = models.CharField(max_length=64, null=False, blank=False)
	original_name = models.CharField(max_length=64, null=False, blank=False)
	genre = models.ManyToManyField(Genre)
	year = models.PositiveIntegerField(null=True)
	language = models.ManyToManyField(Language)
	author = models.ManyToManyField(Author)
	image = models.CharField(max_length=256, blank=True, null=True)
	description = models.TextField()
	page = models.PositiveIntegerField()
	isbn = models.CharField(max_length=32, null=False)
	amount = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.name} - {self.author} ({self.year})"


class Rented(models.Model):
	id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, default=None)
	id_user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, default=None)
	rent_date = models.DateField(blank=True)
	reservation_date = models.DateField(auto_now_add=True)
	return_date = models.DateField(blank=True)


class Rating(models.Model):
	id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, default=None)
	id_user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, default=None)
	rating = models.PositiveIntegerField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
	id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, default=None)
	id_user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, default=None)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
