from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def test_constructor(self):
        player1 = TennisPlayer("Martin", 19, 100)
        self.assertEqual(player1.name, "Martin")
        self.assertEqual(player1.age, 19)
        self.assertEqual(player1.points, 100)
        self.assertEqual(player1.wins, [])
        with self.assertRaises(ValueError) as ve1:
            TennisPlayer("J", 20, 90)
        self.assertEqual(str(ve1.exception), "Name should be more than 2 symbols!")
        with self.assertRaises(ValueError) as ve2:
            TennisPlayer("Dani", 13, 30)
        self.assertEqual(str(ve2.exception), "Players must be at least 18 years of age!")
        with self.assertRaises(ValueError) as ve3:
            TennisPlayer("Fu", 21, 50)
        self.assertEqual(str(ve3.exception), "Name should be more than 2 symbols!")
        player2 = TennisPlayer("Bob", 18, -25)
        self.assertEqual(player2.name, "Bob")
        self.assertEqual(player2.age, 18)
        self.assertEqual(player2.points, -25)
        self.assertEqual(player2.wins, [])

    def test_add_new_win_case1(self):
        player1 = TennisPlayer("Martin", 19, 100)
        player1.add_new_win("Toronto")
        self.assertEqual(player1.name, "Martin")
        self.assertEqual(player1.age, 19)
        self.assertEqual(player1.points, 100)
        self.assertEqual(player1.wins, ["Toronto"])

    def test_add_new_win_case2(self):
        player1 = TennisPlayer("Martin", 19, 100)
        player1.add_new_win("Toronto")
        player1.add_new_win("Moscow")
        player1.add_new_win("Sofia")
        self.assertEqual(player1.name, "Martin")
        self.assertEqual(player1.age, 19)
        self.assertEqual(player1.points, 100)
        self.assertEqual(player1.wins, ["Toronto", "Moscow", "Sofia"])

    def test_add_new_win_case3(self):
        player1 = TennisPlayer("Martin", 19, 100)
        player1.add_new_win("Sofia")
        message = player1.add_new_win("Sofia")
        self.assertEqual(message, "Sofia has been already added to the list of wins!")

    def test_lt_method(self):
        player1 = TennisPlayer("Martin", 19, 100)
        player2 = TennisPlayer("Bob", 18, 90)
        message1 = player1.__lt__(player2)
        message2 = player2.__lt__(player1)
        self.assertEqual(message1, "Martin is a better player than Bob")
        self.assertEqual(message2, "Martin is a top seeded player and he/she is better than Bob")

    def test_str_method(self):
        player1 = TennisPlayer("Martin", 19, 100)
        player1.add_new_win("Sofia")
        player1.add_new_win("Canada")
        player1.add_new_win("Brazil")
        player2 = TennisPlayer("Bob", 18, 90)
        message1 = str(player1)
        message2 = str(player2)
        result1 = f"Tennis Player: Martin\n" \
               f"Age: 19\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: Sofia, Canada, Brazil"
        result2 = f"Tennis Player: Bob\n" \
               f"Age: 18\n" \
               f"Points: 90.0\n" \
               f"Tournaments won: "
        self.assertEqual(message2, result2)
        self.assertEqual(message1, result1)

