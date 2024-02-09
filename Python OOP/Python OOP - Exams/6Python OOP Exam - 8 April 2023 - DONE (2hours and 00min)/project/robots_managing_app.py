from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type == MainService.type_:
            new_service = MainService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        elif service_type == SecondaryService.type_:
            new_service = SecondaryService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        else:
            raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == MaleRobot.type_:
            new_robot = MaleRobot(name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."
        elif robot_type == FemaleRobot.type_:
            new_robot = FemaleRobot(name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."
        else:
            raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if (robot.type_ == FemaleRobot.type_ and service.type_ == SecondaryService.type_) or (robot.type_ == MaleRobot.type_ and service.type_ == MainService.type_):
            if len(service.robots) < service.capacity:
                service.robots.append(robot)
                self.robots.remove(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                raise Exception("Not enough capacity for this robot!")
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        removed = [r for r in service.robots if r.name == robot_name]
        if removed:
            robot = removed[0]
            self.robots.append(robot)
            service.robots.remove(robot)
            return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        if service.robots:
            fed = [r.eating() for r in service.robots]
            return f"Robots fed: {len(fed)}."
        else:
            return f"Robots fed: 0."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        if service.robots:
            total_price = sum([r.price for r in service.robots])
            return f"The value of service {service_name} is {total_price:.2f}."
        else:
            return f"The value of service {service_name} is 0.00."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])
