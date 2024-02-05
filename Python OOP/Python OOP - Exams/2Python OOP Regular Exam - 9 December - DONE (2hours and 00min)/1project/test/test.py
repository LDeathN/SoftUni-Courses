from unittest import TestCase
from project.railway_station import RailwayStation
from collections import deque

class TestRailwayStation(TestCase):
    def test_constructor(self):
        station1 = RailwayStation("North")
        self.assertEqual(station1.name, "North")
        self.assertEqual(station1.arrival_trains, deque([]))
        self.assertEqual(station1.departure_trains, deque([]))
        with self.assertRaises(ValueError) as ve1:
            RailwayStation("D")
        self.assertEqual(str(ve1.exception), "Name should be more than 3 symbols!")
        with self.assertRaises(ValueError) as ve2:
            RailwayStation("Day")
        self.assertEqual(str(ve2.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_case1(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        self.assertEqual(station1.arrival_trains, deque(["South"]))

    def test_new_arrival_case2(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("South")
        self.assertEqual(station1.arrival_trains, deque(["South", "South", "South"]))

    def test_new_arrival_case3(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        station1.new_arrival_on_board("East")
        self.assertEqual(station1.arrival_trains, deque(["South", "West", "East"]))

    def test_train_arrived_case1(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        message = station1.train_has_arrived("South")
        self.assertEqual(message, "South is on the platform and will leave in 5 minutes.")
        self.assertEqual(station1.arrival_trains, deque(["West"]))
        self.assertEqual(station1.departure_trains, deque(["South"]))

    def test_train_arrived_case2(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        message = station1.train_has_arrived("West")
        self.assertEqual(message, "There are other trains to arrive before West.")
        self.assertEqual(station1.arrival_trains, deque(["South", "West"]))
        self.assertEqual(station1.departure_trains, deque([]))

    def test_train_arrived_case3(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        message = station1.train_has_arrived("Sofia")
        self.assertEqual(message, "There are other trains to arrive before Sofia.")
        self.assertEqual(station1.arrival_trains, deque(["South", "West"]))
        self.assertEqual(station1.departure_trains, deque([]))

    def test_train_arrived_case4(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        station1.new_arrival_on_board("East")
        station1.train_has_arrived("South")
        station1.train_has_arrived("West")
        self.assertEqual(station1.arrival_trains, deque(["East"]))
        self.assertEqual(station1.departure_trains, deque(["South", "West"]))

    def test_train_left_case1(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        station1.train_has_arrived("South")
        self.assertEqual(station1.departure_trains, deque(["South"]))
        message = station1.train_has_left("South")
        self.assertEqual(message, True)
        self.assertEqual(station1.arrival_trains, deque(["West"]))
        self.assertEqual(station1.departure_trains, deque([]))

    def test_train_left_case2(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        station1.train_has_arrived("South")
        message = station1.train_has_left("East")
        self.assertEqual(message, False)
        self.assertEqual(station1.arrival_trains, deque(["West"]))
        self.assertEqual(station1.departure_trains, deque(["South"]))

    def test_train_left_case3(self):
        station1 = RailwayStation("North")
        station1.new_arrival_on_board("South")
        station1.new_arrival_on_board("West")
        station1.new_arrival_on_board("East")
        station1.new_arrival_on_board("Sky")
        station1.train_has_arrived("South")
        station1.train_has_arrived("West")
        station1.train_has_arrived("East")
        station1.train_has_left("South")
        station1.train_has_left("West")
        self.assertEqual(station1.arrival_trains, deque(["Sky"]))
        self.assertEqual(station1.departure_trains, deque(["East"]))
        