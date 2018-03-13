import random


class Machine:
    full_bonus_coeff = 3
    modulo = 2
    pool_max = 49
    number_history = []

    def process(self, money_played, number_guessed) -> int:
        print(f"Money played : {money_played}", f"Number tried : {number_guessed}", sep='\n')
        self.number_history.append(random.randint(0, self.pool_max))
        print(f"Number occurred : {self.number_history[-1]}")
        if number_guessed == self.number_history[-1]:
            return money_played * self.full_bonus_coeff
        elif number_guessed % self.modulo == self.number_history[-1] % self.modulo == 0:
            return money_played * 0.5
        return 0


class Player:

    def __init__(self, money: int):
        self.money = money
        self.machine = None

    def choose_number(self) -> int:
        raise NotImplementedError

    def choose_money(self) -> int:
        raise NotImplementedError

    def play(self):
        if not isinstance(self.machine, Machine):
            raise RuntimeError("Must assign a machine before playing")
        money_played = self.choose_money()
        assert money_played <= self.money
        self.money -= money_played
        money = self.machine.process(money_played, self.choose_number())
        print(f"Money earned {money}", f"Money remaining : {self.money}", sep='\n')
        self.money += money


class Human(Player):
    def choose_number(self) -> int:
        while True:
            try:
                number = int(input(f"Choose 0 <-> {self.machine.pool_max} \n"))
                assert 0 <= number <= self.machine.pool_max
                return number
            except (ValueError, AssertionError):
                continue

    def choose_money(self) -> int:
        while True:
            try:
                money = int(input(f"Choose money to play\n"))
                return money
            except (ValueError, RuntimeError):
                continue


def play():
    p = Human(1000)
    m = Machine()
    p.machine = m
    while p.money > 0:
        p.play()


if __name__ == '__main__':
    play()
