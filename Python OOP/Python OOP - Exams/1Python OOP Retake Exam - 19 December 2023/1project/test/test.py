from project.climbing_robot import ClimbingRobot
from unittest import TestCase


class TestClimbingRobot(TestCase):
    def test_constructor(self):
        robot = ClimbingRobot("Indoor", "Software", 300, 200)
        self.assertEqual(robot.category, "Indoor")
        self.assertEqual(robot.part_type, "Software")
        self.assertEqual(robot.memory, 200)
        self.assertEqual(robot.capacity, 300)
        self.assertEqual(robot.installed_software, [])
        self.assertEqual(ClimbingRobot.ALLOWED_CATEGORIES, ['Mountain', 'Alpine', 'Indoor', 'Bouldering'])
        with self.assertRaises(ValueError) as ve:
            ClimbingRobot("Mine", "Arm", 300, 300)
        self.assertEqual(str(ve.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_install_software_case1(self):
        robot = ClimbingRobot("Indoor", "Software", 300, 200)
        self.assertEqual(robot.get_used_capacity(), 0)
        self.assertEqual(robot.get_used_memory(), 0)
        self.assertEqual(robot.get_available_capacity(), 300)
        self.assertEqual(robot.get_available_memory(), 200)
        message = robot.install_software({"name": "Version", "capacity_consumption": 100, "memory_consumption": 100})
        self.assertEqual(message, f"Software 'Version' successfully installed on Indoor part.")
        self.assertEqual(robot.installed_software, [{"name": "Version", "capacity_consumption": 100, "memory_consumption": 100}])
        robot.install_software({"name": "Version 2.0", "capacity_consumption": 100, "memory_consumption": 50})
        self.assertEqual(robot.installed_software, [{"name": "Version", "capacity_consumption": 100, "memory_consumption": 100}, {"name": "Version 2.0", "capacity_consumption": 100, "memory_consumption": 50}])
        message2 = robot.install_software({"name": "Version 3.0", "capacity_consumption": 100, "memory_consumption": 100})
        self.assertEqual(message2, f"Software 'Version 3.0' cannot be installed on Indoor part.")
        message3 = robot.install_software({"name": "Version 3.0", "capacity_consumption": 150, "memory_consumption": 50})
        self.assertEqual(message3, f"Software 'Version 3.0' cannot be installed on Indoor part.")
        robot.install_software({"name": "Version 3.0", "capacity_consumption": 100, "memory_consumption": 50})
        self.assertEqual(robot.installed_software, [{"name": "Version", "capacity_consumption": 100, "memory_consumption": 100}, {"name": "Version 2.0", "capacity_consumption": 100, "memory_consumption": 50}, {"name": "Version 3.0", "capacity_consumption": 100, "memory_consumption": 50}])
        self.assertEqual(robot.get_used_capacity(), 300)
        self.assertEqual(robot.get_used_memory(), 200)
        self.assertEqual(robot.get_available_capacity(), 0)
        self.assertEqual(robot.get_available_memory(), 0)

