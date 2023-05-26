from django.tests import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Lemon dessert", price=7.00, menu_item_description="")
        self.assertEqual(item, "Lemon dessert : 7.00")