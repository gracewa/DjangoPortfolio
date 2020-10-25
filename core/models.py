from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    LOCATION_CHOICES = (
    ("Nairobi", "Nairobi"),
    ("Mombasa", "Mombasa"),
    ("Online", "Online"),
    ("Abroad", "Abroad"),
)
    name = models.CharField(max_length=100, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='noimage.png')
    description = models.CharField(max_length=500, default='no description')
    category = models.ForeignKey(Category, blank=True,
        null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, blank=True,
        null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__name=search_term)
        return photos

    @classmethod
    def search_by_location(cls, search_term):
        photos = cls.objects.filter(location__name=search_term)
        return photos