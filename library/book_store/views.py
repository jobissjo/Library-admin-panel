from django.shortcuts import render, redirect
from .models import Book
from .forms import SearchForm, BookAddForm
from django.contrib import messages
# Create your views here.

def home(request):
    books = Book.objects.all().order_by('-rating')
    non_fiction = Book.objects.filter(genre="Non-fiction")
    fiction = Book.objects.filter(genre="Fiction")
    self_help = Book.objects.filter(genre="Self-help")
    fantasy = Book.objects.filter(genre="Fantasy")
    money_management = Book.objects.filter(genre="Money Management")
    def only_three(li):
        return_list = []
        num = 0
        for book in li:
            if num > 2:
                break
            num += 1
            return_list.append(book)
        return return_list

    high_rated = only_three(books)
    fiction = only_three(fiction)
    self_help = only_three(self_help)
    fantasy = only_three(fantasy)
    money_management = only_three(money_management)
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['q']
        books = Book.objects.filter(name__contains=query)
        return render(request, 'home.html', {'books': books, 'search_form': search_form,})
    return render(request, 'home.html', 
    {'search_form': search_form, 'high_rated': high_rated,
    'fiction':fiction, 'self_help':self_help, 'fantasy':fantasy,
    'money_management':money_management})


def book_details(request):
    books = Book.objects.all().order_by('name')
    allbook = True
    return render(request, 'book_details.html', {'books':books, 'allbook':allbook})

def fiction(request):
    title = 'Fiction'
    books = Book.objects.filter(genre="Fiction").order_by('name')
    return render(request, 'book_details.html', {'books':books, 'title':title})

def fantasy(request):
    title = 'Fantasy'
    books = Book.objects.filter(genre="Fantasy").order_by('name')
    return render(request, 'book_details.html', {'books':books, 'title':title})


def self_help(request):
    title = 'Self-help'
    books = Book.objects.filter(genre="Self-help").order_by('name')
    return render(request, 'book_details.html', {'books':books, 'title':title})

def book_detail(request, id):
    single_book = Book.objects.filter(id=id)
    return render(request, 'book_details.html', {'single_book':single_book})
def add_book(request):
    if request.method == "POST":
        form = BookAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Record is Saved")
            return redirect('book_store:add_book')
        else:
            print("form is not valid")
            return render(request, 'add_book.html', {'form': form})
    else:
        form = BookAddForm()
        return render(request, 'add_book.html', {'form': form})


def search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['q']
        books = Book.objects.filter(name__contains=query)
        return render(request, 'search.html', {'books': books, 'search_form': search_form})
    return render(request, 'search.html', {'search_form': search_form})
# def search(request):
#     search_form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['q']
#         books = Book.objects.filter(name__contains=query)
#         return render(request, 'home.html', {'books': books, 'search_form': search_form})
#     return render(request, 'home.html', {'search_form': search_form})