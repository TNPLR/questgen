import handtype.questutil
import redeal
def no5major(deal):
    return len(deal.north.spades) < 5 and len(deal.north.hearts) < 5
def notNTopener(deal):
    return not (redeal.balanced(deal.north) and (handtype.questutil.north_hcp(deal, 15, 17) or handtype.questutil.north_hcp(deal, 20, 21)))
def restrictor(deal):
    return handtype.questutil.north_hcp(deal, 12, 21) and no5major(deal) and notNTopener(deal)
