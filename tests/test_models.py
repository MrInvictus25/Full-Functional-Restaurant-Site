from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    #@classmethod
    def test_get_item(self):
        item = Menu.objects.create(name="Lemon dessert", price=7, menu_item_description="")
        self.assertEqual(item.name, "Lemon dessert")
        self.assertEqual(item.price, 7.00)

    # def test_getall(self):
    #     #menu = Menu.objects.all()
    #     self.assertEqual(self.item.name, 'Lemon dessert')
    #     self.assertEqual(self.item.price, 7.00)
