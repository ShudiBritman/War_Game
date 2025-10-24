from game_logic.game import *

if __name__ == "__main__":

    new_game = init_game()
    hand_p1 = new_game["player_1"]["hand"]
    hand_p2 = new_game["player_2"]["hand"]
    while hand_p1 and hand_p2:
        play = play_round(new_game["player_1"], new_game["player_2"])





