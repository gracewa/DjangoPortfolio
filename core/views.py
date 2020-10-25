from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photo


def index(request):
    locations = ['Nairobi', 'Mombasa', 'Online', 'Abroad']
    context = {
        'photos': Photo.objects.all(),
        'locations':locations
    }
    return render(request, 'gallery.html', context)

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photo_detail.html', context)

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't entered a search term"
        return render(request, 'search.html',{"message":message})

def search_locations(request, search_term):
    photos = Photo.search_by_location(search_term)
    context = {
        'photos': photos,
        'search_term': search_term
    }
    return render(request, 'location.html', context)