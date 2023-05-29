from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Lemon dessert", price=7.00, menu_item_description="")
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Lemon dessert : 17.00")