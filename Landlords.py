# -*- coding: utf-8 -*-
'''
Created on Nov 20, 2014

@author: ljq
'''
import random
from __builtin__ import True

class Landlords:
    playerGroup = list()
    round = -1              #当前回合
    roundBeginSeat =0       #首位出牌玩家的座次
    curPlayCount = 0        #本回合出牌次数
    curDeskCards = list()   #本回合已出的牌
    result = list()         #得分
    cards = list()          
    keep = list()           #地主牌
    curCardsType = ""       
    def setPlayerGroup(self,pGroup):
        Landlords.playerGroup = pGroup
    def __init__(self,players):
        self.cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,\
                 10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,16]
#         self.playerGroup.append(players)
        self.setPlayerGroup(players)
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
        temPlayCardsA.sort()
        temPlayCardsB.sort()
        temPlayCardsC.sort()
        for x in range(0,len(Landlords.playerGroup)):
            if x == 0 :
                Landlords.playerGroup[0].setCards(temPlayCardsA) 
#                 Landlords.playerGroup[0].append((Landlords.playerGroup[x],temPlayCardsA))
                
            elif x == 1 :
                Landlords.playerGroup[1].setCards(temPlayCardsB)
#                 Landlords.playerGroup[1].append((Landlords.playerGroup[x],temPlayCardsB))
            else :
                Landlords.playerGroup[2].setCards(temPlayCardsC)
