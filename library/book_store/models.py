from django.db import models

# Create your models here.
STATUS = [
    ('Available', 'Available'),
    ('Not Available', 'Not Available'),
    ('Comming Soon', 'Comming Soon'),
]
class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=50)
    rating = models.CharField(max_length=1)
    status = models.CharField(max_length=50, choices=STATUS)
    image = models.ImageField(upload_to='book_image')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']
    
    def __str__(self):
        return self.name
