from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, Publisher
from django.views.generic import ListView

# Create your views here.


# def search_form(request):
#     return render(request, "books/search-form.html")


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books': books, 'query': q})
    return render(request, "books/search-form.html", {"error": error})


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
