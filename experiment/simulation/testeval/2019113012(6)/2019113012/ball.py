import random
from brick import *
from powerup import *
class gameball:
    def __init__(self):
        self.__xvel = 0
        self.__yvel = 0
        self.__ypos = 34
        self.__xpos = random.randint(1,5)
        #self.__xpos = 5
        self.__strin=""
        self.__resetflag = 0
        self.__prevchar = ''
        self.__flagpaddlegrab = 0
        self.__flagandgrab = 0
        self.__isthruball = 0
        self.pushedflag = 0

    def __initialball(self):
        self.__strin=""
        # self.__xpos = random.randint(1,5)
        self.__xpos = 3
        self.__ypos = 34
        for i in range(150):
            if i==0 or i==149:
                self.__strin+="|"
            elif i==self.__xpos:
                self.__strin+="o"
            else:
                self.__strin+=" "
        return self.__strin
    def __moveballright(self):
        #print("inside moveballright")
        self.__xpos+=2
        self.__strin=""
        for i in range(150):
            if i==0 or i==149:
                self.__strin+="|"
            elif i==self.__xpos:
                self.__strin+="o"
            else:
                self.__strin+=" "
        #print("here ",self.__strin)
        return self.__strin
    def __moveballleft(self):
        self.__xpos-=2
        self.__strin=""
        for i in range(150):
            if i==0 or i==149:
                self.__strin+="|"
            elif i==self.__xpos:
                self.__strin+="o"
            else:
                self.__strin+=" "
        return self.__strin
    def __releaseball(self,cntr):
        if self.__xpos > cntr:
            self.__xvel+=abs(self.__xpos-cntr)
        else:
            self.__xvel-=abs(self.__xpos-cntr)
        self.__yvel = -1
    def __checkreflection(self,xposnew,yposnew,cntr,resid):
        if xposnew <= 0:
            self.__xvel = -1*self.__xvel
            xposnew = self.__xpos + self.__xvel
        if xposnew >=148:
            self.__xvel = -1*self.__xvel
            xposnew = self.__xpos + self.__xvel
        if yposnew <=0:
            self.__yvel = -1*self.__yvel
            yposnew = self.__ypos + self.__yvel
        if yposnew >34:
            time = (35-self.__ypos)/abs(self.__yvel)
            varx = self.__xpos+(time*self.__xvel)
            # print(35-self.__ypos,"/",abs(self.__yvel))
            # print("time=",time)
            # print("varx=",varx)
           # print("varx=",varx)
            if varx<=cntr+resid and varx>=cntr-resid:
            #    print("i am here")
                if xposnew<=cntr:

                    # print("checking left wala part")
                    # print("xvel before =",self.__xvel)
                    # print("xcord before =",self.__xpos)
                    # print("cnter =",cntr)
                    # print("add wala part in left wala part =")
                    self.__xvel-=int(abs(cntr-varx))
                    # print("xvel after in left wala part =",self.__xvel)
                    # print("position and velocity are in left wala part",self.__xpos,self.__xvel)
                    if self.__xpos+self.__xvel <=0:
                        self.__xvel = -1*self.__xvel
                        xposnew = self.__xpos + self.__xvel
                else:
                    # print("checking right wala part")
                    # print("xvel before =",self.__xvel)
                    # print("xcord before=",self.__xpos)
                    # print("cnter=",cntr)
                    self.__xvel+=int(abs(varx-cntr))
                    
                    # print("xvel after =",self.__xvel)
                    # print("position and velocity are",self.__xpos,self.__xvel)
                    if self.__xpos+self.__xvel>=148:
                        self.__xvel = -1*self.__xvel
                        xposnew = self.__xpos + self.__xvel
                if self.getpaddlegrabflag()==1:
                        self.setflagandgrab(1)
                        self.__yvel = -1
                        return self.__xpos,self.__ypos
                self.__yvel = -1*self.__yvel
                yposnew = self.__ypos+self.__yvel

                    
            else:

                #print("xposnew=",xposnew,"yposnew=",yposnew,"cnter=",cntr,"approxpos=",time*self.xvel)
                self.__resetflag=1
                self.__xvel = 0
                self.__yvel = 0
        return xposnew,yposnew


    def __updateballpos(self,tdarr,cntr,resid):
        tempstr=""
        tempr=""
        #prev
        # for i in range(150):
        #     if i==0 or i==149:
        #         tempstr+="|"
        #     else:
        #         tempstr+=" "
        xposnew = self.__xpos + self.__xvel
        yposnew = self.__ypos + self.__yvel
        xposnew,yposnew = self.__checkreflection(xposnew,yposnew,cntr,resid)
      #  print("original ypos=",self.ypos,"neweypos =",self.yvel)
        for i in range(35):
            for j in range(150):
                if i == self.__ypos and j== self.__xpos:
                    #print("inside here i=",i," j=",j)
                    for k in range(150):
                        if tdarr[i][k]!='o':
                            tempstr+=tdarr[i][k]
                        else:
                            tempstr+=" "
                    tdarr[i]=tempstr
        for i in range(150):
            if i<xposnew:
                tempr+=tdarr[yposnew][i]
            elif i==xposnew:
                tempr+="o"
            else:
                tempr+=tdarr[yposnew][i]
       # print("yposnew=",yposnew)
        tdarr[yposnew]=tempr
        self.__xpos = xposnew
        self.__ypos = yposnew
        return tdarr
    def initializeball(self):
        return self.__initialball()
    def shiftballright(self):
        #print("inside shiftball right")
        return self.__moveballright()
    def shiftballleft(self):
        return self.__moveballleft()
    def fireball(self,cntr):
        return self.__releaseball(cntr)
    def setballupdate(self,tdarr,cntr,resid):
        return self.__updateballpos(tdarr,cntr,resid)
    def checkflag(self):
        return self.__resetflag
    def restoreflag(self):
        self.__resetflag = 0
    def getxpos(self):
        return self.__xpos
    def getxvel(self):
        return self.__xvel
    def getypos(self):
        return self.__ypos
    def getyvel(self):
        return self.__yvel
    def updateveloc(self,x,y):
        self.__xvel = x
        self.__yvel = y
    def setxypos(self,x,y):
        self.__xpos = x
        self.__ypos = y
    def setxvel(self,x):
        self.__xvel = x
    def setyvel(self,y):
        self.__yvel = y
    def setpaddlegrabflag(self,val):
        self.__flagpaddlegrab=val
    def getpaddlegrabflag(self):
        return self.__flagpaddlegrab
    def setflagandgrab(self,val):
        self.__flagandgrab=val
    def getflagandgrab(self):
        return self.__flagandgrab
    def setthruball(self,val):
        self.__isthruball=val
    def getthruball(self):
        return self.__isthruball
    def increasespeed(self):
        if self.getxvel()>=0:
            self.setxvel(self.getxvel()+1)
        else:
            self.setxvel(self.getxvel()-1)
    def resetdefaultspeed(self):
        if self.getxvel()>=0:
            self.setxvel(self.getxvel()-1)
        else:
            self.setxvel(self.getxvel()+1)
