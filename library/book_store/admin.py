from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'author', 'rating', 'status']
    search_fields = ['name', 'genre', 'author']
    list_filter = ["status"]
    list_per_page = 10
admin.site.register(Book, BookAdmin)