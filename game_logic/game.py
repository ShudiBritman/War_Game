
def create_player(name=None):
    if name is None:
        name = "AI"
    hand = []
    won_pile = []
    player_card = {}
    player_card["name"] = name
    player_card["hand"] = hand
    player_card["won pile"] = won_pile
    return player_card
def init_game():
    p1 = create_player("Eli")
    p2 = create_player()
    dec = creat_deck()
    dec = shuffle(dec)
    p1["name"] = []
    p2["name"] = []
    len_dec = len(dec)
    for i in range(len_dec):
        if i < len_dec/2:
            p1["name"].append(dec[i])
        else:
            p2["name"].append(dec[i])
    game_dict = {"deck":dec, "player_1":p1, "player2":p2}
    return game_dict
def play_round(p1:dict, p2:dict):
    p1_card = p1["hand"][i]
    p2_card = p2["hand"][i]
    result = compare_cards(p1_card, p2_card2)
    if result == "p1":
        temp = p2["hand"].pop(0)
        p1["hand"].append(temp)
    elif result == "p2":
        temp = p1["hand"].pop(0)
        p2["hand"].append(temp)
    else:
        print("round again")
    return p1, p2
