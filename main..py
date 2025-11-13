import time

from game_logic.game import *

if __name__ == "__main__":

    new_game = init_game()
    hand_p1 = new_game["player_1"]["hand"]
    hand_p2 = new_game["player_2"]["hand"]
    while hand_p1 and hand_p2:
        play = play_round(new_game["player_1"], new_game["player_2"])

    won_p1 = len(new_game["player_1"]["won_pile"])
    won_p2 = len(new_game["player_2"]["won_pile"])

    time.sleep(2)

    if won_p1 > won_p2:
        print("The big winner of the game is:")
        time.sleep(2)
        print("\U0001F941")
        time.sleep(5)
        print(new_game["player_1"]["name"])
    else:
        print("The big winner of the game is:")
        time.sleep(2)
        print("Tadam Tadam Tadam...")
        time.sleep(5)
        print(new_game["player_2"]["name"])





