import random


class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        roll_value = random.randint(1, 6)
        self._value = roll_value
        return roll_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    def is_computer(self):
        return self._computer

    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def rolling_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("============================================")
        print(" 🎲 🎲 🎲 Welcome to my Dice Game  🎲 🎲 🎲")
        print("============================================")

        while True:
            self.play_round()
            check = self.game_over()
            if check == False:
                break

    def play_round(self):
        print("-----New Round Start-----")
        input("Press any key to roll the dice. 🎲")

        player_value = self._player.rolling_die()
        computer_value = self._computer.rolling_die()

        print(f"Your Die rolled {player_value}")
        print(f"The Computers die rolled {computer_value}")

        if player_value > computer_value:
            print("You won the round")
            self.update_counters(self._player, self._computer)
        elif computer_value > player_value:
            print("The computer won the round")
            self.update_counters(self._computer, self._player)
        else:
            print("It's a tie")

        print(f"Your Counter is {self._player.counter()}")
        print(f"The Computers counter is {self._computer.counter()}")
        print("======================================")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def game_over(self):
        if self._player.counter() == 0:
            print("You Win. Letss goooo")
            return False
        elif self._computer.counter() == 0:
            print("The Computer Won. you lose")
            return False


player_die = Die()
computer_die = Die()

player1 = Player(player_die, False)
computer1 = Player(computer_die, True)

game = DiceGame(player1, computer1)

game.play()
