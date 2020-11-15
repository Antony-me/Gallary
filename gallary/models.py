from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)
  

    def get_categorys(cls):
        categorys = Category.objects.all()
        return categorys

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)
        

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,  on_delete = models.CASCADE)
    location = models.ForeignKey(Location,  on_delete = models.CASCADE)


    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
        

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, search_term):
        searched_image = Image.objects.filter(category__name__icontains=search_term)
        return searched_image


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']
