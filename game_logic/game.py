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
    dec = shuffle(dec)
    len_dec = len(dec)
    for i in range(len_dec):
        if i < len_dec/2:
            p1["hand"].append(dec[i])
        else:
            p2["hand"].append(dec[i])
    game_dict = {"deck":dec, "player_1":p1, "player_2":p2}
    return game_dict


def play_round(p1:dict, p2:dict):
    rescuer = rescuer_cards(p1, p2)
    result = compare_cards(rescuer[0], rescuer[1])
    if result == "p1":
        players = add_to_won_pile(p1, p2)
        print(f"There are {rescuer[0]["rank"]} {rescuer[0]["suite"]} of {p1["name"]} and {rescuer[1]["rank"]} {rescuer[1]["suite"]} of {p2["name"]}")
        print(f"The winner is {p1["name"]}")
        return players
    elif result == "p2":
        players = add_to_won_pile(p2, p1)
        print(f"There are {rescuer[0]["rank"]} {rescuer[0]["suite"]} of {p1["name"]} and {rescuer[1]["rank"]} {rescuer[1]["suite"]} of {p2["name"]}")
        print(f"The winner is {p2["name"]}")
        return players
    else:
        print(f"There are {rescuer[0]["rank"]} {rescuer[0]["suite"]} of {p1["name"]} and {rescuer[1]["rank"]} {rescuer[1]["suite"]} of {p2["name"]}")
        print("round again")
        players = (p1, p2)
        return players

def add_to_won_pile(winner, loser):
    temp1 = winner["hand"].pop(0)
    temp2 = loser["hand"].pop(0)
    winner["won_pile"].append(temp1)
    winner["won_pile"].append(temp2)
    if winner["name"] == "Ai":
        return loser, winner
    else:
        return winner, loser

def rescuer_cards(p1, p2):
    p1_card = p1["hand"][0]
    p2_card = p2["hand"][0]
    return p1_card, p2_card

def updates_results(game_now, players):
    game_now["player_1"]["hand"] = players[0]["hand"]
    game_now["player_1"]["won_pile"] = players[0]["won_pile"]
    game_now["player_2"]["hand"] = players[1]["hand"]
    game_now["player_2"]["won_pile"] = players[1]["won_pile"]
    return game_now


