# Design of Computer Programs - Peter Norvig

## Poker function

def poker(hands):
    '''
    Returns the best hand : poker([hands,.....]) => hand.
    '''
    return allmax(hands, key = hand_rank)
    
    
def allmax(iterable, key = None):
    '''
    Returns a list of all items equal to max of iterable.
    '''
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    
    return result
    
    
    
def hand_rank(hand):
    '''
    Return a value indicating the ranking of the hand.
    '''
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, max(ranks), ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)
    
    
def card_ranks(cards):
    '''
    Returns a list of ranks sorted in order of Higher to Lower.
    
    ##ranks = [r for r,s in cards]   # We are using r and s to iterate over cards because cards contain number and suit.
    ##ranks.sort(reverse = True)     # It won't give the expected answer when cards like ten and jack will be there.
                                    # So we need to fix this bug.
    
    ##return ranks
    
    def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks
    '''
    
    ranks = []
    for i,j in cards:
        if i == 'T':
            ranks.append(10)
        elif i == 'J':
            ranks.append(11)
        elif i == 'Q':
            ranks.append(12)
        elif i == 'K':
            ranks.append(13)
        elif i == 'A':
            ranks.append(14)
        else:
            ranks.append(int(i))
    ranks.sort(reverse=True)
    
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks
    
    
    
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [j for i,j in hand]
    
    return len(set(suits)) == 1    
    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
   
    for i in ranks:
        if ranks.count(i) == n : return i
    return None        
    
    
def two_pair(ranks):
    """
    If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.
    """
    
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair != low_pair: return (pair, low_pair)
    else: return None
    
    
    
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    
print test()    
    
    
    
# Dealing Cards for the Game.

import random 

# This builds a deck of 52 cards. 

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    
    
    
