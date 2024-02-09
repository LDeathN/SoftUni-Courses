from project.services.base_service import BaseService


class MainService(BaseService):
    type_ = "MainService"
    Capacity = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.Capacity)

    def details(self):
        result = [f"{self.name} Main Service:"]
        if self.robots:
            robot = ' '.join([r.name for r in self.robots])
            result.append(f"Robots: {robot}")
        else:
            result.append(f"Robots: none")
        return '\n'.join(result)
