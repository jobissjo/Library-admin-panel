from django.urls import path
from . import views
app_name = 'members'
urlpatterns = [
    path('book_form/', views.book_form, name='book_form'),
    path('borrow_list/', views.borrow_list, name='borrow_list'),
    path('edit_profile/<int:id>', views.borrow_list_edit, name='edit_profile'),
    # path('class_edit_profile/<int:pk>', views.Member_update_view.as_view(), name='c_edit_profile'),
    # path('claas_view_memeber/<int:pk>/', views.Task_details_view.as_view(),name='cbvdetail'),
]