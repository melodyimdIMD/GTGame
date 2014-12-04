# -*- coding: utf-8 -*-
import sys
import time
from Landlords import Players 
from Landlords import Landlords

from Robot import GtalkRobot
from dns.rdatatype import NULL
from functools import total_ordering
from Canvas import Group


reload(sys)
sys.setdefaultencoding('utf-8') 
#########################################################################################

class SampleBot(GtalkRobot):
    gameGroup = list()
    chatGroup = list()
    normalGroup = list()
    game = NULL
#     game = Landlords()
    #Regular Expression Pattern Tips:
    # I or IGNORECASE <=> (?i)      case insensitive matching
    # L or LOCALE <=> (?L)          make \w, \W, \b, \B dependent on the current locale
    # M or MULTILINE <=> (?m)       matches every new line and not only start/end of the whole string
    # S or DOTALL <=> (?s)          '.' matches ALL chars, including newline
    # U or UNICODE <=> (?u)         Make \w, \W, \b, and \B dependent on the Unicode character properties database.
    # X or VERBOSE <=> (?x)         Ignores whitespace outside character sets
    
    #"command_" is the command prefix, "001" is the priviledge num, "setState" is the method name.
    #This method is used to change the state and status text of the bot.
    def command_001_setState(self, user, message, args):
        #the __doc__ of the function is the Regular Expression of this command, if matched, this command method will be called. 
        #The parameter "args" is a list, which will hold the matched string in parenthesis of Regular Expression.
        '''(available|online|on|busy|dnd|away|idle|out|off|xa)( +(.*))?$(?i)'''
        show = args[0]
        status = args[1]
        jid = user.getStripped()

        # Verify if the user is the Administrator of this bot
        if jid == 'ldmiao@gmail.com':
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            self.replyMessage(user, "State settings changed！")

    #This method is used to send email for users.
    def command_002_SendEmail(self, user, message, args):
        #email ldmiao@gmail.com hello dmeiao, nice to meet you, bla bla ...
        '''[email|mail|em|m]\s+(.*?@.+?)\s+(.*?),\s*(.*?)(?i)'''
        email_addr = args[0]
        subject = args[1]
        body = args[2]
        #call_send_email_function(email_addr, subject,  body)
        
        self.replyMessage(user, "\nEmail sent to "+ email_addr +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
    
    #This method is used to response users.
    def command_100_default(self, curUser, message, args = NULL):
        '''.*?(?s)(?m)'''
#         self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
#         text = "请输入/help查看帮助"
        msg = curUser.nickName + "悄悄地说："+ message
        self.broadcast(msg,'normalGroup')
#         self.replyMessage(user,text)
    def noticeSinglePlayer(self,player,msg):
        self.replyMessage(player.usrJID,msg)
    def noticeAllPlayer(self,msg):
        for p in SampleBot.gameGroup:
            self.replyMessage(p.usrJID,msg)
            
    def noticePlayerAction(self,player,act):
        txt = player.nickName +"在本回合"+ act
        for p in SampleBot.gameGroup:
            self.replyMessage(p.usrJID,txt)
        
        
    def command_010_game(self, curUser, message, args = NULL):
    #the __doc__ of the function is the Regular Expression of this command, if matched, this command method will be called. 
    #The parameter "args" is a list, which will hold the matched string in parenthesis of Regular Expression.
        '''(/game)( +(.*))?$(?i)'''
#         self.modeInit(user)
#         if not self.allReady:
#             queue = self.getReadyQueue()
#             if self.mode == 'ready' :tmp = "你已经在等待队列"
#             text = tmp + "请等待其他玩家准备就绪。。。\n"\
#                    "目前在游戏队列中的玩家为："+ queue +'\n'\
#                    "集齐3名玩家即可开始游戏"
#             self.replyMessage(user, text)
#         else:
    def modeInits(self, curUser,command):
        command = command.split(' ')
        if command[0] == '/!q' :
            curUser.modeInit = False #game initflag
            if curUser.mode == 'ready':
                SampleBot.gameGroup.remove(curUser)
                text =  "************************************************\n"\
                        "你已退出游戏模式,你可以 \n"\
                        "-------->输入/game 重新进入游戏模式，或者\n"\
                        "-------->输入/help 查看帮助\n"\
                        "************************************************"
            self.replyMessage(curUser.usrJID, text) 
            curUser.mode = 'normal'
        if command[0] == '/quit' or command =='/q' :
            curUser.modeInit = False #game initflag
            text= "啊 啊 啊 啊啊啊 出错了"
            if curUser.mode == 'normal':
                text = "你已经在普通模式"
            if curUser.mode == 'gaming':
                text = "请完成该局后再退出"
                self.replyMessage(curUser.usrJID, text)
                return
            if curUser.mode == 'ready':
                SampleBot.gameGroup.remove(curUser)
                text =  "************************************************\n"\
                        "你已退出游戏模式,你可以 \n"\
                        "-------->输入/game 重新进入游戏模式，或者\n"\
                        "-------->输入/help 查看帮助\n"\
                        "************************************************"
            self.replyMessage(curUser.usrJID, text) 
            curUser.mode = 'normal'
        elif command[0] == '/game' :
            curUser.mode = 'preGame'
            curUser.modeInit = True 
            text =  "************************************************\n"\
                    "你已进入游戏模式(默认游戏：斗地主),你可以 \n"\
                    "-------->输入/ready 加入准备队列,\n"\
                    "-------->输入/q 或/quit 退出,\n"\
                    "************************************************"
            self.replyMessage(curUser.usrJID, text)
            #----------
        elif command[0] == '/ready' and curUser.mode == 'preGame':
            bGroupmember = False
            curUser.mode = 'ready'
            for i in SampleBot.gameGroup:
                if curUser == i:bGroupmember = True
            if not bGroupmember :
                if curUser.nickName == '': curUser.nickName = curUser.node
                SampleBot.gameGroup.append(curUser) 
            if self.getTotalGroupNum() == 1:
                #------------------------------------
                A = list()
                B = list()
                A.append(SampleBot.gameGroup[0].usrJID)
                B.append(SampleBot.gameGroup[0].usrJID)
                playerA = Players(A[0],"OOOOO")
#                 playerA.usrJID.node = "AAAAAA"
                playerB = Players(B[0],"XXXXX")
#                 playerB.usrJID.node = "BBBB"
                SampleBot.gameGroup.append(playerA)
                SampleBot.gameGroup.append(playerB)
                #------------------------------------
                SampleBot.game = Landlords(SampleBot.gameGroup) 
                SampleBot.game.start()
                msg = "游戏正式开始,是否抢地主？\n"\
                      "抢：-y,不抢: -p \n"
                self.noticeAllPlayer(msg)
                for p in SampleBot.gameGroup:
                    p.mode = 'gaming'
                return
            queue = self.getReadyQueue()
            text =  "************************************************\n"\
                    "已加入准备队列，队列中的玩家为："+queue+" \n"\
                    "等待其余玩家准备完毕，等待中。。。 \n"\
                    "************************************************"
            self.replyMessage(curUser.usrJID, text)
        elif command[0] == '/nick':
            curUser.setNickName(command[1])
            self.broadcast("用户:"+curUser.usrJID.node+"将昵称设置为："+command[1])
        
        elif command[0] == '/help':
            text =  "************************************************\n"\
                    "支持的命令有： \n"\
                    "/game ---进入游戏模式 \n"\
                    "/quit ---返回普通模式 \n"\
                    "/nick ---设置昵称，\n"\
                    "     用法：/nick + ”昵称名“ （空格分隔） \n"\
                    "/ready ---准备就绪，加入游戏队列，等待游戏开始 \n"\
                    "/queue ---查看游戏队列中的玩家\n"\
                    "-：出牌，\n"\
                    "     用法: '-' + '牌'，示例：-34567（出34567）\n"\
                    "************************************************"
            self.replyMessage(curUser.usrJID, text)
        elif command[0] == '/queue':
            queue = self.getReadyQueue()
            text =  "************************************************\n"\
                    "已加入准备队列，队列中的玩家为："+queue+" \n"\
                    "等待其余玩家准备完毕，等待中。。。 \n"\
                    "************************************************"
            self.replyMessage(curUser.usrJID, text)
            
    def getTotalGroupNum(self):
        return len(SampleBot.gameGroup)
      
    def getGameGroupMbNickName(self):
        members = list()

        for p in SampleBot.gameGroup:
            members.append(p.getPlayerNickName())
        return members
    def roundHandle(self,player):
        #第0回合
        if SampleBot.game.round == 0 and player.role != 1 and player.role != 0:
            if player.input == '-y':
                player.role = 1
                msg = "我抢，\n"
                self.noticeSinglePlayer(player, msg)
            elif player.input == '-p':
                player.role = 0
                msg = "我不抢，\n"
                self.noticeSinglePlayer(player, msg)
            else :
                msg = "请重新选择，\n"\
                      "抢地主输入 : -y 不抢输入: -n\n"
                self.noticeSinglePlayer(player, msg)
        elif SampleBot.game.round > 0:
            if player.input[0] != '-':
                msg = "不合法的操作，请在要出的牌前加上'-'号\n"\
                      "示例: -56666  (出三带一)\n"
                self.noticeSinglePlayer(player, msg)
            else :
                tmp = player.input[1:len(player.input)]
                for i in tmp:
                    if i == 'J':i = 11
                    elif i == 'Q':i = 12
                    elif i == 'K':i = 13
                    elif i == 'A':i = 14
                    elif i == '☆':i = 15
                    elif i == '★':i = 16 
                player.play = tmp
                ret = SampleBot.game.roundHandle(player)
                self.noticeAllPlayer(ret[1])
                
    def handleGaming(self,curUser, message):
        self.roundHandle(curUser)
        return
    
    def addMember(self,usr,nickname,group = 'normalGroup'):
        player = Players(usr,nickname)
        if group == 'normalGroup':
            SampleBot.normalGroup.append(player)
        elif group == 'chatGroup':
            SampleBot.gameGroup.append(player)
        elif group == 'gameGroup':
            SampleBot.gameGroup.append(player)
        return player 
            
    def authentication(self,usr,group = 'normalGroup'):
        if group == 'normalGroup':
            for p in SampleBot.normalGroup:
                if p.usrJID == usr : return p
       
        if group == 'chatGroup':
            for p in SampleBot.chatGroup:
                if p.usrJID == usr : return p
       
        elif group == 'gameGroup':
            for p in SampleBot.gameGroup:
                if p.usrJID == usr : return p
       
        return         
                
    def modeControl(self, user, message, args = NULL):
        curUser = NULL
        curUser = self.authentication(user)
        if not curUser: 
            nickname = user.node
            curUser = self.addMember(user, nickname, 'normalGroup')
            self.replyMessage(user, '欢迎尊贵的'+nickname+'来到活动室\n')
        
                
        if message[0] == '/':
            self.modeInits(curUser, message)
            return
        if curUser.mode == 'preGame' or curUser.mode == 'ready':
            self.command_010_game(curUser, message, args)
        elif curUser.mode == 'gaming':
            player = self.authentication(user, "gameGroup") 
            self.handleGaming(player, message)
        else :
            self.command_100_default(curUser, message, args)
        
    def findPlayer(self,usr):
        for player in SampleBot.gameGroup:
            if usr == player.name:return player
        return False
    
    def getReadyQueue(self):
        queue = "("
        for t in self.getGameGroupMbNickName():
            if t and queue != "(" :queue += ' , '
            queue += t
        queue +=  ")"
        return queue
    
    def broadcast(self,msg,group = "normalGroup"):
        if group == "normalGroup":
            for player in SampleBot.normalGroup:
                self.replyMessage(player.usrJID, msg)
        
        elif group == "gameGroup":
            for player in SampleBot.gameGroup:
                self.replyMessage(player.usrJID, msg)
        elif group == "chatGroup":
            for player in SampleBot.chatGroup:
                self.replyMessage(player.usrJID, msg)        
        else :
            for player in SampleBot.normalGroup:
                self.replyMessage(player.usrJID, msg)
                   
            
    def __init__(self):
        self.nickName = ''
#         SampleBot.game = game
        return
#         elif self.mode == 'chat':   
#########################################################################################
if __name__ == "__main__":
    bot = SampleBot()
    bot.setState('available', "ljq`s game room")
    bot.start("livasu517@gmail.com", "xxxx")