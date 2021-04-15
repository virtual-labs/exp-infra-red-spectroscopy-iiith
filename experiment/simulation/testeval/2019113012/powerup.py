import time
import random
class power:
    def __init__(self):
        self.xcord = 0
        self.ycord = 0
        self.xvel = 0
        self.yvel = 1
        self.flag = 0
        self.powerarr = ['A','B','C','D','E','F']
        self.prevstrin = ""
        self.cnt = 0
        self.id = 0
        self.time = 0
    def updatepos(self):
        pass
    def setid(self,ident):
        pass
    def setxpos(self,x):
        pass
    def setypos(self):
        pass
    
class expandpaddle(power):
    def __init__(self):
        super().__init__()
        self.char = 'E'
        self.powerxvel = 0
        self.poweryvel = 0
        self.id = 1
        self.elem_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag=0
        self.dontprint = 0
        self.fire = 0
        self.prev=""
        self.endtime=0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def setfire(self):
        self.fire = 1
    def fireendtime(self):
        self.endtime = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val
class contractpaddle(power):
    def __init__(self):
        super().__init__()
        self.char = 'C'
        self.id = 2
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val

class multipleballs(power):
    def __init__(self):
        super().__init__()
        self.char = 'M'
        self.id = 3
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val
    
# class increasespeed(power):
#     def __init(self):
#         super().__init__()
class paddlgrab(power):
    def __init__(self):
        super().__init__()
        self.char = 'P'
        self.id = 4
        self.xvel = 0
        self.yvel = 0
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val
class thruball(power):
    def __init__(self):
        super().__init__()
        self.char = 'T'
        self.id = 5
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val
class increaseballspeed(power):
    def __init__(self):
        super().__init__()
        self.char = 'I'
        self.id = 6
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val

class cannon(power):
    def __init__(self):
        super().__init__()
        self.char = 'B'
        self.id = 7
        self.element_id = 0
        self.removeflag = 0
        self.startflag = 0
        self.collidflag = 0
        self.dontprint = 0
        self.prev=""
        self.fire = 0
        self.endtime = 0
        self.xvel = 0
        self.yvel = 0
        self.yprev = ''
    def updatepos(self,tdarr):
        temp = ""
        tempr = ""
        if self.dontprint ==1:
            return tdarr
        if self.startflag==0:
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            self.startflag=1
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o' or self.prev[i]=='@' or self.prev[i]=='B' :
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            self.yprev = self.ycord
            tdarr[self.ycord] = temp
        else:
            tempr = ''
            tdarr[self.yprev] = self.prev
            if (self.xcord + self.xvel <= 0) or (self.xcord + self.xvel >=149):
                self.xvel = -1*self.xvel
            if (self.ycord + self.yvel <= 0) or (self.ycord + self.yvel >=149):
                self.yvel = -1*self.yvel
            self.xcord = self.xcord + self.xvel
            self.ycord = self.ycord + self.yvel
            if self.yvel <= 0:
                self.yvel = self.yvel + 1
            print("yvel is",self.yvel)
            self.prev = tdarr[self.ycord]
            for i in range(len(self.prev)):
                if self.prev[i]=='o' or self.prev[i]=='@' or self.prev[i]=='B':
                    tempr +=' '
                else:
                    tempr +=self.prev[i]
            self.prev = tempr
            temp=""
            for i in range(150):
                if i==self.xcord:
                    temp+=self.char
                else:
                    temp+=tdarr[self.ycord][i]
            

            tdarr[self.ycord]=temp
            self.yprev = self.ycord
        return tdarr
    def setid(self,ident):
        self.element_id = ident
    def setxpos(self,x):
        self.xcord = x
    def setypos(self,y):
        self.ycord = y
    def setdontprintflag(self):
        self.dontprint = 1
    def setcollideflag(self):
        self.collidflag = 1
    def setcollideflag(self):
        self.collidflag = 1
    def getiden(self):
        return self.id
    def settime(self):
        self.time = time.time()
    def fireendtime(self):
        self.endtime = 1
    def setfire(self):
        self.fire = 1
    def setxvel(self,val):
        self.xvel = val
    def setyvel(self,val):
        self.yvel = val
