class airdrop:
    def __init__(self):
        self.__cntr = 0
        self.__xpos = 0
        self.__ypos = 1
        self.__droparray = []
        self.prev = ''
        self.yprev = ''
        self.startflag = 0
        self.__char = 'V'
    def setxpos(self,val):
        self.__xpos = val
    def setypos(self):
        self.__ypos = self.__ypos + 1 
    def getxpos(self):
        return self.__xpos
    def getypos(self):
        return self.__ypos
    def getchar(self):
        return self.__char
    def getstartflag(self):
        return self.startflag
    def setstartflag(self,val):
        self.startflag = val
    def getyprev(self):
        return self.yprev
    def setyprev(self,val):
        self.yprev = val
    def setprev(self,val):
        self.prev = val
    def getprev(self):
        return self.prev
class bossenemy:
    def __init__(self):
        self.__cntr = 0
        self.__resid = 1
        self.__len = 3
        self.__var = 2
        self.__cntr = 3
        self.__droparray = []
        self.__itr = 0
        self.__health = 7
        self.__chance = 2
        self.__createcoverflag = 0
        self.__coverbrickstrenght = 5
        self.removeflag = 0
    def setcntr(self,val):
        self.__cntr = val
    def getcntr(self):
        return self.__cntr 
    def initializeboss(self,tdarr):
        self.__var = 2
        self.__cntr = 3
        self.__droparray = []
        self.__itr = 0
        self.__health = 7
        self.__chance = 2
        self.__createcoverflag = 0
        self.__coverbrickstrenght = 5
        self.__removeflag = 0
        strin = ''
        for i in range(0,self.__var):

            if tdarr[1][i]=='J':
                strin+=' '
            else:
                strin+=tdarr[1][i]
        for i in range(self.__var,self.__var+self.__len):
                strin+='J'
        for i in range(self.__var+self.__len,150):
            if tdarr[1][i]=='J':
                strin+=' '
            else:
                strin+=tdarr[1][i]
        tdarr[1]=strin
        print("strin = ",len(tdarr[2]))
        return tdarr
    def moveright(self,tdarr):
        if self.removeflag==1:
            return tdarr
        strin = tdarr[1]
        if(self.__var<=142):
            strin = ''
            var = 0
            self.__var+=2
            var2 = self.__var
            cntr2 = self.__cntr
            self.__cntr+=2
            self.__strin=("")
            for i in range(0,self.__var):
                if tdarr[1][i]=='J':
                    strin+=' '
                else:
                    strin+=tdarr[1][i]
                var = var + 1
            for i in range(self.__var,self.__var+self.__len):
                    strin+='J'
                    var = var + 1
            for i in range(self.__var+self.__len,150):
                if tdarr[1][i]=='J':
                    strin+=' '
                else:
                    strin+=tdarr[1][i]
                var = var + 1
            tdarr[1]=strin
            if self.__createcoverflag == 1:
                strin = ''
                var = 0
                # self.__var+=2
                # self.__cntr+=2
                self.__strin=("")
                for i in range(0,var2):
                    if tdarr[2][i]=='C':
                        strin+=' '
                    else:
                        strin+=tdarr[2][i]
                    var = var + 1
                for i in range(var2,var2+self.__len):
                        strin+='C'
                        var = var + 1
                for i in range(var2+self.__len,150):
                    if tdarr[2][i]=='C':
                        strin+=' '
                    else:
                        strin+=tdarr[2][i]
                    var = var + 1
                tdarr[2]=strin

        print("strin = ",len(tdarr[2]))
        return tdarr
    def createcover(self,tdarr):
        if self.removeflag == 1:
            return tdarr
        if self.__createcoverflag == 1:
            strin = ''
            for i in range(0,self.__var):
                if tdarr[2][i]=='c' or tdarr[2][i]=='o' or tdarr[2][i]=='@':
                    strin += ' '
                else:
                    strin+=tdarr[2][i]
            for i in range(self.__var,self.__var+self.__len):
                    strin+='C'
            for i in range(self.__var+self.__len,150):
                if tdarr[2][i]=='c' or tdarr[2][i]=='o' or tdarr[2][i]=='@':
                    strin += ' '
                else:
                    strin+=tdarr[2][i]
            tdarr[2]=strin
        return tdarr
            
                
                
    def moveleft(self,tdarr):
        if self.removeflag == 1:
            return tdarr
        strin = ''
        if(self.__var>=3):
            self.__var-=2
            self.__cntr-=2
            var2 = self.__var
            self.__strin=("")
            for i in range(0,self.__var):
                if tdarr[1][i]=='J':
                    strin+=' '
                else:
                    strin+=tdarr[1][i]
            for i in range(self.__var,self.__var+self.__len):
                    strin+=("J")
            for i in range(self.__var+self.__len,150):
                if tdarr[1][i]=='J':
                    strin+=' '
                else:
                    strin+=tdarr[1][i]
            tdarr[1]=strin
            if self.__createcoverflag == 1:
                strin = ''
                var = 0
                # self.__var-=2
                # self.__cntr-=2
                self.__strin=("")
                for i in range(0,var2):
                    if tdarr[2][i]=='C':
                        strin+=' '
                    else:
                        strin+=tdarr[2][i]
                    var = var + 1
                for i in range(var2,var2+self.__len):
                        strin+='C'
                        var = var + 1
                for i in range(var2+self.__len,150):
                    if tdarr[2][i]=='C':
                        strin+=' '
                    else:
                        strin+=tdarr[2][i]
                    var = var + 1
                tdarr[2]=strin
        return tdarr
    def decreasehealth(self):
        self.__health = self.__health - 1
        if self.__health == 3 and self.__createcoverflag==0:
            self.__createcoverflag = 1
        if self.__health == 2:
            self.__createcoverflag = 1
        if self.__health == 0:
            self.removeflag = 1

        # elif self.__health <=3 and self.__createcoverflag==1:
        #     if self.__coverbrickstrenght > 0:
        #         self.__coverbrickstrenght = self.__coverbrickstrength - 1
        #     elif if self.__coverbrickstrenght == 0:
        #         if self.


    def decreasecoverhealth(self):
        self.__coverbrickstrenght -=1  
    def getcoverhealth(self):
        return self.__coverbrickstrenght
    def gethealth(self):
        return self.__health 
    def createbomb(self):
        if self.removeflag == 1:
            return
        if self.__itr == 0:
            temp = airdrop()
            temp.setxpos(self.__cntr)
            temp.setstartflag(0)
            self.__droparray.append(temp)
        self.__itr = (self.__itr + 1)%200
    def updatebombpos(self,tdarr,paddl,brick):
        if self.removeflag == 1:
            return tdarr,paddl
        idtemp = brick.retrunidval()
        for i in range(len(self.__droparray)):
            y = self.__droparray[i].getypos()
            x = self.__droparray[i].getxpos()
            print("xup = ",x,"yup=",y,"tdarr[y]up=",tdarr[y])
            strin = ''
            tempr = ''
            print("iup=",i," startflag=",self.__droparray[i].getstartflag())
            if self.__droparray[i].getstartflag() == 0:
                for t in range(len(tdarr[y])):
                    if tdarr[y][t] == '@'or tdarr[y][t] == 'o' :
                        tempr += ' '
                    else:
                        if (tdarr[y][t]=='#' or tdarr[y][t]=='G' or tdarr[y][t]=='*') and idtemp[y][t]==0:
                            tempr+=' '
                        else:
                            tempr +=tdarr[y][t]
                print("inside o flag wala part")
                self.__droparray[i].setprev(tempr)
                self.__droparray[i].setyprev(y)
                print("y =",y)
                print("here y is",len(tdarr[y]))
                for j in range(150):
                    if j == x:
                        strin+=self.__droparray[i].getchar()
                    else:
                        strin+=tdarr[y][j]
                tdarr[y] = strin
                print("len strin is",len(strin))
                self.__droparray[i].setstartflag(1)
                
                self.__droparray[i].setyprev(y)
                self.__droparray[i].setypos()
            else:
                print("inside else")
                print("y is",y)
                print("tdarr =",len(tdarr[y]))
                tdarr[self.__droparray[i].getyprev()]= self.__droparray[i].getprev()
                print("here changed y is",len(tdarr[y]))
                strin = ''
                for j in range(150):
                    if j == x:
                        strin+=self.__droparray[i].getchar()
                    else:
                        strin+=tdarr[y][j]
                for t in range(len(tdarr[y])):
                    if tdarr[y][t] == '@'or tdarr[y][t] == 'o' :
                        tempr += ' '
                    else:
                        if (tdarr[y][t]=='#' or tdarr[y][t]=='G' or tdarr[y][t]=='*') and idtemp[y][t]==0 :
                            tempr+=' '
                        else:
                            tempr +=tdarr[y][t]
                
                self.__droparray[i].setprev(tempr)
                # self.__bulletarr[i].setprev(tdarr[y])
                print("ypos=",self.__droparray[i].getypos())
                if self.__droparray[i].getypos()==36:
                    #self.__droparray.pop(i)
                    a1 = paddl.getpadlcentr()
                    a2 = paddl.getpadlresid()
                    print("a1 =",a1," a2=",a2)
                    print("xcord=",self.__droparray[i].getxpos())
                    if ((self.__droparray[i].getxpos()>=(a1-a2)) and (self.__droparray[i].getxpos()<=(a1+a2))):
                        paddl.redpaddlehealth()
                    self.__droparray.pop(i)
                    return tdarr,paddl
                ynew = self.__droparray[i].getypos()
                xnew = self.__droparray[i].getxpos()
                removebrickflag = -1
                flag = 0
                print("ek baar len of strin=",len(strin))
                print("y=",y)

                tdarr[y]=strin
                self.__droparray[i].setyprev(y)
                self.__droparray[i].setypos()
                # for k in range(37):
                #     print("i=",i,"lenth=",len(tdarr[k]))
        return tdarr,paddl
    def checkballcollision(self,mballs,tdarr):
        if self.removeflag == 1:
            return mballs,tdarr
        for i in range(len(mballs.ballarr)):
            if mballs.ballarr[i].getypos()==2:
                if self.getcntr()-1<=mballs.ballarr[i].getxpos() and self.getcntr()+1>=mballs.ballarr[i].getxpos():
                    if mballs.ballarr[i].getyvel()<0:
                        mballs.ballarr[i].setyvel(1)
                        print("i am to decrease health")
                        self.decreasehealth()
            elif mballs.ballarr[i].getypos()==3:
                if self.__createcoverflag == 1:
                    if self.getcntr()-1<=mballs.ballarr[i].getxpos() and self.getcntr()+1>=mballs.ballarr[i].getxpos():
                        if mballs.ballarr[i].getyvel()<0:
                            self.decreasecoverhealth()
                            if (self.getcoverhealth()%3)==0:
                                self.__createcoverflag = 0
                                strin = ''
                                for t in range(0,self.__var):
                                    if tdarr[2][t]=='C':
                                        strin+=' '
                                    else:
                                        strin+=tdarr[2][t]
                                    # var = var + 1
                                for t in range(self.__var,self.__var+self.__len):
                                        strin+=' '
                                        # var = var + 1
                                for t in range(self.__var+self.__len,150):
                                    if tdarr[2][t]=='C':
                                        strin+=' '
                                    else:
                                        strin+=tdarr[2][t]
                                    # var = var + 1
                                tdarr[2]=strin
                                if self.removeflag == 1:
                                    for t in range(0,self.__var):
                                        if tdarr[1][t]=='J':
                                            strin+=' '
                                        else:
                                            strin+=tdarr[1][t]
                                    # var = var + 1
                                    for t in range(self.__var,self.__var+self.__len):
                                            strin+=' '
                                            # var = var + 1
                                    for t in range(self.__var+self.__len,150):
                                        if tdarr[1][t]=='J':
                                            strin+=' '
                                        else:
                                            strin+=tdarr[1][t]
                                        # var = var + 1
                                tdarr[1]=strin
                                    

                            mballs.ballarr[i].setyvel(1)


            print("checkball pos xpos xvel,yvel",mballs.ballarr[i].getxpos(),mballs.ballarr[i].getxvel(),mballs.ballarr[i].getyvel(),mballs.ballarr[i].getypos())
        return mballs,tdarr