class multiballs:
    def __init__(self):
        self.ballarr = []
        self.flg = 0
    def reset(self):
        self.ballarr = []
        self.flg = 0
    def setballarr(self,ball):
        for i in range(len(ball)):
            print("transferred xvel = ",ball[i].getxvel())
            print("transferred yvel = ",ball[i].getyvel())
        for i in range(len(ball)):
            self.ballarr.append(ball[i])
        # for i in range(self.ballarr[i]):
    def getballarr(self):
        return self.ballarr
    def initializeinitalball(self,x,y,xvel,yvel):
        if self.flg ==0:
            temp = gameball()
            temp.setxypos(x,y)
            temp.updateveloc(xvel,yvel)
            self.ballarr.append(temp)
            self.flg = 1
    def updateallballpos(self,tdarr,cntr,resid,paddl):
        tempro = []
        cnt = 1
        while cnt!=0:
            cnt = 0
            for i in range(len(self.ballarr)):
                if self.ballarr[i].getflagandgrab()==1:
                    cnt+=1
                    tempro.append(self.ballarr[i])
                    self.ballarr.pop(i)
                    break
        for i in range(len(self.ballarr)):
            #if self.ballarr[i].getflagandgrab()==0:
           # print("before error=",self.ballarr[i].getyvel())
            tdarr = self.ballarr[i].setballupdate(tdarr,cntr,resid)
        if len(tempro)!=0:
            print("tempro length=",len(tempro))
            paddl.setactivatepaddlearr(tempro)
        return tdarr,paddl
    def addball(self):
        tempo = []
        for i in range(len(self.ballarr)):
            tempr = gameball()
            tempr.setxvel(self.ballarr[i].getxvel())
            tempr.setyvel(self.ballarr[i].getyvel())
            tempr.setxypos(self.ballarr[i].getxpos(),self.ballarr[i].getypos())
            tempo.append(tempr)
        for i in range(len(self.ballarr)):
            if self.ballarr[i].getxvel()!=0:
                tempo[i].setxvel(-1*(tempo[i].getxvel()))
            else:
                tempo[i].setxvel(1)
        for i in range(len(tempo)):
            self.ballarr.append(tempo[i])
    def checkbrickcollision(self,brick,pwrup,tdarr,scr):
        for i in range(len(self.ballarr)):
            #print("length = ",len(self.ballarr))
            #print("checking error i=",self.ballarr[i].getxvel())
            x,y,iden = brick.checkcollisionbrick(self.ballarr[i].getxvel(),self.ballarr[i].getyvel(),self.ballarr[i].getxpos(),self.ballarr[i].getypos(),self.ballarr[i].getthruball())
            if iden != -1:
                tdarr = brick.removebrick(tdarr,iden)
                pwrup.createpowerup(tdarr,brick.getarray(),iden,brick.retrunidval())
                scr+=1
            self.ballarr[i].updateveloc(x,y)
        return brick,pwrup,tdarr,scr
    def removeballs(self):
        cnt = 1
        while cnt!=0:
            cnt = 0
            for i in range(len(self.ballarr)):
                if self.ballarr[i].checkflag()==1:
                    self.ballarr.pop(i)
                    cnt+=1
                    break
        print("length = ",len(self.ballarr))
        return len(self.ballarr)
        #if len(self.ballarr)==0:
        #    return 1
        #return 0

        



    



        


            

    