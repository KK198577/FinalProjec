from django.shortcuts import render
from django.views.generic import TemplateView
from viewer.models import Book, Genre, Author


# Create your views here.
def home(request):
	return render(request, template_name="index.html")


def new_books(request):
	book_list = Book.objects.all()
	genres_list = Genre.objects.all()
	context = {'books': book_list, 'genres': genres_list}
	return render(request, template_name='index.html', context=context)


# class NewBookView(TemplateView):
# 	template_name = "index.html"
# 	book_list = Book.objects.all()
# 	genres_list = Genre.objects.all()
# 	extra_context = {'books': book_list, 'genres': genres_list}
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context["books"] = Book.objects.all()
# 		return context


def authors(request):
	author_list = Author.objects.all()
	context = {'authors': author_list}
	return render(request, template_name='authors.html', context=context)


# def books(request):
# 	book_list = Book.objects.all()
# 	genre_list = Genre.objects.all()
# 	author_list = Author.objects.all()
# 	context = {'books': book_list, 'genre': genre_list, 'author': author_list}
# 	return render(request, template_name='books.html', context=context)

class BooksView(TemplateView):
	template_name = 'books.html'
	book_list = Book.objects.all()
	genre_list = Genre.objects.all()
	author_list = Author.objects.all()
	extra_context = {'books': book_list, 'genres': genre_list, 'author': author_list}

