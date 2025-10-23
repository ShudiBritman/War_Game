import random


def create_card(rank:str, suite:str):
    values_list_nums = {
                   "2":2,
                   "3":3,
                   "4":4,
                   "5":5,
                   "6":6,
                   "7":7,
                   "8":8,
                   "9":9,
                   "10":10,
                   "J":11,
                   "Q":12,
                   "K":13,
                   "A":14
                        }
    card = {}
    if suite in values_list:
        card["rank"] = rank
        card["suite"] = suite
        card["value"] = values_list[rank]
    return card
def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "War"
def create_deck():
    list_suite = ["H", "C", "D", "S"]
    dict_rank = {  "J":11,
                   "Q":12,
                   "K":13,
                   "A":14
                   }
    pack_of_cards = []
    for i in range(len(list_suite)):
        for j in range(2, 11):
            card = {}
            card["rank"] = str(j)
            card["suite"] = list_suite[i]
            card["value"] = j
            pack_of_cards.append(card)
        for k, v in dict_rank.items():
            card = {}
            card["rank"] = k
            card["suite"] = list_suite[i]
            card["value"] = v
            pack_of_cards.append(card)
    return pack_of_cards

def shuffle(deck:list[dict]):
    for i in range(1000):
        i1 = random.randint(1, 52)
        i2 = random.randint(1, 52)
        print(i2)
        print(i1)
        deck = swap(deck, deck[i1], deck[i2])
    return deck

def swap(list, i1, i2):
    temp = i1
    list[i1] = list[i2]
    list[i2] = list[temp]
    return list
pack = create_deck()
pack = shuffle(pack)
