from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type == PassengerCar.type_:
            for vehicle in self.vehicles:
                if vehicle.license_plate_number == license_plate_number:
                    return f"{license_plate_number} belongs to another vehicle."
            new_vehicle = PassengerCar(brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
        elif vehicle_type == CargoVan.type_:
            for vehicle in self.vehicles:
                if vehicle.license_plate_number == license_plate_number:
                    return f"{license_plate_number} belongs to another vehicle."
            new_vehicle = CargoVan(brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
        else:
            return f"Vehicle type {vehicle_type} is inaccessible."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
        idx = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id=idx)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        users = [user for user in self.users if user.driving_license_number == driving_license_number]
        user = users[0] if users else None
        vehicles = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number]
        vehicle = vehicles[0] if vehicles else None
        routes = [route for route in self.routes if route.route_id == route_id]
        route = routes[0] if routes else None

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        if vehicle.is_damaged:
            return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: Damaged"
        else:
            return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: OK"

    def repair_vehicles(self, count: int):
        repaired = 0
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]
        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
            repaired += 1
        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda user: -user.rating)
        result = []
        result.append("*** E-Drive-Rent ***")
        for user in users:
            result.append(str(user))
        return "\n".join(result)
