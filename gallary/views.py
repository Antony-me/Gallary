from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):



    return render(request, 'home.html')

def about(request):

    return render(request, 'about.html')



