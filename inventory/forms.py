from django.forms import ModelForm
from django import forms
from .models import Books

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class BookForm(forms.Form):
    book_Name = forms.CharField()
    author_Name = forms.CharField()
    author_Image = forms.CharField()
    genre = forms.CharField()
    quantity = forms.CharField()

class BookSearchForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
