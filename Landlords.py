# -*- coding: utf-8 -*-
'''
Created on Nov 20, 2014

@author: ljq
'''
import random

class Landlords:
    playerGroup = list()
    round = 0
    curIdx =0  #当前回合出牌玩家索引
    curDeskCards = list()
    result = list()
    playerCards = list()
    cards = list()
    keep = list()
    def __init__(self,players):
        self.cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,\
                 10,10,10,10,'j','j','j','j','Q','Q','Q','Q','k','k','k','k','A','A','A','A','☆','★']
        self.playerGroup = players
        self.roundIdx = 0
        return
    
    def setPlayer(self):
        return
    
    def shuffle(self):
        random.shuffle (self.cards)
        return
    
    def draw(self):
        temPlayCards = list()
        temPlayCardsA = list()
        temPlayCardsB = list()
        temPlayCardsC = list()

#         j = 0
        for i in range(0,3):
            self.keep.append(self.cards.pop())
            
        for card in self.cards :
            if i % 3 == 0 :
                #temPlayCards.insert(j*3 + i, card)
                temPlayCardsA.append(card)
            elif i % 3 == 1 :
#                 temPlayCards.insert(j*3 + i, card)
                temPlayCardsB.append(card)
            elif i % 3 == 2 :
#                 temPlayCards.insert(j*3 + i, card)
                temPlayCardsC.append(card)
            i += 1
            if i == 3 : 
                i = 0
#                 j += 1
        self.playerCards = []
        temPlayCardsA.sort()
        temPlayCardsB.sort()
        temPlayCardsC.sort()
        for x in range(0,3):
            if x == 0 : 
                self.playerCards.append((self.playerGroup[x],temPlayCardsA))
            elif x == 1 :
                self.playerCards.append((self.playerGroup[x],temPlayCardsB))
            else :
                self.playerCards.append((self.playerGroup[x],temPlayCardsC))
        return
    
    def play(self,playCard,player):
        busr = False
        for p in self.playerGroup:
            if player == p: busr = True
        if not busr  :
            return -2
        if self.playOrder !=  Landlords.curIdx:
            return -1 
#         if  playCard 满足出牌条件
#             出牌
#         else    
#           重新选牌
        
        tmpPlayCards = list()
        tmpPlayCards.append(playCard)
        tmpPlayCards.sort()
        cardsType = self.getPlayCardsType(tmpPlayCards[0])
#         if Landlords.curIdx == 0:
#             playCard

#出牌结束
        Landlords.curIdx += 1
        if Landlords.curIdx > 2:
            Landlords.curIdx = 0
            Landlords.curDeskCards = []
        return
    
    def drawOrder(self):
        return
    def Grabthelandlord(self):
        
        return _player


    def getPlayCardsType(self,cards):
        cardsLen = len(cards)
        if cardsLen == 1 : cardsType = 'single'
        elif cardsLen == 2 : 
            cardsType = 'double'
            if tmpPlayCards[0] == '☆★' or tmpPlayCards[0] == '★☆' : cardsType = 'bigBomb'
        elif cardsLen == 3 : cardsType = 'treble'
        elif cardsLen == 4 : 
            cardsType = 'bomb'
        elif cardsLen == 5: cardsType = 's'
        
class Players:
    def __init__(self,name):
        self.name = name
        self.cards = list()
        self.game = ' '
        
    def playCards(self):
        return
    def joinGame(self):
        return
    def Grabthelandlord(self):
        return
    def playCards(self):
        return
    def getCards(self):
        return
        

if __name__ == "__main__":
    players = ['Xman','Spider','Superman']
    landlds = Landlords(players)
    landlds.shuffle()
    landlds.draw()
    print landlds.cards
    print landlds.playerCards