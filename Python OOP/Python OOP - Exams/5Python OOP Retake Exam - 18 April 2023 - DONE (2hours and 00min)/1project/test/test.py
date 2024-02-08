from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def test_constructor(self):
        robot1 = Robot("0007", "Military", 10, 5000)
        robot2 = Robot("", "Education", 0, 0)
        with self.assertRaises(ValueError) as ve1:
            Robot("3332", "Mine", 100, 6000)
        with self.assertRaises(ValueError) as ve2:
            Robot("5555", "Humanoids", 100, -5000)
        self.assertEqual(robot1.robot_id, "0007")
        self.assertEqual(robot1.category, "Military")
        self.assertEqual(robot1.available_capacity, 10)
        self.assertEqual(robot1.price, 5000)
        self.assertEqual(robot1.software_updates, [])
        self.assertEqual(robot1.hardware_upgrades, [])
        self.assertEqual(robot2.robot_id, "")
        self.assertEqual(robot2.category, "Education")
        self.assertEqual(robot2.available_capacity, 0)
        self.assertEqual(robot2.price, 0)
        self.assertEqual(robot2.software_updates, [])
        self.assertEqual(robot2.hardware_upgrades, [])
        self.assertEqual(str(ve1.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")
        self.assertEqual(str(ve2.exception), "Price cannot be negative!")

    def test_upgrade_case1(self):
        robot1 = Robot("0007", "Military", 10, 5000)
        message = robot1.upgrade("VideoCard", 1000)
        self.assertEqual(message, "Robot 0007 was upgraded with VideoCard.")
        self.assertEqual(robot1.hardware_upgrades, ["VideoCard"])
        self.assertEqual(robot1.price, 6500)

    def test_upgrade_case2(self):
        robot1 = Robot("0007", "Military", 10, 5000)
        robot1.upgrade("VideoCard", 2000)
        message = robot1.upgrade("RAM", 1000)
        self.assertEqual(message, "Robot 0007 was upgraded with RAM.")
        self.assertEqual(robot1.hardware_upgrades, ["VideoCard", "RAM"])
        self.assertEqual(robot1.price, 9500)

    def test_upgrade_case3_failed(self):
        robot1 = Robot("0007", "Military", 10, 5000)
        robot1.upgrade("VideoCard", 1000)
        message = robot1.upgrade("VideoCard", 2500)
        self.assertEqual(message, "Robot 0007 was not upgraded.")
        self.assertEqual(robot1.hardware_upgrades, ["VideoCard"])
        self.assertEqual(robot1.price, 6500)

    def test_update_case1(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        message = robot1.update(1.1, 20)
        self.assertEqual(message, 'Robot 0007 was updated to version 1.1.')
        self.assertEqual(robot1.software_updates, [1.1])
        self.assertEqual(robot1.available_capacity, 80)

    def test_update_case2_same_version(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot1.update(1.1, 20)
        message = robot1.update(1.1, 20)
        self.assertEqual(message, "Robot 0007 was not updated.")
        self.assertEqual(robot1.software_updates, [1.1])
        self.assertEqual(robot1.available_capacity, 80)

    def test_update_case3_worse_version(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot1.update(2.1, 40)
        message = robot1.update(2.0, 30)
        self.assertEqual(message, "Robot 0007 was not updated.")
        self.assertEqual(robot1.software_updates, [2.1])
        self.assertEqual(robot1.available_capacity, 60)

    def test_update_case4_no_capacity(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot1.update(2.0, 40)
        message = robot1.update(2.1, 70)
        self.assertEqual(message, "Robot 0007 was not updated.")
        self.assertEqual(robot1.software_updates, [2.0])
        self.assertEqual(robot1.available_capacity, 60)

    def test_update_case5_double_update(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot1.update(2.0, 40)
        message = robot1.update(2.1, 50)
        self.assertEqual(message, 'Robot 0007 was updated to version 2.1.')
        self.assertEqual(robot1.software_updates, [2.0, 2.1])
        self.assertEqual(robot1.available_capacity, 10)

    def test1_gt_method(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot2 = Robot("0008", "Entertainment", 90, 4500)
        message = robot1.__gt__(robot2)
        self.assertEqual(message, 'Robot with ID 0007 is more expensive than Robot with ID 0008.')

    def test2_gt_method(self):
        robot1 = Robot("0007", "Military", 100, 5000)
        robot2 = Robot("0008", "Entertainment", 90, 4500)
        message = robot2.__gt__(robot1)
        self.assertEqual(message, 'Robot with ID 0008 is cheaper than Robot with ID 0007.')

    def test3_gt_method(self):
        robot1 = Robot("0007", "Military", 100, 55000)
        robot2 = Robot("0008", "Entertainment", 100, 55000)
        message1 = robot1.__gt__(robot2)
        message2 = robot2.__gt__(robot1)
        self.assertEqual(message1, 'Robot with ID 0007 costs equal to Robot with ID 0008.')
        self.assertEqual(message2, 'Robot with ID 0008 costs equal to Robot with ID 0007.')


if __name__ == '__main__':
    main()
    