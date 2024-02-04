class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTests(unittest.TestCase):
    def test_initialize_worker(self):
        worker = Worker("John", 1000, 10)
        self.assertEqual(worker.name, "John")
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)

    def test_increment_energy_after_rest(self):
        worker = Worker("Alice", 1200, 5)
        worker.rest()
        self.assertEqual(worker.energy, 6)

    def test_error_raised_when_working_with_zero_or_negative_energy(self):
        worker = Worker("Bob", 800, 0)

        with self.assertRaises(Exception) as context:
            worker.work()

        expected_message = "Not enough energy."
        self.assertEqual(str(context.exception), expected_message)

    def test_increase_money_after_work(self):
        worker = Worker("Eve", 1500, 8)
        worker.work()
        self.assertEqual(worker.money, 1500)

    def test_decrease_energy_after_work(self):
        worker = Worker("Charlie", 900, 12)
        worker.work()
        self.assertEqual(worker.energy, 11)

    def test_get_info_returns_proper_string(self):
        worker = Worker("Diana", 1100, 7)
        info_str = worker.get_info()
        self.assertEqual(info_str, "Diana has saved 0 money.")


if __name__ == '__main__':
    unittest.main()

