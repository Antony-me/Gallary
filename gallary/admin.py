from django.contrib import admin
from .models import Cartegory, Location, Photo

# Register your models here.

admin.site.register(Location)
admin.site.register(Cartegory)
admin.site.register(Photo)