import random


def create_card(rank:str, suite:str):
    values_list_nums = {"J": 11, "Q": 12, "K": 13, "A": 14}
    for i in range(1, 11):
        values_list_nums[str(i)] = i
    card = {}
    if rank in values_list_nums:
        card["rank"] = rank
        card["suite"] = suite
        card["value"] = values_list_nums[rank]
    return card
def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "War"
def create_deck():
    list_suites = ["Heart", "Club", "Dimond", "Spade"]
    list_rank = ["J", "Q", "K", "A"]
    pack_of_cards = []
    for i in range(len(list_suites)):
        for j in range(2, 11):
            card = create_card(str(j), list_suites[i])
            pack_of_cards.append(card)
        for j in list_rank:
            card = create_card(list_rank[i], list_suites[i])
            pack_of_cards.append(card)
    return pack_of_cards

def shuffle(deck:list[dict]):
    for i in range(1000):
        i1 = random.randint(0, 51)
        i2 = random.randint(0, 51)
        deck = swap(deck, i1, i2)
    return deck

def swap(list, i1, i2):
    list[i1], list[i2] = list[i2], list[i1]
    return list

