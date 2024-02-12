from project.client import Client
from project.meals.meal import Meal

class FoodOrdersApp:
    types_of_meals = ["Starter", "MainDish", "Dessert"]
    receipts = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if client:
            raise Exception(f"The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ not in self.types_of_meals:
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")
        result = [m.details() for m in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)
        else:
            client = client[0]
        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name]
            if not meal:
                client.shopping_cart = []
                client.bill = 0.0
                raise Exception(f"{meal_name} is not on the menu!")
            meal = meal[0]
            if meal.quantity < meal_quantity:
                client.shopping_cart = []
                client.bill = 0.0
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            client.shopping_cart.append(meal)
            client.bill += meal.price * meal_quantity
        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity
        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity
        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception(f"There are no ordered meals!")
        client.shopping_cart = []
        paid = client.bill
        client.ordered_meals = {}
        client.bill = 0.0
        self.receipts += 1
        return f"Receipt #{self.receipts} with total amount of {paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

