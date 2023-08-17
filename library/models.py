from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    download_url = models.URLField()
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.name