class managepowerup:
    def __init__(self):
        self.poweruparr = []
        self.elemid = 0
    def setdefault(self):
        self.poweruparr = []
        self.elemid = 0
    def createpowerup(self,tdarr,arr,iden,idarr,ballxvel,ballyvel):
        x = 100
        y = 100
        for j in range(len(arr)):
            if arr[j].getid()==iden:
                #print("inside powerup id = ",iden)
                xcomprs,xcompre,ycomprs,ycompre = arr[j].getcomps()
                x = int((xcomprs+xcompre)/2)
                y = int((ycomprs+ycompre)/2)
                #print("inside x and y",x,y)
        # idx = random.randint(0,5)
        idx = 6
        if idx == 0:
            temp = contractpaddle()
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            #print("checking here",temp.id)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
        elif idx == 1:
            temp = expandpaddle()
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
        elif idx ==2:
            temp = multipleballs()
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
        elif idx==3:
            temp = paddlgrab()
            #print("checking here",temp.id)
            #print(temp.collidflag)
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
            #print("checking this",temp.collidflag)
        elif idx==4:
            temp = thruball()
            #print("checking here",temp.id)
            #print(temp.collidflag)
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
            #rint("checking this",temp.collidflag)
        elif idx==5:
            temp = increaseballspeed()
            #print("checking here",temp.id)
            #print(temp.collidflag)
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)
            #print("checking this",temp.collidflag)
        else:
            temp = cannon()
            #print("checking here",temp.id)
            #print(temp.collidflag)
            temp.setid(self.elemid+1)
            temp.setxpos(x)
            temp.setypos(y)
            temp.setxvel(ballxvel)
            temp.setyvel(ballyvel)
            self.elemid = self.elemid + 1         
            self.poweruparr.append(temp)

    def checkcolllid(self,resid,cntr,tdarr):
        for i in range(len(self.poweruparr)):
            if self.poweruparr[i].ycord == 34:

                if (self.poweruparr[i].xcord>=cntr-resid) and (self.poweruparr[i].xcord<=cntr+resid):
                    
                    self.poweruparr[i].setdontprintflag()
                    self.poweruparr[i].setcollideflag()
                    self.poweruparr[i].settime()
                    strin = ''
                    for j in range(150):
                        if j==self.poweruparr[i].xcord:
                            strin+=' '
                        else:
                            strin+=tdarr[self.poweruparr[i].ycord][j]
                    tdarr[self.poweruparr[i].ycord] = strin
                    self.poweruparr[i].ycord = self.poweruparr[i].ycord+1
                else:
                    self.poweruparr[i].setdontprintflag()
                    
                    strin = ''
                    for j in range(150):
                        if j==self.poweruparr[i].xcord:
                            strin+=' '
                        else:
                            strin+=tdarr[self.poweruparr[i].ycord][j]
                    tdarr[self.poweruparr[i].ycord] = strin
                    self.poweruparr[i].ycord = self.poweruparr[i].ycord+1
        return tdarr
    #def checktime(self):
    #    for i in range(len(self.poweruparr)):
    def reset(self):
        self.poweruparr=[]

    def updatepowerups(self,paddl,mballs):
        for i in range(len(self.poweruparr)):
            if self.poweruparr[i].collidflag == 1:
                if self.poweruparr[i].getiden() == 1:
                    if int(time.time()-self.poweruparr[i].time)>10:
                        if self.poweruparr[i].endtime==0:
                            self.poweruparr[i].fireendtime()
                            paddl.decreasepadllength()
                    if self.poweruparr[i].fire==0:
                        paddl.increasepadllength()
                        self.poweruparr[i].setfire()
                elif self.poweruparr[i].getiden()==2:
                    if int(time.time()-self.poweruparr[i].time)>10:
                        if self.poweruparr[i].endtime==0:
                            self.poweruparr[i].fireendtime()
                            paddl.increasepadllength()
                    if self.poweruparr[i].fire==0:
                        paddl.decreasepadllength()
                        self.poweruparr[i].setfire()
                elif self.poweruparr[i].getiden()==3:
                    #for i in range(len(ballarr)):
                    if self.poweruparr[i].endtime==0:
                        self.poweruparr[i].fireendtime()
                        mballs.addball()
                elif self.poweruparr[i].getiden()==4:
                    if int(time.time()-self.poweruparr[i].time)>15:
                        for i in range(len(mballs.ballarr)):
                            mballs.ballarr[i].setpaddlegrabflag(0)
                    else:
                        for i in range(len(mballs.ballarr)):
                            mballs.ballarr[i].setpaddlegrabflag(1)
                elif self.poweruparr[i].getiden()==5:
                    if int(time.time()-self.poweruparr[i].time)>15:
                        for i in range(len(mballs.ballarr)):
                            mballs.ballarr[i].setthruball(0)  
                    else:
                        for i in range(len(mballs.ballarr)):
                            mballs.ballarr[i].setthruball(1)
                elif self.poweruparr[i].getiden()==6:
                    if int(time.time()-self.poweruparr[i].time)<15:
                         if self.poweruparr[i].endtime==0:
                            self.poweruparr[i].fireendtime()
                            for i in range(len(mballs.ballarr)):
                                mballs.ballarr[i].increasespeed()  
                    else:
                        if self.poweruparr[i].fire==0:
                        #paddl.increasepadllength()
                            for i in range(len(mballs.ballarr)):
                                mballs.ballarr[i].resetdefaultspeed()
                            self.poweruparr[i].setfire()
                #self.poweruparr.pop(i)
                else:
                    if int(time.time()-self.poweruparr[i].time)<15:
                         if self.poweruparr[i].endtime==0:
                            self.poweruparr[i].fireendtime()
                            paddl.setcannon(1)
                            # for i in range(len(mballs.ballarr)):
                            #     mballs.ballarr[i].increasespeed()  
                    else:
                        if self.poweruparr[i].fire==0:
                        #paddl.increasepadllength()
                            paddl.setcannon(0)
                            # for i in range(len(mballs.ballarr)):
                            #     mballs.ballarr[i].resetdefaultspeed()
                            self.poweruparr[i].setfire()
                #self.poweruparr.pop(i)
        return paddl,mballs
    def updateallpos(self,tdarr):
        for i in range(len(self.poweruparr)):
            tdarr=self.poweruparr[i].updatepos(tdarr)
        return tdarr
    




    



        

    