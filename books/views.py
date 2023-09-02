from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Book, ExchangeRequest
from .forms import AddBookForm, SearchBooksForm, ExchangeRequestForm

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  
            book.save()
            return redirect('book_list')
    else:
        form = AddBookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def search_books(request):
    query = request.GET.get('q')
    form = SearchBooksForm(initial={'query': query})
    books = []

    if query:
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'books/book_list.html', {'form': form, 'books': books})

@login_required
def request_exchange(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ExchangeRequestForm(user=request.user) 
        if form.is_valid():
            message = form.cleaned_data['message']
            book_to_exchange_id = form.cleaned_data['book_to_exchange']
            book_to_exchange = get_object_or_404(Book, pk=book_to_exchange_id)
            ExchangeRequest.objects.create(book=book, requester=request.user, book_to_exchange=book_to_exchange, message=message)
            return redirect('exchange_requested')

    else:
        form = ExchangeRequestForm(user=request.user)

    context = {'book': book, 'form': form}
    return render(request, 'books/request_exchange.html', context)

@login_required
def view_exchange_requests(request):
    user = request.user
    exchange_requests = ExchangeRequest.objects.filter(requester=user)
    context = {'exchange_requests': exchange_requests}
    return render(request, 'books/view_exchange_requests.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    print(request.user)
    return render(request, 'registration/profile.html')