#                 Landlords.playerGroup[2].append((Landlords.playerGroup[x],temPlayCardsC))
        return
    def compareCards(self,cardsA,cardsTypeA,cardsB,cardsTypeB):
        #B>A return true ,否则 return false
        if cardsTypeA == 'rocket':     
            return False
        elif cardsTypeB == 'rocket':
            Landlords.curCardsType = cardsTypeB
            return True
        elif cardsTypeA != cardsTypeB and cardsTypeB != 'bomb' :
            return False
        elif cardsTypeA != cardsTypeB and cardsTypeB == 'bomb':
            Landlords.curCardsType = cardsTypeB
            return True
        elif cardsTypeA == cardsTypeB:
            if  cardsTypeA  == 'single':
                if cardsB > cardsA:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'double':
                if cardsB[0] > cardsA[0]:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'threble':
                if cardsB[0] > cardsA[0]:
                    return True
                else:
                    return False                    
            elif cardsTypeA  == 'threbleOne':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                doubleNumA = 0
                threbleNumA = 0
                doubleNumB = 0
                threbleNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 1 :
                        singleNumA = itemA[0]
                    elif itemA[1] == 3 :
                        threbleNumA == itemA[0]
                              
                for itemB in samelistB:
                    if itemB[1] == 1 :
                        singleNumB = itemB[0]
                    elif itemA[1] == 3 :
                        threbleNumB == itemB[0]
                if threbleNumB > threbleNumA:
                    return True
                elif threbleNumB == threbleNumA:
                    if singleNumB > singleNumA:
                        return True
                    else:
                        return False
                else:
                    return False
            elif cardsTypeA  == 'threbleTwo':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                doubleNumA = 0
                threbleNumA = 0
                doubleNumB = 0
                threbleNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 2 :
                        doubleNumA = itemA[0]
                    elif itemA[1] == 3 :
                        threbleNumA == itemA[0]
                
                for itemB in samelistB:
                    if itemB[1] == 2 :
                        doubleNumB = itemB[0]
                    elif itemA[1] == 3 :
                        threbleNumB == itemB[0]
                if threbleNumB > threbleNumA:
                    return True
                elif threbleNumB == threbleNumA:
                    if doubleNumB > doubleNumA:
                        return True
                    else:
                        return False
                else:
                    return False    
            elif cardsTypeA  == 'seqSingle':
                if len(cardsA)== len(cardsB) and cardsB[0] > cardsA[0]:
                    return True
                else:    
                    return False
                
            elif cardsTypeA  == 'seqDouble':
                if len(cardsA)== len(cardsB) and cardsB[0] > cardsA[0]:
                    return True
                else:    
                    return False
                return
            elif cardsTypeA  == 'flySingle':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                threbleNumA = 0
                threbleNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 3 :
                        threbleNumA == itemA[0]
                        break
                for itemB in samelistB:
                    if itemA[1] == 3 :
                        threbleNumB == itemB[0]
                        break
                if threbleNumB > threbleNumA:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'flyDouble':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                threbleNumA = 0
                threbleNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 3 :
                        threbleNumA == itemA[0]
                        break
                for itemB in samelistB:
                    if itemA[1] == 3 :
                        threbleNumB == itemB[0]
                        break
                if threbleNumB > threbleNumA:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'fourTwoSingle':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                fourNumA = 0
                fourNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 4 :
                        fourNumA == itemA[0]
                        break
                for itemB in samelistB:
                    if itemA[1] == 4 :
                        fourNumB == itemB[0]
                        break
                if fourNumB > fourNumA:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'fourTwoDouble':
                samelistA = self.countSameCards(cardsA)
                samelistB = self.countSameCards(cardsB)
                fourNumA = 0
                fourNumB = 0 
                for itemA in samelistA:
                    if itemA[1] == 4 :
                        fourNumA == itemA[0]
                        break
                for itemB in samelistB:
                    if itemA[1] == 4 :
                        fourNumB == itemB[0]
                        break
                if fourNumB > fourNumA:
                    return True
                else:
                    return False
            elif cardsTypeA  == 'bomb':
                if cardsB > cardsA:
                    return True
                else:
                    return False
        return False
    
    def getCurPlaySeat(self):
        curplayseat =  (Landlords.roundBeginSeat + Landlords.curPlayCount % 3)%3 
        return curplayseat
    def isWin(self,player):
        if player.cards == "" :
            return True
        else:
            return False
    def playAble(self,player):
        ret = [False,"undefine error"]
        curplayseat = self.getCurPlaySeat()
        if player.seat != curplayseat:
            ret[1] = "还没有轮到你出牌，请稍安勿躁\n"
            return ret
        
        cardsType = self.getPlayCardsType(player)
        if not cardsType[0]:
            ret[1] = "不能这么出牌，请重新选择\n"
            return cardsType
        #第一个出牌
        if Landlords.curPlayCount == 0 and curplayseat == Landlords.roundBeginSeat:
            ret[0] = True
            ret[1] = 'OK'
            Landlords.curCardsType = cardsType[1]
        #
        else :
            prePlay = Landlords.curDeskCards.pop()
            playCardsType = self.getPlayCardsType(player)
            #可以出所给的牌
            if self.compareCards(prePlay, Landlords.curCardsType, player.play, playCardsType[1] ):
                ret[0] = True
                ret[1] = 'OK'
            else:
                ret[0] = False
                ret[1] = 'Wrong'
        
        return ret

    def play(self,player):
        ret = self.playAble(player)
        
        if ret:
            if self.isWin(player):
                ret[1] = 'win'
                return ret 
            else :
                Landlords.curDeskCards.append(player.play)
                
                for i in player.play:
                    player.cards.remove(i)
                    
                if self.isWin(player):
                    ret[1] = 'win'
                    return ret 
                else:Landlords.curPlayCount += 1
        return ret

    def Grablandlord(self):
        tmp = list()
        for p in Landlords.playerGroup:
            if p.role == 1 : 
                tmp.append(p.seat)
        random.shuffle (tmp)
        for p in Landlords.playerGroup:
            if p.seat == tmp[0] : 
                p.role = 'landLord'
            else:
                p.role = 'farmer'
        
    def checkPlay(self,player):
#         if player.seat == 0:
#             return player.play
#         for 
#         elif:
#             player.play
            return 
        
    def playerConfirm(self,player):
        ret = False
        for p in self.playerGroup:
            if player == p and player.seat == Landlords.roundBeginSeat: ret = True
        return ret
    def getPrePlayerState(self,curPlayer):
        preSeat = curPlayer.seat -1
        if preSeat == -1:preSeat = 2
        for p in Landlords.playerGroup:
            if p.seat == preSeat :
                return p.roundState
    def beginNewRound(self,beginSeat):
        Landlords.round += 1
        Landlords.roundBeginSeat = beginSeat
        Landlords.curPlayCount = 0
        
    def seatAllocation(self):
        seat = random.randint(0, 2)      
        for p in Landlords.playerGroup:
            p.seat = seat
            seat += 1
            if seat == 3:seat = 0
                        
    def roundHandle(self,player):
        ret = [False,'undefine error type']
