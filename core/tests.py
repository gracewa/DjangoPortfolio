from django.test import TestCase
from .models import Photo


class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.flaskip= Photo(title = 'Minute Pitch', description = 'A website where users can submit one-minute pitches.', image ='../media/images/opener.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.flaskip, Photo))

    def test_save_method(self):
        self.flaskip.save_image()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_method(self):
        self.flaskip.save_image()
        instance = Photo.objects.get(id=1)
        instance.delete_image()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) == 0)
