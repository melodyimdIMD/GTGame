# -*- coding: utf-8 -*-
import sys
import time
from Landlords import Players 
from Landlords import Landlords

from Robot import GtalkRobot
from dns.rdatatype import NULL

#########################################################################################

class SampleBot(GtalkRobot):
    gameGroup = list()
    game = Landlords()
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
    def command_100_default(self, user, message, args = NULL):
        '''.*?(?s)(?m)'''
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))
        
    def command_010_game(self, user, message, args = NULL):
    #the __doc__ of the function is the Regular Expression of this command, if matched, this command method will be called. 
    #The parameter "args" is a list, which will hold the matched string in parenthesis of Regular Expression.
        '''(/game)( +(.*))?$(?i)'''
        if self.modeInit == False :
            self.mode = 'game'
            bnewGroupmember = True       
            for i in SampleBot.gameGroup:
                if user == i:bGroupmember = False    
            if SampleBot.group == null or bnewGroupmember: 
                player = Players(user)
                SampleBot.gameGroup.append(player)
            totalPlayer = 0   
            for i in SampleBot.gameGroup:
                if i : totalPlayer += 1
            if totalPlayer == 3:
#                 SampleBot.game.play() 
                # 输入/ready 等待其他玩家准备完毕，即可开始游戏\n
            text = "你已进入游戏模式(默认：斗地主)，输入/q 或/quit 退出,\n"\
                    + "-----------------------------------------------------------------------------------"
            self.replyMessage(user, text)
            self.modeInit = True
        self.replyMessage(user, "请等待。。。")
        
        
        
    def modeControl(self, user, message, args):
        if self.mode == 'game':self.command_010_game(user, message, args)
        
    def findPlayer(self,usr):
        for player in SampleBot.gameGroup:
            if usr == player.name:return player
        return False
    
    def __init__(self,game):
        
#         SampleBot.game = game
        return
#         elif self.mode == 'chat':   
        

#########################################################################################
if __name__ == "__main__":
    bot = SampleBot()
    bot.setState('available', "ljq`s game room")
    bot.start("livasu517@gmail.com", "rianeihualan")