#        -------------------------------------------
        if Landlords.round == -1:
            ret[1] = 'error in roundhandle'
            return ret
#        --------------- 身份验证-------------------------- 
        if not self.playerConfirm(player):
            ret[1] = 'player error' 
            return ret
#        ----------------过牌--------------------------
        if player.input == '-p':
            if self.getPrePlayerState(player) == 'pass':
                beginSeat = (player.seat + 1)%3
                self.beginNewRound(beginSeat)
                ret[0] = True
                ret[1] = "newRound"
                return ret
            player.roundState = 'pass'
            Landlords.curPlayCount += 1
            return [True,'pass']
#        ----------------出牌--------------------------      
        elif Landlords.round == 0:
            self.Grablandlord()
        else:
            ret = self.play(player)
        
#         Landlords.round += 1
        return ret        
#             
    def start(self):
        msg = 'game start'
        self.seatAllocation()
        self.shuffle()
        self.draw()
        return "现在游戏开始：\n"   
    def reportResult(self):
        return
    
    def countSameCards(self,cards):
        sameList = list()
        tmpSet = set(cards)
        for item in tmpSet:
            sameList.append((item,cards.count(item)))
            
        return sameList
    def isSeqThreble(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen % 3 != 0:
            return ret
        for index in range(cardslen):
            if index <= cardslen - 4: 
                if index % 3 == 0 and cards[index] != cards[index + 3] -1:
                    return ret
                elif index % 3 == 0 :
                    for i in range(index,index + 3):
                        if i + 1 < index + 3:
                            if cards[i] != cards[i + 1]:
                                return ret
        ret = True
        return ret
    def isSeqDouble(self,cards):
        ret = False
        cardslen = len(cards)
        if cards[0] == 2:
            return ret
        if cardslen % 2 != 0:
            return ret
        for index in range(cardslen):
            if index <= cardslen - 3: 
                if index % 2 == 0 and cards[index] != cards[index + 2] -1:
                    return ret
                elif index % 2 == 0:
                    for i in range(index,index + 2):
                        if i + 1 < index + 2:
                            if cards[i] != cards[index + 1]:
                                return ret
        ret = True
        return ret
    
    def isSeqSingle(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen < 5:
            return ret
        for index in range(1,cardslen):
            if cards[index] == 2:
                return ret
                    
            if cards[index - 1 ] != cards[index]  - 1 :
                return ret 
        ret = True
        return  ret 
    def isRocket(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen != 2:
            return ret
        elif cards[0] == 15 and cards[1] == 16:
            ret = True
        elif cards[0] == 16 and cards[1] == 15:
            ret = True
        return ret
    
    def isFlySingle(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen % 4 != 0 and cardslen < 8:
            return ret
        else:
            samelist = list()
            samelist  = self.countSameCards(cards)            
            samelist.sort()
#             for index in range(len(samelist)):
#                 if samelist[index][1] == 3:
#                     for i in range(cardslen / 4):
#                         if index + i + 1 <= cardslen / 4: 
#                             if samelist[index + i][0] != samelist[index + i + 1][0] - 1:
#                                 return ret
            bCut = False
            for index in range(len(samelist)):
                if samelist[index][1] > 3:
                    return ret
                elif samelist[index][1] == 3:
                    if not bCut:          
                        tmp = list()
                        tmp = samelist[index : index + cardslen / 4]
                        bCut = True
                        if len(tmp) < 2:
                            return False
                        for i in range(0,len(tmp)):
                            if tmp[i][1] != 3:
                                return False 
                            elif i < len(tmp) -1  and tmp[i+1][0] -1 != tmp[i][0]:
                                return False 
                        continue 
        ret = True
        return ret
    def isFlyDouble(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen % 5 != 0 or cardslen < 10:
            return ret
        else:
            samelist = list()
            samelist  = self.countSameCards(cards)
            samelist.sort();
            bCut = False
            for index in range(len(samelist)):
                if samelist[index][1] != 2 and samelist[index][1] != 3:
                    return ret
                elif samelist[index][1] == 3:
                    if not bCut:          
                        tmp = list()
                        tmp = samelist[index : index + cardslen / 5]
                        bCut = True
                        for i in range(0,len(tmp)):
                            if tmp[i][1] != 3:
                                return False 
                            elif i < len(tmp) -1  and tmp[i+1][0] -1 != tmp[i][0]:
                                return False                            
        ret = True
        return ret
    
    def isBomb(self,cards):
        ret = False
        samelist = list()
        samelist  = self.countSameCards(cards)
        samelist.sort()
        if len(samelist)!= 1 or samelist[0][1] != 4:
            return ret
        ret = True 
        return ret
    def isThreble(self,cards):
        ret = False
        samelist = list()
        samelist  = self.countSameCards(cards)
        samelist.sort()
        if len(samelist)!= 1 or samelist[0][1] != 3:
            return ret
        ret = True
        return ret
    
    def isThrebleOne(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen != 4:
            return ret
        for i in range(cardslen):
            if i + 1 < cardslen - 1 and cards[i] == cards[i + 1]:
                if i + 2 < cardslen -1 and  cards[i] == cards[i + 2]:
                    if i == 0 and cards[i] != cards[i + 3]:
                        return True
                    elif i == 1 and cards[i] != cards[0]:
                        return True
        return ret
    
    def isThrebleTwo(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen != 5:
            return ret
        sameCards = list()
        sameCards = self.countSameCards(cards)
        sameCards.sort()
        if len(sameCards) != 2 :
            return ret
        for i in sameCards:
            if i[1] != 2 and i[1] != 3:
                return ret 
#         for i in range(cardslen):
#             if i + 1 < cardslen  and cards[i] == cards[i + 1]:
#                 if i + 2< cardslen  and cards[i] == cards[i + 2] :
#                     return True
        ret = True
        return ret
    
    def isFourTwoSingle(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen != 6 :
            return ret
        sameCards = list()
        sameCards = self.countSameCards(cards)
        sameCards.sort()
        tmp =False
        if len(sameCards) != 3 and  len(sameCards) != 2:
            return ret
        for i in range(len(sameCards)):
#             if sameCards[i][1] == 2:
#                 return ret
            if  sameCards[i][1] == 4:
                tmp = True
        ret = tmp             
        return ret
    
    def isFourTwoDouble(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen != 8 :
            return ret
        sameCards = list()
        sameCards = self.countSameCards(cards)
        sameCards.sort()
        tmp =False
        if len(sameCards) != 3:
            return ret
        for i in range(len(sameCards)):
            if sameCards[i][1] == 1:
                return ret
            elif  sameCards[i][1] == 4:
                tmp = True
        ret = tmp             
        return ret
 
    def isDouble(self,cards):
        ret = False
        cardslen = len(cards)
        if cardslen!= 2 or cards[0] != cards[1]:
            return ret
        ret = True
        return ret
    
    def getPlayCardsType(self,player):
        cards = player.play
        cardsLen = len(cards)
        cardsType = [False,"errorType"]
        if cardsLen == 1:
            cardsType[0] = True
            cardsType[1] = 'single' 
            return cardsType
        elif cardsLen == 2:
            if self.isDouble(cards):
                cardsType[0] = True
                cardsType[1] = 'double' 
                return cardsType
            elif self.isRocket(cards):
                cardsType[0] = True
                cardsType[1] = 'rocket' 
                return cardsType
            else:
                return cardsType
        elif cardsLen == 3:
            if self.isThreble(cards):
                cardsType[0] = True
                cardsType[1] = 'threble' 
                return cardsType
            else:
                return cardsType
        elif cardsLen == 4:
            if self.isBomb(cards):
                cardsType[0] = True
                cardsType[1] = 'bomb' 
                return cardsType
            elif self.isThrebleOne(cards):
                cardsType[0] = True
                cardsType[1] = 'threbleOne' 
                return cardsType
            else:
                return cardsType
        elif cardsLen == 5:
            if self.isSeqSingle(cards):
                cardsType[0] = True
                cardsType[1] = 'seqSingle' 
                return cardsType
            elif self.isThrebleTwo(cards):
                cardsType[0] = True
                cardsType[1] = 'threbleTwo' 
                return cardsType
        elif cardsLen >= 6:
            if self.isSeqSingle(cards):
                cardsType[0] = True
                cardsType[1] = 'seqSingle' 
                return cardsType
            elif self.isSeqDouble(cards):
                cardsType[0] = True
                cardsType[1] = 'seqDouble' 
                return cardsType
            elif cardsLen == 6:
                if self.isFourTwoSingle(cards):
                    cardsType[0] = True
                    cardsType[1] = 'fourTwoSingle' 
                    return cardsType
                if self.isSeqThreble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'seqThreble' 
                    return cardsType
            elif cardsLen == 8:
                if self.isFourTwoDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'fourTwoDouble' 
                    return cardsType
                elif self.isFlySingle(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flySingle' 
                    return cardsType
            elif cardsLen == 9:
                if self.isSeqThreble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'seqThreble' 
                    return cardsType
            elif cardsLen == 10:
                if self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flyDouble' 
                    return cardsType
            elif cardsLen == 12:
                if self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flySingle' 
                    return cardsType
            elif cardsLen == 15:
                if self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flyDouble' 
                    return cardsType
            elif cardsLen == 16:
                if self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flySingle' 
                    return cardsType
            elif cardsLen == 20:
                if self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flySingle' 
                    return cardsType
                elif self.isFlyDouble(cards):
                    cardsType[0] = True
                    cardsType[1] = 'flyDouble' 
                    return cardsType
        return cardsType 
        
class Players:
#     def setGameState(self,attribute,states):
#         if attribute == 'seat':self.seat = states
#         elif attribute == 'handHog':self.handHog = True
#         self.grubLords = states
    def __init__(self,usr,nickname):
        self.usrJID = usr
        self.name = self.usrJID.node
        self.cards = list()
        self.game = ' '
        self.nickName = nickname
        self.input =''
        self.actionState = 'inaction'
        self.role = 'common'
        self.modeInit = False
        self.mode = 'normal'
        self.play = list() #本轮出牌
        self.roundState = '' #本回合状态
        self.seat = -1
    def myTurn(self,curRound):
        ret = -1
        if curRound == 0:
            ret = self.Grabthelandlord()
        else:
            ret = self.play()
        return ret
    def getPlayerName(self):
        return self.name   
    def play(self,pCards):
        return  self.nickName + "play" + pCards
    def joinGame(self):
        return
    def Grabthelandlord(self):
        if self.input == 'yes' or self.input =='y' :
            self.game.Grabthelandlord()
#         else 
        return
    def playCards(self,pCards):
        return
    def getCurCards(self):
        ret =''
        for p in self.cards:
            ret += bytes(p)
            ret += '|'
        return ret
    
    def getPlayerNickName(self):
        return self.nickName   
 
    def setNickName(self,nickname):
        self.nickName = nickname
    
    def setCards(self,cards):
        self.cards = cards
        

if __name__ == "__main__":
#     players = ['Xman','Spider','Superman']
#     plist = list()
#     plist.append(Players("one 3",'sda',5)) 
#     plist.append(Players("two 3",'sda',2))
#     plist.append(Players("three 3",'sda',6))
#     plist.append(Players("four 3",'sda',9))
#     
#     plist.sort(cmp=None, key=lambda x:x.sortID, reverse=False)
#     plist.sort(plist,key=lambda x:x.sortID)
#     print "haha"
#     a = [1,2,3,4,5,6,6,6,3,3,7,]
#     a.remove(6)
#     a.remove(6)
#     a.remove(6)
    print a
#     print sorted(plist, key=lambda x:x.sortID)
#     plist.sort(cmp=None, key=None, reverse=False)
    
#     landlds = Landlords(players)
#     cards = [4,4,4,6]
#     cards = [1,1,1,4,4]
#     ret = landlds.isDouble(cards)
#     ret = landlds.isThreble(cards)
#     ret = landlds.isBomb(cards)
#     ret = landlds.isFlyDouble(cards)
#     ret = landlds.isRocket(cards)
#     ret =  landlds.isSeqSingle(cards)
#     ret = landlds.isFlySingle(cards)
#     ret = landlds.isFourTwoSingle(cards) 
#     ret = landlds.isFourTwoDouble(cards)
#     ret = landlds.isSeqDouble(cards)
#     ret = landlds.isSeqThreble(cards)
#     ret = landlds.isThrebleOne(cards)
#     ret = landlds.isThrebleTwo(cards) 
#     player = Players('ljq','hehe',cards)
#     ret = landlds.getPlayCardsType(player)   
#     print ret
#     if ret :
#         print 'OK'
#     else:
#         print 'wrong'
#     landlds.shuffle()
#     landlds.draw()
#     print landlds.cards
#     print landlds.playerCards