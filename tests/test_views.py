from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.firstItem = Menu.objects.create(name = 'Lemon dessert', price = 7.00)
        cls.secondItem = Menu.objects.create(name='Grilled fish', price = 9.00)

    def test_getall(self):
        #menu = Menu.objects.all()
        self.assertEqual(self.firstItem.name, 'Lemon dessert')
        self.assertEqual(self.firstItem.price, 7.00)
        self.assertEqual(self.secondItem.name, 'Grilled fish')
        self.assertEqual(self.secondItem.price, 9.00)
        