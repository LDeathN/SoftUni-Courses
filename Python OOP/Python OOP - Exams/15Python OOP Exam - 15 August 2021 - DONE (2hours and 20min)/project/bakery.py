from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.drink.tea import Tea
from project.drink.water import Water
from project.baked_food.cake import Cake
from project.baked_food.bread import Bread


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.drinks_menu = []
        self.food_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip() or not value:
            raise ValueError(f"Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, food_name: str, price: float):
        food = [f for f in self.food_menu if f.name == food_name]
        if food:
            raise Exception(f"{food_type} {food_name} is already in the menu!")
        if food_type == "Bread":
            new_food = Bread(food_name, price)
        if food_type == "Cake":
            new_food = Cake(food_name, price)
        self.food_menu.append(new_food)
        return f"Added {food_name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, drink_name: str, portion: float, brand: str):
        drink = [d for d in self.drinks_menu if d.name == drink_name]
        if drink:
            raise Exception(f"{drink_type} {drink_name} is already in the menu!")
        if drink_type == "Tea":
            new_drink = Tea(drink_name, portion, brand)
        if drink_type == "Water":
            new_drink = Water(drink_name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {drink_name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        tables = [t for t in self.tables_repository if t.capacity >= number_of_people and (not t.is_reserved)]
        if not tables:
            return f"No available table for {number_of_people} people"
        table = tables[0]
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        not_in_menu = []
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        for food_name in food_names:
            food = [f for f in self.food_menu if f.name == food_name]
            if not food:
                not_in_menu.append(food_name)
            else:
                food = food[0]
                table.order_food(food)
        result = [f"Table {table_number} ordered:"]
        for food in table.food_orders:
            result.append(food.__repr__())
        result.append(f"{self.name} does not have in the menu:")
        for f in not_in_menu:
            result.append(f)
        return "\n".join(result)

    def order_drink(self, table_number: int, *drink_names):
        not_in_menu = []
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        for drink_name in drink_names:
            drink = [d for d in self.drinks_menu if d.name == drink_name]
            if not drink:
                not_in_menu.append(drink_name)
            else:
                drink = drink[0]
                table.order_drink(drink)
        result = [f"Table {table_number} ordered:"]
        for drink in table.drink_orders:
            result.append(drink.__repr__())
        result.append(f"{self.name} does not have in the menu:")
        for d in not_in_menu:
            result.append(d)
        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            float_bill = float(bill)
            self.total_income += float_bill
            result = [f"Table: {table_number}"]
            result.append(f"Bill: {bill:.2f}")
            table.clear()
            return "\n".join(result)
        else:
            return f"Could not find table {table_number}"

    def get_free_tables_info(self):
        free_tables_info = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return "\n".join(info for info in free_tables_info if info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

