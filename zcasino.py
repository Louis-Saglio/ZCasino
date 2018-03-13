import random


class Machine:

    def __init__(self):
        self.nbr_history = []
        self.max = 49
        self.full_win_coeff = 3.0
        self.semi_win_coeff = 0.5

    def get_number(self) -> int:
        number = random.randint(0, self.max)
        self.nbr_history.append(number)
        return number

    def process(self, money: float, played_nbr: int):
        number = self.get_number()
        if number == played_nbr:
            earned_money = money * self.full_win_coeff
        elif number % 2 == played_nbr % 2:
            earned_money = money * self.semi_win_coeff
        else:
            earned_money = 0.0
        earned_money = round(earned_money, 2)
        print(
            '-' * 30,
            f"Tested number : {played_nbr}",
            f"Occurred number : {number}",
            f"Played money : {money}",
            f"Earned money : {earned_money}",
            sep="\n"
        )
        return earned_money


class Player:

    def __init__(self, money: int=1000):
        self.money = money
        self.machine: Machine = None

    def choose_number(self) -> int:
        raise NotImplementedError

    def choose_money(self) -> float:
        raise NotImplementedError

    def pay(self, money: float):
        if money > self.money:
            raise RuntimeError
        self.money -= money

    def play(self):
        played_money = self.choose_money()
        self.pay(played_money)
        choosen_number = self.choose_number()
        self.money += self.machine.process(played_money, choosen_number)
