# -*- coding: utf-8 -*-
'''
Created on Nov 20, 2014

@author: ljq
'''
import random

class Landlords:
    playerGroup = list()
    round = 0
    result = list()
    playerCards = list()
    cards = list()
    def __init__(self,players):
        self.cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,\
                 10,10,10,10,'j','j','j','j','Q','Q','Q','Q','k','k','k','k','A','A','A','A','']
        self.playerGroup.append(players)
        return
    
    def setPlayer(self):
        return
    
    def shuffle(self):
        random.shuffle (self.cards)
        return
    
    def draw(self):
        temPlayCards = ()
        temPlayCards[0] = []
        temPlayCards[1] = []
        temPlayCards[2] = []
        i = 0
        for card in self.cards :
            if i % 3 == 0 :
                temPlayCards[0].append(card)
            elif i % 3 == 1 :
                temPlayCards[1].append(card)
            elif i % 3 == 2 :
                temPlayCards[2].append(card)
            i += 1
            if i == 3 : i =0
        for x in [0,2]:
            self.playerCards.append((self.playerGroup[x],temPlayCards[x]))  
        return
    
    def play(self):
        return
    
    def drawOrder(self):
        return
    

if __name__ == "__main__":
    players = ['Xman','Spider','Superman']
    landlds = Landlords(players)
    landlds.shuffle()
    landlds.draw()
    print landlds.cards
    print landlds.playerCards