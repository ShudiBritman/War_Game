from utils.deck import *

def create_player(name=None):
    if name is None:
        name = "AI"
    hand = []
    won_pile = []
    card_player = {}
    card_player["name"] = name
    card_player["hand"] = hand
    card_player["won_pile"] = won_pile

    return card_player


def init_game():
    p1 = create_player("Renana")
    p2 = create_player()
    dec = create_deck()
    dec = shuffle(dec, len(dec))
    len_dec = len(dec)
    hand_p1 = dec[:len_dec//2]
    hand_p2 = dec[len_dec//2:]
    p1["hand"] += hand_p1
    p2["hand"] += hand_p2
    game_dict = {"deck":dec, "player_1":p1, "player_2":p2}

    return game_dict


def play_round(p1:dict, p2:dict):
    rescuer = rescuer_cards(p1, p2)
    result = compare_cards(rescuer[0], rescuer[1])
    if result == "p1":
        players = add_to_won_pile(p1, p2)
        print_msg(p1, p2, rescuer)

        return players

    elif result == "p2":
        players = add_to_won_pile(p2, p1)
        print_msg(p2, p1, rescuer)

        return players

    else:
        print_msg(p1, p2, rescuer)

        p1 = shuffle(p1["hand"], len(p1["hand"]))
        p2 = shuffle(p2["hand"], len(p2["hand"]))

        return p1, p2


def add_to_won_pile(winner, loser):
    if winner["hand"][0] != loser["hand"][0]:
        temp1 = winner["hand"].pop(0)
        temp2 = loser["hand"].pop(0)
        winner["won_pile"].append(temp1)
        winner["won_pile"].append(temp2)
    if winner["name"] == "Ai":
        return loser, winner    #P1 will always be returned first
    else:
        return winner, loser


def rescuer_cards(p1, p2):
    p1_card = p1["hand"][0]
    p2_card = p2["hand"][0]

    return p1_card, p2_card


def print_msg(winner, loser, cards):
    print(f"There is {cards[0]["rank"]} {cards[0]["suite"]} of {winner["name"]}")
    print(f"There is {cards[1]["rank"]} {cards[1]["suite"]} of {loser["name"]}")

    if cards[0]["value"] != cards[1]["value"]:
        print(f"The winner is {winner["name"]}")

    else:
        print("round again")




