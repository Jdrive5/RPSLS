from player import Player
from time import sleep
from gesture import Gesture

class Human(Player):
    def __init__(self):
        sleep(1)
        self.name = input("What is your name?")
        sleep(1)
        print(f"Welcome {self.name}!")
        sleep(1)
        super().__init__()
        self.wins = 0

    def display_gestures(self):
        counter = 0
        print(f'{self.name}, choose between these options: ')
        for gesture in self.gestures:
            print(f'Choose {str(counter)} for {gesture}')
            sleep(1)
            counter += 1


    def gesture_update(self):
        self.display_gestures()
        self.gesture = Gesture()
        self.choice_of_gesture = self.gesture.pick_gesture()