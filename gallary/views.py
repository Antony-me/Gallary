from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Location

# Create your views here
def home(request):

    images = Image.get_images()
    locations = Location.get_locations()
 
    return render(request, 'gallary/home.html', {'images':images, 'locations':locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    
    return render(request, 'gallary/location.html', {'images': images})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'gallary/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "There are no images in that category yet"
        return render(request, 'gallary/search_results.html', {"message": message})

