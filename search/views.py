from django.shortcuts import render
from .models import Book
import requests

# Create your views here.
def search_book(request):
    isbn = requests.Get.get('isbn', '')

    api_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&callback=mycallback"
    response = requests.get(api_url)
    data = response.json()

    book_data = data[f'ISBN:{isbn}']
    title = book_data['title']
    author = book_data['authors'][0]['name']

    book = Book(title=title, author=author, isbn=isbn)
    book.save()

    return render(request, 'book_search.html' ,{'book': book}) 