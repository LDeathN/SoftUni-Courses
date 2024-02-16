from project.team import Team
from unittest import TestCase


class TestTeam(TestCase):
    def test_constructor(self):
        team1 = Team("Devin")
        self.assertEqual(team1.name, "Devin")
        self.assertEqual(team1.members, {})
        with self.assertRaises(ValueError) as ve:
            Team("")
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")
        with self.assertRaises(ValueError) as ve2:
            Team("Number 1")
        self.assertEqual(str(ve2.exception), "Team Name can contain only letters!")

    def test_add_method_case1(self):
        team1 = Team("Devin")
        team2 = Team("Stars")
        message = team1.add_member(Martin=18, Dani=19, Ivan=19)
        self.assertEqual(message, "Successfully added: Martin, Dani, Ivan")
        self.assertEqual(team1.members, {"Martin": 18, "Dani": 19, "Ivan": 19})
        self.assertEqual(len(team1), 3)
        message = team1.add_member(Martin=18, Gosho=20, Dani=19)
        self.assertEqual(message, "Successfully added: Gosho")
        self.assertEqual(team1.members, {"Martin": 18, "Dani": 19, "Ivan": 19, "Gosho": 20})
        self.assertEqual(len(team1), 4)

    def test_remove_method_case2(self):
        team1 = Team("Devin")
        team1.add_member(Martin=18, Dani=19, Ivan=19)
        message = team1.remove_member("Martin")
        self.assertEqual(message, "Member Martin removed")
        self.assertEqual(team1.members, {"Dani": 19, "Ivan": 19})
        self.assertEqual(len(team1), 2)
        message2 = team1.remove_member("Peter")
        self.assertEqual(message2, "Member with name Peter does not exist")

    def test_gt_method(self):
        team1 = Team("Devin")
        team2 = Team("Stars")
        team1.add_member(Martin=18, Dani=19, Ivan=19)
        team2.add_member(Martin=18, Gosho=20, Dani=19, Ivan=19)
        self.assertEqual(team1 > team2, False)
        self.assertEqual(team2 > team1, True)

    def test_add_method(self):
        team1 = Team("Devin")
        team2 = Team("Stars")
        team5 = Team("K")
        team1.add_member(Martin=18)
        team2.add_member(Dani=19, Ivan=19)
        team3 = team1.__add__(team2)
        self.assertEqual(team3.name, "DevinStars")
        self.assertEqual(team3.members, {"Martin": 18, "Dani": 19, "Ivan": 19})
        self.assertEqual(len(team3), 3)
        team4 = team3.__add__(team2)
        self.assertEqual(team4.name, "DevinStarsStars")
        self.assertEqual(team4.members, {"Martin": 18, "Dani": 19, "Ivan": 19})
        self.assertEqual(len(team4), 3)
        team6 = team5.__add__(team2)
        self.assertEqual(team6.name, "KStars")
        self.assertEqual(team6.members, {"Dani": 19, "Ivan": 19})
        self.assertEqual(len(team6), 2)

    def test_str_method(self):
        team1 = Team("Devin")
        result = team1.__str__()
        self.assertEqual(result, "Team name: Devin")
        team1.add_member(Martin=18, Dani=19, Ivan=19)
        result = team1.__str__()
        actual = ["Team name: Devin"]
        actual.append("Member: Dani - 19-years old")
        actual.append("Member: Ivan - 19-years old")
        actual.append("Member: Martin - 18-years old")
        actual = "\n".join(actual)
        self.assertEqual(result, actual)
        team1.remove_member("Dani")
        result = team1.__str__()
        actual = ["Team name: Devin"]
        actual.append("Member: Ivan - 19-years old")
        actual.append("Member: Martin - 18-years old")
        actual = "\n".join(actual)
        self.assertEqual(result, actual)
        