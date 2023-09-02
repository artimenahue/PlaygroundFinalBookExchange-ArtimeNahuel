from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'photo']

class SearchBooksForm(forms.Form):
    query = forms.CharField(label='Buscar libros', max_length=100)

class ExchangeRequestForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    book_to_exchange = forms.ModelChoiceField(
        queryset=Book.objects.none(),
        empty_label="Selecciona un libro para intercambiar"
    )

    def __init__(self, user, *args, **kwargs):
        super(ExchangeRequestForm, self).__init__(*args, **kwargs)
        # Filtra los libros del usuario actual para el campo de selección
        self.fields['book_to_exchange'].queryset = Book.objects.filter(user=user)

class CustomUserCreationForm(UserCreationForm):
    # Agrega un atributo help_text personalizado para el campo de contraseña
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Ingresa una contraseña segura."
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Repite la misma contraseña para verificar."
    )

    class Meta:
        model = User
        fields = ("username",)