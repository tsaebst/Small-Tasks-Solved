import random


class Round:
    result = (5000)

    def __init__(self, my_bet=1, guess=True, round_list=result):
        money = round_list
        self.money = money
        self.my_bet = my_bet
        self.guess = guess

    def bet(self):
        while self.money[0] != 0:
            bet = int(input(f"You  have {self.money}. How many do you want to bet?(1-{self.money}/or: QUIT = 1):"))
            if bet == 1:
                print(f"Thank you for the game! Your final balance is: {self.money}")
                self.my_bet = 0
                return self.my_bet
            if bet > self.money:
                continue
            self.my_bet = bet
            return self.my_bet

    def random_val(self):
        while self.money[0] != 0:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            compare = dice2 == dice1
            ask = input("Do you think the value is going to be?(odd/even):").lower()
            if ask.startswith("e"):
                if ask == compare:
                    print("You`re right!")
                    self.guess = True
                    return self.guess
                print("No way!:(")
                self.guess = False
                return self.guess
            if ask.startswith("o"):
                if ask != compare:
                    print("You`re right!")
                    return self.guess
                print("No way!:(")
                self.guess = False
                return self.guess

    def refund(self):
        while self.money[0] != 0:
            fee = self.my_bet / 10
            if self.guess == True:
                self.money += self.my_bet
                print(f"You won! You take {self.my_bet} mon. The house collects a {fee} mon fee.")
            else:
                if self.my_bet == self.money:
                    print(f"You lose! You give {self.my_bet} mon. The end of the game!")
                    self.round_list.append("0")
                self.money -= self.my_bet
                print(f"You lose! You give {self.my_bet} mon. The house collects a {fee} mon fee.")
            percent = self.money - (fee)
            self.money = percent
            money = self.money
            print(f"You`re balance is : {self.money}")
            self.round_list.append(str(self.money))
            return


while True:
    play = Round()
    play.bet()
    play.random_val()
    play.refund()
