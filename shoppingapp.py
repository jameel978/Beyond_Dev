class ShoppingItem:
    def __init__(self, name):
        self.name = name
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True
    
    def check_if_purchased(self):
        return self.purchased

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} {'(Purchased)' if self.purchased else ''}"


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name):
        item = ShoppingItem(item_name)
        self.items.append(item)

    def mark_item_as_purchased(self, item_index):
        if 0 <= item_index < len(self.items):
            if not self.items[item_index].check_if_purchased():
                self.items[item_index].mark_as_purchased()
            else:
                raise Exception("Item Already Purchased")
        else:
            raise IndexError("Invalid item index")

    def display_list(self):
        print(f"Shopping List: {self.name}")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item}")
        print()

    def get_items(self):
        return self.items


class ShoppingListApp:
    def __init__(self):
        self.shopping_lists = {}

    def create_shopping_list(self, list_name):
        if list_name in self.shopping_lists:
            #print("Shopping list with that name already exists.")
            pass
        else:
            self.shopping_lists[list_name] = ShoppingList(list_name)
            #print(f"Shopping list '{list_name}' created successfully.")

    def add_item_to_list(self, list_name, item_name):
        try:
            self.shopping_lists[list_name].add_item(item_name)
            #print(f"Item '{item_name}' added to '{list_name}' successfully.")
            pass
        except KeyError:
            #print(f"Shopping list '{list_name}' does not exist.")
            pass

    def mark_item_as_purchased(self, list_name, item_name):
        try:
            shopping_list = self.shopping_lists[list_name].get_items()
            for idx, item in enumerate(shopping_list):
                if item.name.lower() == item_name.lower():
                    try:
                        self.shopping_lists[list_name].mark_item_as_purchased(idx)
                        #print(f"Item '{item_name}' marked as purchased.")
                        pass
                    except Exception as e:
                        #print(f"Error: {e}")
                        pass
                    return
            #print(f"Item '{item_name}' does not exist in Shopping list '{list_name}'")
            pass
        except KeyError:
            #print(f"Shopping list '{list_name}' does not exist.")
            pass

    def display_all_lists(self):
        if not self.shopping_lists:
            #print("No shopping lists available.")
            pass
        else:
            for shopping_list in self.shopping_lists.values():
                shopping_list.display_list()
