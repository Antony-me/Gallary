from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here. 

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Category(name='Game')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)
        self.image_test.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))
 
    '''
     Test to test save image method
    ''' 
    
    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)


    '''
     Test to test delete image method
    ''' 

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    '''
     Test to test update image method
    ''' 

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    '''
     Test to test get-image-by id  method
    ''' 

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(id=1)
        image = Image.objects.filter(id=1)
        self.assertTrue(found_image, image)

    '''
     Test to test filter_image_by_location method
    ''' 


    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_images) == 1)


    '''
     Test to test search image by category method
    ''' 

    def test_search_image_by_category(self):
        found_img = self.image_test.search_by_category(self.category)
        image = Image.objects.all()
        self.assertTrue(found_img, image)

    '''
     Test to test filter_image_by_location method
    ''' 


    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_images) == 1)

    '''
     Tear Down
    '''

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class TestLocation(TestCase):
    '''
    setup Method
    '''

    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    '''
    Test to test save_location method
    '''

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    
    '''
    Test to test get_location method
    '''

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(locations, 'Nairobi') 


    
    '''
    Test to test Update_location method
    '''

    def test_update_location(self):
        self.location.update_location(id=1, value='Nowhere')
        locations = Location.get_locations()
        self.assertTrue(locations, 'Nowhere' )

    
    '''
    Test to test delete_location method
    '''

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):

    '''
    SetUp method
    '''

    def setUp(self):
        self.category = Category(name='Game')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    
    '''
    Test to test save_category method
    '''

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    '''
    Test to test delete_category method
    '''

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)