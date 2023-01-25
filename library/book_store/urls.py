from django.urls import path
from . import views

app_name = 'book_store'
urlpatterns = [
    path('', views.home, name='home'),
    path('book_details/', views.book_details, name='book_details'),
    path('book_details/<int:id>', views.book_detail, name='book_detail'),
    path('fantasy', views.fantasy, name='fantasy'),
    path('self_help', views.self_help, name='self_help'),
    path('fiction', views.fiction, name='fiction'),
    path('add_book', views.add_book, name='add_book'),
    path('search', views.search, name='search')
    # path('',views.search, name='book_details')
]