from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here
def home(request):

    images = Image.get_images()
 
    return render(request, 'gallary/home.html', {'images':images})

def about(request):

    return render(request, 'about.html')

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'gallary/location.html', {'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'gallary/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "There are no images in that category"
        return render(request, 'gallary/search_results.html', {"message": message})
