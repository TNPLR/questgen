from redeal import *
import json
import handtype.minor_opening
import handtype.questutil

def questgen(restrictor):
    dealer = Deal.prepare()
    result = []
    auction = [
        {"name": "1S", "explanation": "", "alert": False},
        {"name": "P", "explanation": "", "alert": False},
        {"name": "2NT", "explanation": "Jacoby 2NT", "alert": False}
    ]
    board_num = 1
    jsonFile = open('out.json', 'w')
    while True:
        deal = dealer(restrictor)
        hand = deal.north
        print(hand, "HCP", hand.hcp)
        command = input(">>")
        if command == "s":
            continue
        elif command == "q":
            break
        else:
            new_result = {"spades": str(hand.spades), "hearts": str(hand.hearts), "diamonds": str(hand.diamonds), "clubs": str(hand.clubs), "auction": auction, "correct": command, "answers": {}, "board_num": board_num}
            while True:
                command = input("---->")
                if command == 'n':
                    break
                else:
                    new_result["answers"][command] = input("---!>")
            result.append(new_result)
            print(new_result)
            #result += new_result
    json.dump(result, jsonFile, indent=2, ensure_ascii=False)

def restrictor(deal):
    if len(deal.south.spades) < 4:
        return False
    if len(deal.north.spades) < 5:
        return False
    if deal.north.hcp <= 11:
        return False
    if deal.south.hcp <= 11:
        return False
    return True
questgen(restrictor)