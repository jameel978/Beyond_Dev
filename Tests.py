import unittest
from shoppingapp import ShoppingItem, ShoppingList, ShoppingListApp


class TestStringMethods(unittest.TestCase):
    def test_add_item_shoppinglist(self):
        shopping_list = ShoppingList("Groceries")
        shopping_list.add_item("Milk")
        shopping_list.add_item("Bread")
        self.assertEqual(len(shopping_list.get_items()),2)

    def test_mark_item_as_purchased_shoppinglist(self):
        shopping_list = ShoppingList("Groceries")
        shopping_list.add_item("Milk")
        shopping_list.mark_item_as_purchased(0)
        self.assertTrue(shopping_list.get_items()[0].check_if_purchased())

    def test_mark_item_as_purchased_invalid_index_shoppinglist(self):
        shopping_list = ShoppingList("Groceries")
        shopping_list.add_item("Milk")
        try:
            shopping_list.mark_item_as_purchased(5)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_create_shopping_list_shoppinglist(self):
        shopping_app = ShoppingListApp()
        shopping_app.create_shopping_list("Groceries")
        self.assertIn("Groceries",shopping_app.shopping_lists)

    def test_add_item_to_list_shoppinglist(self):
        shopping_app = ShoppingListApp()
        shopping_app.create_shopping_list("Groceries")
        shopping_app.add_item_to_list("Groceries", "Milk")
        self.assertEqual(len(shopping_app.shopping_lists["Groceries"].get_items()),1)

    def test_mark_item_as_purchased_shoppingapp(self):
        shopping_app = ShoppingListApp()
        shopping_app.create_shopping_list("Groceries")
        shopping_app.add_item_to_list("Groceries", "Milk")
        shopping_app.mark_item_as_purchased("Groceries", "Milk")
        self.assertTrue(shopping_app.shopping_lists["Groceries"].get_items()[0].check_if_purchased())

    def test_mark_item_as_purchased_item_not_exist_shoppingapp(self):
        shopping_app = ShoppingListApp()
        shopping_app.create_shopping_list("Groceries")
        shopping_app.add_item_to_list("Groceries", "Milk")
        try:
            shopping_app.mark_item_as_purchased("Groceries", "Eggs")
            self.assertTrue(False)
        except:
            self.assertTrue(True)







