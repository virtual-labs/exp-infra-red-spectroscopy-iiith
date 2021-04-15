from input import *
from board import *
from collision import *
from paddle import *
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
mv = move()
prnt=printboard()
while(1):
    print("\033[%d;%dH" % (0, 0))
    if flag == 0:
        tdarr=prnt.printscreeninit() #initializing the screen
        tdarr[35]
        padl = paddl(tdarr)
        flag=1
    else:
        dmar = ""
        prev=var
        c = input_to(getch)
        if c=='d':
            var=mv.movright(var)
        elif c=='a':
            var = mv.movleft(var)
        elif c==' ':
            if flag1==0:
                flag1=1
                xorg=var+2
                yorg=35
                flag2=0
                xvel=0
                yvel=1
                flag3=1
        if c=='q':
            break
        cntr=var+2
        xorg,yorg,xvel,yvel = collide.collidpaddle(xorg,yorg,xvel,yvel,cntr,2)
        xvel = collide.collidwalls(xorg,xvel)
        prnt.changepaddle(prev,var,flag3,tdarr)
        #padl.movetestaisehi()
        if flag1:
            print("here i come again")
            print("yvel is ",yvel)
            xorg,yorg,flag2,xvel,yvel,tdarr=prnt.changebalpos(xorg,yorg,flag2,xvel,yvel,tdarr)
        prnt.printscreen(tdarr)
        
     