from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [h.name for h in System._hardware]:
            return f"Hardware does not exist"
        else:
            new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            if hardware.memory >= new_software.memory_consumption and hardware.capacity >= new_software.capacity_consumption:
                hardware.install(new_software)
                System._software.append(new_software)
            else:
                raise Exception(f"Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in [h.name for h in System._hardware]:
            return f"Hardware does not exist"
        else:
            new_software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            if hardware.memory >= new_software.memory_consumption and hardware.capacity >= new_software.capacity_consumption:
                hardware.install(new_software)
                System._software.append(new_software)
            else:
                raise Exception(f"Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name in [h.name for h in System._hardware] and software_name in [s.name for s in System._software]:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return f"Some of the components do not exist"

    @staticmethod
    def analyze():
        result = [f"System Analysis"]
        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([hardware.total_memory for hardware in System._hardware])}")
        result.append(f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([hardware.total_capacity for hardware in System._hardware])}")
        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}")
            result.append(f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}")
            result.append(f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == 'Light'])}")
            result.append(f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.total_memory}")
            result.append(f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.total_capacity}")
            result.append(f"Type: {hardware.hardware_type}")
            software_components = ', '.join([s.name for s in hardware.software_components]) if hardware.software_components else "None"
            result.append(f"Software Components: {software_components}")
        return "\n".join(result)
