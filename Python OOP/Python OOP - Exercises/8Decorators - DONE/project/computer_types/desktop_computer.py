from math import log
from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processors = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
        rams = [2, 4, 8, 16, 32, 64, 128]
        processor_price = 0

        if ram in rams:
            ram_price = log(ram, 2) * 100
        else:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if processor not in processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        else:
            for element in processors:
                if element == processor:
                    processor_price = processors[element]
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {int(self.price)}$."

