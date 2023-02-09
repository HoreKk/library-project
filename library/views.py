from django.shortcuts import  render, redirect
from .forms import NewUserForm, BookForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={ "register_form": form })


class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'home.html'

class BookListView(UserPassesTestMixin, ListView):
	model = Book
	template_name = 'back/list_books.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['book_fields'] = [f.name for f in Book._meta.get_fields()]
		return context

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre', 'library']
	template_name = 'back/edit_book.html'
	success_url = '/books'

class BookUpdateView(LoginRequiredMixin, UpdateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre', 'library']
	template_name = 'back/edit_book.html'
	success_url = '/books'