from time import sleep
from player import Player
from human import Human
from ai import AI



class Game:
    def __init__(self):
        self.player_one = Player
        self.player_two = Player
        self.type_of_game = ''


    def run_game(self):
        self.display_welcome()
        self.choose_game_type()
        self.start_game()
        self.declare_winner()


    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        sleep(2)
        print("Each match will be best of 3.")
        sleep(2)


    def choose_game_type(self):
        user_choice = input("Press 1 for single player or 2 for multiplayer: ")
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()


    def start_game(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.gesture_update()
            self.player_two.gesture_update(self.player_one.get_gesture())
            if self.player_one.gesture_update == self.player_two.gesture_update:
                print(f"It's a tie! Choose again.")
                sleep(2)
            elif self.player_one.gesture_update == "Rock":
                if self.player_two.gesture_update == "Paper":
                    print(f"Paper covers rock, {self.player_two.name} wins!")
                    self.player_two.wins += 1
                    sleep(2)
                elif self.player_two.gesture_update == "Scissors":
                    print(f"Rock crushes scissors, you win!")
                    self.player_one.wins +=1
                    sleep(2)
                elif self.player_two.gesture_update == "Lizard":
                    print(f"Rock crushes Lizard, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Spock":
                    print(f"Spock vaporizes rock, {self.player_two.name} wins!")
                    sleep(2)
                else:
                    print("Try again")
                    sleep(2)
            elif self.player_one.gesture_update == "Paper":
                if self.player_two.gesture_update == "Rock":
                    print(f"Paper covers rock, you win!")
                    self.player_one.wins += 1
                    sleep(2)
                elif self.player_two.gesture_update == "Scissors":
                    print(f"Scissors cut paper, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Lizard":
                    print(f"Lizard eats paper, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Spock":
                    print(f"Paper disproves spock, you win!")
                    sleep(2)
                else:
                    print("Try again")
                    sleep(2)
            elif self.player_one.gesture_update == "Scissors":
                if self.player_two.gesture_update == "Rock":
                    print(f"Rock smashes scissors, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Paper":
                    print(f"Scissors cut paper, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Lizard":
                    print(f"Scissors decapitates lizard, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Spock":
                    print(f"Spock smashes scissors, {self.player_two.name} wins!")
                    sleep(2)
                else:
                    print("Try again")
                    sleep(2)
            elif self.player_one.gesture_update == "Lizard":
                if self.player_two.gesture_update == "Rock":
                    print(f"Rock crushes lizard, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Paper":
                    print(f"Lizard eats paper, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Scissors":
                    print(f"Scissors decapitates lizard, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Spock":
                    print(f"Lizard poisons spock, you win!")
                    sleep(2)
                else:
                    print("Try again")
                    sleep(2)
            elif self.player_one.gesture_update == "Spock":
                if self.player_two.gesture_update == "Rock":
                    print(f"Spock vaporizes rock, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Paper":
                    print(f"Paper disproves spock, {self.player_two.name} wins!")
                    sleep(2)
                elif self.player_two.gesture_update == "Scissors":
                    print(f"Spock smashes scissors, you win!")
                    sleep(2)
                elif self.player_two.gesture_update == "Lizard":
                    print(f"Lizard poisons spock, {self.player_two.name} wins!")
                    sleep(2)
                else:
                    print("Try again")
                    sleep(2)


    def declare_winner(self):
        if self.player_one.wins == 2:
            print(f"You win 2 out of 3 you are the winner!")
            sleep(2)
        elif self.player_two.wins == 2:
            print(f"{self.player_two.name} wins 2 out of 3 and is the winner!")
            sleep(2)



               
