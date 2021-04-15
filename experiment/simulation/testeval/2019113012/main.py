import time
from colorama import Fore, Back, Style
from boss import *
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
minimumnew = 0
flag1=0
flag2=0
flag3=0
xvel=0
paddleflag = 0
yvel=0
levelupplease = 0
lent = 2
cntr=var+2
xorg=0
yorg=0
firecannon = 0
tdarr=[]
paddletime = 0
ball = gameball()
mballs = multiballs()
pwrup = managepowerup()
#mv = move()
timetrack = time.time()
paddle = paddl()
prnt=printboard()
brick = brickarray()
boss = bossenemy()
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
            if prnt.getlevel()==2:
                tdarr = boss.initializeboss(tdarr)
            paddletime = time.time()
            pwrup.reset()
            mballs.reset()
            minimum1 = 0
            firecannon = 0
            # boss.createbomb()
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
                    if prnt.getlevel()==2:
                        tdarr = boss.moveright(tdarr)
                    if flag1==0:
                        #print("i am here1")
                        #print(ball.moveballright())
                        tdarr[34]=ball.shiftballright()
                    #tdarr = ball.initright(tdarr)
                    prnt.setupdategrid(tdarr)
            elif c=='a':
                if paddle.padlleftpos()==1:
                    tdarr,flag2 = paddle.callmoveleft(tdarr)
                    if prnt.getlevel()==2:
                        tdarr = boss.moveleft(tdarr)
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
            if c=='p':
                tdarr = brick.changebrickpos(tdarr)
            if c=='t':
                mballs.addball()
            if c=='l':
                levelupplease = 1
            if c=='m':
                tdarr = brick.movebrickdown(tdarr,5,1)
            if c=='f':
                if paddle.getcannon() == 1:
                    paddle.createbullet()
            # tdarr = brick.movebrickdown(tdarr)
            cntr = paddle.getpadlcentr()
            
            if flag1 !=0:
                scr = prnt.getscore()
                brick,pwrup,tdarr,scr,bricksdestroyed = mballs.checkbrickcollision(brick,pwrup,tdarr,scr)
                prnt.updatescore(scr)
                brick.setnewbricknumber(bricksdestroyed)
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
                tdarr,paddle,collidflag = mballs.updateallballpos(tdarr,cntr,paddle.getpadlresid(),paddle)
                print("paddle flag is=",collidflag)
                tdarr = brick.movebrickdown(tdarr,int(time.time()-paddletime),collidflag)
                flag2 = paddle.getactivategrabpaddle()
                if prnt.getlevel()==2:
                    boss.createbomb()
                    tdarr,paddle = boss.updatebombpos(tdarr,paddle,brick)
                    tdarr = boss.createcover(tdarr)
                    print("paddle health =",paddle.getpaddlehealth())
                    print("boss health=",boss.gethealth())
                    mballs,tdarr = boss.checkballcollision(mballs,tdarr)
                tdarr,brick,removebrickcheck = paddle.updatebulletpos(tdarr,brick)
                    #tdarr=ball.setballupdate(tdarr,cntr,paddle.getpadlresid())
                tdarr = paddle.cleartdarr(tdarr,brick)
                    
                if removebrickcheck!=-1:
                    tdarr,brickdestroy = brick.removebrick(tdarr,removebrickcheck)
                    pwrup.createpowerup(tdarr,brick.getarray(),removebrickcheck,brick.retrunidval(),0,-1)
                # scr+=1
                #prnt.setupdategrid(tdarr)
            prnt.setupdategrid(tdarr)
            #print("flag2 here=",flag2)
            #mballs.removeballs()
            minimumnew = brick.getminimum1()
            print("minimumnew=",minimumnew)
            if minimumnew == 1:
                print("game over")
                sys.exit()
            if (mballs.removeballs()==0 and flag1!=0 and flag2==0) or paddle.getpaddlehealth()==0:
                flag = 0
                ball.restoreflag()
                paddle.setpaddlehealth(4)
                tdarr = []
                prnt.getlives()
                paddle.resetpadlpos()
                paddletime = time.time()
                paddle.setcannon(0)
                flag1=0
                
            print("currentbricknumber=",brick.getcurrentbrick())
            
            
            # print("removebrickcheck=",removebrickcheck)
            if brick.getcurrentbrick()==0 or levelupplease ==1:
                flag = 0
                brick.increaselevel()
                ball.restoreflag()
                brick.setnewbricknumber(1)
                paddletime = time.time()
                paddle.setcannon(0)
                # tdarr = brick.changebrickpos(tdarr)
                tdarr = []
                levelupplease = 0
                # prnt.getlives()
                paddle.resetpadlpos()
                prnt.setlevel()
                flag1=0
            

        #sleep(0.3)
        #tdarr = brick.createarr(tdarr)
        brick.changerainbowcolor()
        os.system('clear')
        prnt.callprintscreen(brick.returnvis(),brick.retrunidval(),brick.getarray())
        #os.system('clear')
        #print("\033[%d;%dH" % (0, 0))
        #os.system('clear')
        #print("\033[%d;%dH" % (0, 0))
        
     




