from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    type_ = "PassengerCar"
    max_mileage = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.max_mileage)

    def drive(self, mileage: float):
        self.battery_level -= round(mileage / self.max_mileage * 100)
