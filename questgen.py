from redeal import *
import json

# one_nt_btu = balanced
#shape = Shape("5") + Shape("(53)(32)")
#predeal = {"N": SmartStack(balanced, Evaluator(4, 3, 2, 1), range(12, 21))}

#dealer = Deal.prepare(predeal)
dealer = Deal.prepare()
def restrictor(deal):
    n = (deal.north.hcp >= 12 and deal.north.hcp <= 21) and len(deal.north.hearts) >= 5
    s = deal.south.hcp >= 6 and deal.south.hcp <= 11
    return n and s

result = []
auction = []

jsonFile = open('out.json', 'w')
while True:
    #deal = dealer(restrictor)
    deal = dealer()
    hand = deal.north
    print(hand, "HCP", hand.hcp)
    command = input(">>")
    if command == "s":
        continue
    elif command == "q":
        break
    else:
        new_result = {"spades": str(hand.spades), "hearts": str(hand.hearts), "diamonds": str(hand.diamonds), "clubs": str(hand.clubs), "auction": auction, "correct": command, "answers": {}}
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