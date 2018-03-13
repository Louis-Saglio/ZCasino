from unittest import TestCase

from zcasino import Machine, Player


class TestMachine(TestCase):
    
    def setUp(self):
        self.machine = Machine()

    def test_process_lost(self):
        self.machine.get_number = lambda: 2 
        money = self.machine.process(10, 5)
        self.assertEqual(0, money)
    
    def test_full_win(self):
        self.machine.get_number = lambda: 2
        money = self.machine.process(10, 2)
        self.assertEqual(30, money)

    def test_semi_win(self):
        self.machine.get_number = lambda: 2
        money = self.machine.process(10, 4)
        self.assertEqual(5, money)

    def test_get_number(self):
        number = self.machine.get_number()
        self.assertIn(number, range(self.machine.max))
        self.assertEqual(self.machine.nbr_history[-1], number)


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player(100)

    def test_pay_success(self):
        self.player.pay(42)
        self.assertEqual(58, self.player.money)

    def test_pay_fail(self):
        self.assertRaises(
            RuntimeError,
            lambda: self.player.pay(101)
        )

    def test_play(self):
        self.player.machine = Machine()
        self.player.machine.max = 0
        self.player.choose_number = lambda: 5
        self.player.choose_money = lambda: 42
        self.player.play()
        self.assertEqual(58, self.player.money)
