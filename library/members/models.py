from django.db import models
from book_store.models import Book
# Create your models here.
BOOK_STATUS = [
    ('Borrowed', 'Borrowed'),
    ('Returned', 'Returned'),
]
class Member(models.Model):
    name = models.CharField(max_length=50)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    taken_date = models.DateField(auto_now_add=True,null=True,blank=True)
    return_date = models.DateField(null=True,blank=True)
    book_status = models.CharField(max_length=20,choices=BOOK_STATUS)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=1000)
    member_id = models.CharField(max_length=15)
         
    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = "Members"
        ordering = ['book_status']
    
    def __str__(self):
        return self.name
# date = member.taken_date.date()