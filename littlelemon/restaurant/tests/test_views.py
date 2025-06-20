from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item_1 = Menu.objects.create(Title = "IceCream",
                                   Price = 80,
                                   Inventory = 100)
        self.menu_item_2 = Menu.objects.create(Title = "Noodles",
                                   Price = 40,
                                   Inventory = 200)
        self.menu_item_3 = Menu.objects.create(Title = "Burger",
                                   Price = 20,
                                   Inventory = 1000)
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many = True).data
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_items)