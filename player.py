class Player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = ""
        self.score = 0
        self.chosen_gesture =""


    def choose_gesture(self):
        pass

    def gesture_update(self, gesture):
        self.chosen_gesture = gesture