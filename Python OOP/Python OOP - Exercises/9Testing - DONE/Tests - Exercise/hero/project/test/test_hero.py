from hero.project.hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def test_constructor(self):
        hero = Hero("Me", 9, 100.00, 25.00)
        self.assertEqual(type(hero.username), str)
        self.assertEqual(type(hero.level), int)
        self.assertEqual(type(hero.health), float)
        self.assertEqual(type(hero.damage), float)
        self.assertEqual(hero.username, "Me")
        self.assertEqual(hero.level, 9)
        self.assertEqual(hero.health, 100.00)
        self.assertEqual(hero.damage, 25.00)

    def test_battle_case1(self):
        hero1 = Hero("Me", 9, 100.00, 25.00)
        hero2 = Hero("Me", 9, 100.00, 25.00)
        with self.assertRaises(Exception) as context:
            hero1.battle(hero2)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_case2(self):
        hero1 = Hero("Me", 9, 0, 25.00)
        hero2 = Hero("You", 9, 100.00, 25.00)
        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_case3(self):
        hero1 = Hero("Me", 9, 100.00, 25.00)
        hero2 = Hero("Him", 9, 0, 25.00)
        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)
        self.assertEqual(str(context.exception), "You cannot fight Him. He needs to rest")

    def test_battle_case4(self):
        hero1 = Hero("Me", 15, 100.00, 10.00)
        hero2 = Hero("Him", 13, 100.00, 10.00)
        result = hero1.battle(hero2)
        self.assertEqual(result, "Draw")

    def test_battle_case5(self):
        hero1 = Hero("Me", 15, 100.00, 10.00)
        hero2 = Hero("Him", 13, 100.00, 5.00)
        result = hero1.battle(hero2)
        self.assertEqual(result, "You win")
        self.assertEqual(hero1.level, 16)
        self.assertEqual(hero1.damage, 15.00)
        self.assertEqual(hero1.health, 40.00)

    def test_battle_case6(self):
        hero1 = Hero("Me", 15, 100.00, 5.00)
        hero2 = Hero("Him", 10, 100.00, 10.00)
        result = hero1.battle(hero2)
        self.assertEqual(result, "You lose")
        self.assertEqual(hero2.level, 11)
        self.assertEqual(hero2.damage, 15.00)
        self.assertEqual(hero2.health, 30.00)

    def test_str_method(self):
        hero1 = Hero("Me", 15, 100.00, 5.00)
        hero2 = Hero("Him", 10, 100.00, 10.00)
        result1 = hero1.__str__()
        result2 = hero2.__str__()
        self.assertEqual(result1, "Hero Me: 15 lvl\n"
                "Health: 100.0\n"
                "Damage: 5.0\n")
        self.assertEqual(result2, "Hero Him: 10 lvl\n"
                "Health: 100.0\n"
                "Damage: 10.0\n")


if __name__ == '__main__':
    unittest.main()


