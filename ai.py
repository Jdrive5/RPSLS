from player import Player
import random 
from time import sleep


class AI(Player):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = 'AI'
        self.wins = 0
    
    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")

    def gesture_update(self, gesture):
        pass