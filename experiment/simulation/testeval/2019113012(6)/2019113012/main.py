import time
from colorama import Fore, Back, Style
from input import *
#from board import *
from collision import *
from test import *
from paddle import *
from ball import *
from time import sleep
from brick import *
from powerup import *
import os 
getch = Get()
var = 0 
flag = 0
flag1=0
flag2=0
flag3=0
xvel=0
yvel=0
lent = 2
cntr=var+2
xorg=0
yorg=0
tdarr=[]
ball = gameball()
mballs = multiballs()
pwrup = managepowerup()
#mv = move()
timetrack = time.time()
paddle = paddl()
prnt=printboard()
brick = brickarray()
#scrobj = printboard()
while(1):
    
    if time.time()-timetrack >= 0.10:
        timetrack = time.time()
        if flag == 0:
            prnt.getinitalscreen() #initializing the screen
            tdarr = prnt.copygrid()
            tdarr = brick.createarr(tdarr)
            tdarr[34] = ball.initializeball()
            tdarr[35] = paddle.initializepaddle()
            pwrup.reset()
            mballs.reset()
            #tdarr = brick.createarr(tdarr)
            

            prnt.setupdategrid(tdarr)
            prnt.initializetime() 
            flag=1
        else:
            flag2 = 0
            tdarr = prnt.copygrid()
            tdarr=paddle.returnpaddle(tdarr)
            c = input_to(getch)
            if c=='d':
                #var=mv.movright(var)
                if paddle.padlrightpos()==1:
                    #print("here")
                    tdarr,flag2 = paddle.callmoveright(tdarr)
                    if flag1==0:
                        #print("i am here1")
                        #print(ball.moveballright())
                        tdarr[34]=ball.shiftballright()
                    #tdarr = ball.initright(tdarr)
                    prnt.setupdategrid(tdarr)
            elif c=='a':
                if paddle.padlleftpos()==1:
                    tdarr,flag2 = paddle.callmoveleft(tdarr)
                    if flag1==0:
                        tdarr[34]=ball.shiftballleft()
                    prnt.setupdategrid(tdarr)
            elif c==' ':
                if flag1==0:
                    flag1=1
                    cntr = paddle.getpadlcentr()
                    ball.fireball(cntr)
                    mballs.initializeinitalball(ball.getxpos(),ball.getypos(),ball.getxvel(),ball.getyvel())
                else:
                    paddle.paddledegrab()
                    mballs.setballarr(paddle.getactivatepaddlearr())
            if c=='q':
                break
            # if c=='t':
            #     mballs.addball()
            #tdarr = brick.createarr(tdarr)
            cntr = paddle.getpadlcentr()
            if flag1 !=0:
                scr = prnt.getscore()
                brick,pwrup,tdarr,scr = mballs.checkbrickcollision(brick,pwrup,tdarr,scr)
                prnt.updatescore(scr)
                # x,y,iden = brick.checkcollisionbrick(ball.getxvel(),ball.getyvel(),ball.getxpos(),ball.getypos())
                # print("iden = ",iden)
                # if iden != -1:
                #     tdarr = brick.removebrick(tdarr,iden)
                #     pwrup.createpowerup(tdarr,brick.getarray(),iden,brick.retrunidval())
                # brick,pwrup = 
                tdarr = pwrup.checkcolllid(paddle.getpadlresid(),paddle.getpadlcentr(),tdarr)
                paddle,mballs = pwrup.updatepowerups(paddle,mballs)
                tdarr = pwrup.updateallpos(tdarr)
                #ball.updateveloc(x,y)
                tdarr,paddle = mballs.updateallballpos(tdarr,cntr,paddle.getpadlresid(),paddle)
                flag2 = paddle.getactivategrabpaddle()
                #tdarr=ball.setballupdate(tdarr,cntr,paddle.getpadlresid())
                
                #prnt.setupdategrid(tdarr)
            prnt.setupdategrid(tdarr)
            #print("flag2 here=",flag2)
            #mballs.removeballs()
            if mballs.removeballs()==0 and flag1!=0 and flag2==0:
                flag = 0
                ball.restoreflag()
                tdarr = []
                prnt.getlives()
                paddle.resetpadlpos()
                flag1=0

        #sleep(0.3)
        #tdarr = brick.createarr(tdarr)
        os.system('clear')
        prnt.callprintscreen(brick.returnvis(),brick.retrunidval(),brick.getarray())
        #os.system('clear')
        #print("\033[%d;%dH" % (0, 0))
        #os.system('clear')
        #print("\033[%d;%dH" % (0, 0))
        
     




