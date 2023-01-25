# forms.py
from django import forms
from .models import Book
class SearchForm(forms.Form):
    q = forms.CharField(label='Search')

class BookAddForm(forms.ModelForm):
    description = forms.CharField(
        label= "Description",
        widget=forms.Textarea(attrs={
            'row': 5
        })
    )
    class Meta:
        model = Book
        fields = '__all__'
    