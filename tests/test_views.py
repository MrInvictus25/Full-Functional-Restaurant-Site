from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(cls):
        cls.firstItem = Menu.objects.create(name = 'Lemon dessert', price = 7.00)
        cls.secondItem = Menu.objects.create(name='Grilled fishhhh', price = 19.00)

    def test_getall(self):
        menu = Menu.objects.all()
        self.assertIsInstance(self.firstItem.name, str)
        self.assertIsInstance(self.firstItem.price, int)
        self.assertIsInstance(self.secondItem.name, str)
        self.assertIsInstance(self.secondItem.price, int)
        