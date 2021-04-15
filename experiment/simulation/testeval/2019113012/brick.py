from colorama import Fore, Back, Style
import random
class brick:
    def __init__(self):
        self.__strength = 5
        self.__color = ""
        self.__bricklength = 0
        self.__brickwidth = 0
        self.__isbreakable = 0
        self.__isglass = 0
        self.__xstart = 0
        self.__xend = 0
        self.__ystart = 0
        self.__yend = 0
        self.__char = ''
        self.__colorarr = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        self.__id = 0
        self.__level = 0
    
class strongbrick(brick):
    def setvalues(self,xstart,xend,ystart,yend,val):
        self.__xstart = xstart
        self.__xend = xend
        self.__ystart = ystart
        self.__yend = yend
        self.__strength = 3
        self.__charac = '#'
        self.__color = Back.GREEN
        self.__id = 1
        self.__isglass=0
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        self.__itr = 0
        self.__israinbow = 0
    def getvalue(self):
        return self.__charac
    def getid(self):
        return self.__bid
    def getcolor(self):
        return self.__color
    def getcomps(self):
        return self.__xstart,self.__xend,self.__ystart,self.__yend
    def setcolofvalue(self,thru):
        var = (self.__itr + 1)%3
        self.__color=self.__arraycolor[var]
        self.__itr = var
        if thru==1:
            self.__strength = 0
        else:
            self.__strength = self.__strength-1
        if self.__strength==0:
            return 1
        else:
            return 0
    def checkglass(self):
        return self.__isglass
    def getxstart(self):
        return self.__xstart
    def getxend(self):
        return self.__xend
    def getystart(self):
        return self.__ystart
    def getyend(self):
        return self.__yend
    def increaseyecord(self):
        self.__ystart = self.__ystart+1
        self.__yend = self.__yend + 1
    def getcharac(self):
        return self.__charac
    def getrainbowflag(self):
        return self.__israinbow

class rainbowbrick(brick):
    def setvalues(self,xstart,xend,ystart,yend,val):
        self.__xstart = xstart
        self.__xend = xend
        self.__ystart = ystart
        self.__yend = yend
        self.__strength = 3
        self.__charac = 'R'
        self.__color = Back.GREEN
        self.__id = 4
        self.__isglass=0
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        self.__itr = 0
        self.__rainbowitr = 0
        self.__israinbow  = 1
        self.__stoprainbow = 0
    def getvalue(self):
        return self.__charac
    def getid(self):
        return self.__bid
    def getcolor(self):
        return self.__color
    def getcomps(self):
        return self.__xstart,self.__xend,self.__ystart,self.__yend
    def setcolofvalue(self,thru):
        var = (self.__itr + 1)%3
        self.__stoprainbow = 1
        self.__color=self.__arraycolor[var]
        self.__itr = var
        if thru==1:
            self.__strength = 0
        else:
            self.__strength = self.__strength-1
        if self.__strength==0:
            return 1
        else:
            return 0
    def rainbowchangecolor(self):
        if self.__stoprainbow == 0:
            var = (self.__rainbowitr + 1)%3
            self.__rainbowitr = self.__rainbowitr + 1
            print("inside rainbowchange color,var=",var)
            self.__color = self.__arraycolor[var]

    def checkglass(self):
        return self.__isglass
    def getxstart(self):
        return self.__xstart
    def getxend(self):
        return self.__xend
    def getystart(self):
        return self.__ystart
    def getyend(self):
        return self.__yend
    def increaseyecord(self):
        self.__ystart = self.__ystart+1
        self.__yend = self.__yend + 1
    def getcharac(self):
        return self.__charac
    def getrainbowflag(self):
        return self.__israinbow
class unbreakablebrick(brick):
    def setvalues(self,xstart,xend,ystart,yend,val):
        self.__xstart = xstart
        self.__xend = xend
        self.__ystart = ystart
        self.__yend = yend
        self.__strength = -1
        self.__charac = '*'
        self.__isglass=0
        self.__color = Back.MAGENTA
        self.__id = 2
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        self.__itr = 0
        self.__israinbow = 0

    def getvalue(self):
        return self.__charac
    def getid(self):
        return self.__bid
    def getcolor(self):
        return self.__color
    def getcomps(self):
        return self.__xstart,self.__xend,self.__ystart,self.__yend
    def setcolofvalue(self,thru):
        var = (self.__itr + 1)%3
        self.__color=self.__arraycolor[var]
        self.__itr = var
        if thru==1:
            self.__strength = 0
        else:
            self.__strength = self.__strength-1
        if self.__strength == 0:
            return 1
        else:
            return 0
    def checkglass(self):
        return self.__isglass
    def getxstart(self):
        return self.__xstart
    def getxend(self):
        return self.__xend
    def getystart(self):
        return self.__ystart
    def getyend(self):
        return self.__yend
    def increaseyecord(self):
        self.__ystart = self.__ystart+1
        self.__yend = self.__yend + 1
    def getcharac(self):
        return self.__charac
    def getrainbowflag(self):
        return self.__israinbow
class glassbrick(brick):
    def setvalues(self,xstart,xend,ystart,yend,val):
        self.__xstart = xstart
        self.__xend = xend
        self.__ystart = ystart
        self.__yend = yend
        self.__strength = 1
        self.__color = Back.YELLOW
        self.__isglass = 1
        self.__charac = 'G'
        self.__id = 3
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        self.__itr=0
        self.__israinbow=0
    def getvalue(self):
        return self.__charac
    def getid(self):
        return self.__bid
    def getcolor(self):
        return self.__color
    def getcomps(self):
        return self.__xstart,self.__xend,self.__ystart,self.__yend
    def setcolofvalue(self,thru):
        var = (self.__itr + 1)%3
        self.__color=self.__arraycolor[var]
        self.__itr = var
        if thru == 1:
            self.__strength = 0
        else:
            self.__strength = self.__strength-1
        if self.__strength == 0:
            return 1
        else:
            return 0
    def checkglass(self):
        return self.__isglass
    def getxstart(self):
        return self.__xstart
    def getxend(self):
        return self.__xend
    def getystart(self):
        return self.__ystart
    def getyend(self):
        return self.__yend
    def increaseyecord(self):
        self.__ystart = self.__ystart+1
        self.__yend = self.__yend + 1
    def getcharac(self):
        return self.__charac
    def getrainbowflag(self):
        return self.__israinbow
class brickarray():
    def __init__(self):
        self.arr = []
        self.copy = ''
        self.vis = []
        self.fin = []
        self.idarr = []
        self.__itr = 0
        self.__movebrickflag = 0
        self.__level = 0
        self.currentbricknumber = 16
        self.movebricktime = 4
        self.minimum1 = 0
    def movebrickdown(self,tdarr,timeer,flg):
        self.minimum1 = 0
        if timeer > 3 and flg==1:
            print("inside movebrick down")
            print("idarray")
            for i in range(37):
                for j in range(150):
                    print(self.idarr[i][j],end="")
                print('\n')

            for i in range(35):
                flag = 0
                flagstart = 0 
                startindx = 0
                endindx = 0
                flagend = 0
                strin1 = ''
                strin2 = ''
                for j in range(150):
                    if self.idarr[i][j] != 0:
                        if flagstart == 0:
                            startindx = j
                            flagstart = 1
                        flag = 1
                        endindx = j
                if flag == 1:
                    print("starindx=",startindx,"endindx=",endindx,"i=",i)
                    for j in range(150):
                        if j>=startindx and j<=endindx:
                            strin1+=" "
                            strin2+=tdarr[i][j]
                        else:
                            strin1+=tdarr[i][j]
                            strin2+=tdarr[i+1][j]
                    print("strin1=",strin1)
                    print("strin2=",strin2)
                    tdarr[i+1] = strin2
                    tdarr[i]=strin1
                    # tdarr[i] = strin2

            tempr = []
            for j in range(37):
                tocreate = ""
                for i in range(150):
                    tocreate+=' '
                tempr.append(tocreate)
                    

            for i in range(35,1,-1):
                for j in range(150):
                    self.idarr[i][j]=self.idarr[i-1][j]

            for i in range(17):
                print("Inside the increase ycord")
                self.arr[i].increaseyecord()
            
            
            returnarray = []
            for i in range(37):
                strin=''
                flag = 0
                char = ' '
                for j in range(150):
                    flag = 0
                    for k in range(17):
                        if i>=self.arr[k].getystart() and i<=self.arr[k].getyend() and j>=self.arr[k].getxstart() and j<=self.arr[k].getxend():
                            flag = 1
                            if self.idarr[i][j] != 0:
                                char = self.arr[k].getcharac()
                            print("index at this point = ",self.idarr[i][j])
                            break
                    if flag==1:
                        strin+=char
                    else:
                        strin+=tdarr[i][j]
                returnarray.append(strin)
            print("checkign the tdarr")
            minimumz = 0
            print("above minimumz=",minimumz)
            for i in range(37):
                for j in range(150):
                    #print("inside the loopwr")
                    if self.idarr[i][j]!=0:
                        if i > minimumz:
                            minimumz = i
            print("minimumz=",minimumz)
            if minimumz >= 34:
                print("minimumz=",minimumz)
                self.minimum1 = 1
            print("Minimum1=",self.minimum1)
            return returnarray
        return tdarr
    def getminimum1(self):
        return self.minimum1
    def getlevel(self):
        return self.__level
    def initializebricks(self):
        if self.__level == 1:
            
            br1 = unbreakablebrick()
            br2 = strongbrick()
            br3 = glassbrick()
            br4 = unbreakablebrick()
            br5 = strongbrick()
            br6 = glassbrick()
            br7 = unbreakablebrick()
            br8 = strongbrick()
            br9 = glassbrick()
            br10 = unbreakablebrick()
            br11 = strongbrick()
            br12 = glassbrick()
            br13 = strongbrick()
            br14 = glassbrick()
            br15 = glassbrick()
            br16 = strongbrick()
            br17 = rainbowbrick()
            br1.setvalues(52,53,10,11,1)
            br2.setvalues(44,45,12,13,2)
            br3.setvalues(54,55,10,11,3)
            br4.setvalues(56,57,12,17,4)
            br5.setvalues(48,49,12,13,5)
            br6.setvalues(42,43,14,15,6)
            br7.setvalues(44,45,14,15,7)
            br8.setvalues(46,48,14,15,8)
            br9.setvalues(42,43,16,17,9)
            br10.setvalues(44,46,16,17,10)
            br11.setvalues(47,48,16,17,11)
            br12.setvalues(49,50,16,17,12)
            br13.setvalues(50,55,12,13,13)
            br14.setvalues(38,39,12,13,14)
            br15.setvalues(36,37,12,13,15)
            br16.setvalues(40,41,14,15,16)
            br17.setvalues(58,59,10,11,17)
            self.arr=[]
            self.arr.append(br1)
            self.arr.append(br2)
            self.arr.append(br3)
            self.arr.append(br4)
            self.arr.append(br5)
            self.arr.append(br6)
            self.arr.append(br7)
            self.arr.append(br8)
            self.arr.append(br9)
            self.arr.append(br10)
            self.arr.append(br11)
            self.arr.append(br12)
            self.arr.append(br13)
            self.arr.append(br14)
            self.arr.append(br15)
            self.arr.append(br16)
            self.arr.append(br17)
        elif self.__level == 0:
            print("movebrick flag = ",self.__movebrickflag)
            br1 = unbreakablebrick()
            br2 = strongbrick()
            br3 = glassbrick()
            br4 = unbreakablebrick()
            br5 = strongbrick()
            br6 = glassbrick()
            br7 = unbreakablebrick()
            br8 = strongbrick()
            br9 = glassbrick()
            br10 = unbreakablebrick()
            br11 = strongbrick()
            br12 = glassbrick()
            br13 = strongbrick()
            br14 = glassbrick()
            br15 = glassbrick()
            br16 = glassbrick()
            br17 = rainbowbrick()
            br1.setvalues(42,43,10,11,1)
            br2.setvalues(44,45,10,11,2)
            br3.setvalues(40,41,12,13,3)
            br4.setvalues(42,47,12,13,4)
            br5.setvalues(48,49,12,13,5)
            br6.setvalues(42,43,14,15,6)
            br7.setvalues(44,45,14,15,7)
            br8.setvalues(46,48,14,15,8)
            br9.setvalues(42,43,16,17,9)
            br10.setvalues(44,46,16,17,10)
            br11.setvalues(47,48,16,17,11)
            br12.setvalues(49,50,16,17,12)
            br13.setvalues(50,55,12,13,13)
            br14.setvalues(38,39,12,13,14)
            br15.setvalues(36,37,12,13,15)
            br16.setvalues(40,41,14,15,16)
            br17.setvalues(46,49,10,11,17)
            self.arr=[]
            self.arr.append(br1)
            self.arr.append(br2)
            self.arr.append(br3)
            self.arr.append(br4)
            self.arr.append(br5)
            self.arr.append(br6)
            self.arr.append(br7)
            self.arr.append(br8)
            self.arr.append(br9)
            self.arr.append(br10)
            self.arr.append(br11)
            self.arr.append(br12)
            self.arr.append(br13)
            self.arr.append(br14)
            self.arr.append(br15)
            self.arr.append(br16)
            self.arr.append(br17)
        elif self.__level == 2:
            br1 = unbreakablebrick()
            br2 = strongbrick()
            br3 = glassbrick()
            br4 = unbreakablebrick()
            br5 = strongbrick()
            br6 = glassbrick()
            br7 = unbreakablebrick()
            br8 = strongbrick()
            br9 = glassbrick()
            br10 = unbreakablebrick()
            br11 = strongbrick()
            br12 = glassbrick()
            br13 = strongbrick()
            br14 = glassbrick()
            br15 = glassbrick()
            br16 = strongbrick()
            br17 = rainbowbrick()
            br1.setvalues(52,53,10,11,1)
            br2.setvalues(44,45,12,13,2)
            br3.setvalues(54,55,10,11,3)
            br4.setvalues(56,57,12,17,4)
            br5.setvalues(48,49,12,13,5)
            br6.setvalues(42,43,14,15,6)
            br7.setvalues(44,45,14,15,7)
            br8.setvalues(46,48,14,15,8)
            br9.setvalues(42,43,16,17,9)
            br10.setvalues(44,46,16,17,10)
            br11.setvalues(47,48,16,17,11)
            br12.setvalues(49,50,16,17,12)
            br13.setvalues(50,55,12,13,13)
            br14.setvalues(38,39,12,13,14)
            br15.setvalues(36,37,12,13,15)
            br16.setvalues(40,41,14,15,16)
            br17.setvalues(58,59,10,11,17)
            self.arr=[]
            self.arr.append(br1)
            self.arr.append(br2)
            self.arr.append(br3)
            self.arr.append(br4)
            self.arr.append(br5)
            self.arr.append(br6)
            self.arr.append(br7)
            self.arr.append(br8)
            self.arr.append(br9)
            self.arr.append(br10)
            self.arr.append(br11)
            self.arr.append(br12)
            self.arr.append(br13)
            self.arr.append(br14)
            self.arr.append(br15)
            self.arr.append(br16)
            self.arr.append(br17)


    def createarr(self,tdarr):
        # self.__itr = self.__itr  + 1
        if self.__level == 1:
            self.initializebricks()
            self.idarr = []
            self.vis = []
            self.fin = []
            self.copy = []
            ans = []
            for i in range(37):
                temp = []
                for j in range(150):
                    temp.append(0)
                self.vis.append(temp)
                self.idarr.append(temp)
            # print("Initial vis=")
            # for i in range(37):
            #     for j in range(150):
            #         print(self.vis[i][j],end='')
            #     print()
            #self.arr.append(a1)
            #self.arr.append(a2)
            strin = ""
            for i in range(37):
                strin=''
                flag = 0
                char = ' '
                for j in range(150):
                    flag = 0
                    for k in range(17):
                        if i>=self.arr[k].getystart() and i<=self.arr[k].getyend() and j>=self.arr[k].getxstart() and j<=self.arr[k].getxend():
                            flag = 1
                            char = self.arr[k].getcharac()
                            self.idarr[i][j] = self.arr[k].getid()
                            # print("index at this point = ",self.idarr[i][j])
                            break
                    if flag==1:
                        strin+=char
                    else:
                        strin+=tdarr[i][j]
                self.copy.append(strin)
                print("checking this itr flag:(",self.__itr)
                #self.__movebrickflag = 1
            return self.copy
        elif self.__level == 0:  
            self.initializebricks()
            self.idarr = []
            self.vis = []
            self.fin = []
            self.copy = []
            ans = []
            for i in range(37):
                temp = []
                for j in range(150):
                    temp.append(0)
                self.vis.append(temp)
                self.idarr.append(temp)
            
            # print("Initial vis=")
            # for i in range(37):
            #     for j in range(150):
            #         print(self.vis[i][j],end='')
            #     print()
            #self.arr.append(a1)
            #self.arr.append(a2)
            strin = ""
            for i in range(37):
                strin=''
                flag = 0
                char = ' '
                for j in range(150):
                    flag = 0
                    for k in range(17):
                        if i>=self.arr[k].getystart() and i<=self.arr[k].getyend() and j>=self.arr[k].getxstart() and j<=self.arr[k].getxend():
                            flag = 1
                            char = self.arr[k].getcharac()
                            self.idarr[i][j] = self.arr[k].getid()
                            # print("index at this point = ",self.idarr[i][j])
                            break
                    if flag==1:
                        strin+=char
                    else:
                        strin+=tdarr[i][j]
                self.copy.append(strin)
            return self.copy
        elif self.__level == 2:  
            self.initializebricks()
            self.idarr = []
            self.vis = []
            self.fin = []
            self.copy = []
            ans = []
            for i in range(37):
                temp = []
                for j in range(150):
                    temp.append(0)
                self.vis.append(temp)
                self.idarr.append(temp)
            
            # print("Initial vis=")
            # for i in range(37):
            #     for j in range(150):
            #         print(self.vis[i][j],end='')
            #     print()
            #self.arr.append(a1)
            #self.arr.append(a2)
            strin = ""
            for i in range(37):
                strin=''
                flag = 0
                char = ' '
                for j in range(150):
                    flag = 0
                    for k in range(17):
                        if i>=self.arr[k].getystart() and i<=self.arr[k].getyend() and j>=self.arr[k].getxstart() and j<=self.arr[k].getxend():
                            flag = 1
                            char = self.arr[k].getcharac()
                            self.idarr[i][j] = self.arr[k].getid()
                            # print("index at this point = ",self.idarr[i][j])
                            break
                    if flag==1:
                        strin+=char
                    else:
                        strin+=tdarr[i][j]
                self.copy.append(strin)
            return self.copy
    def changerainbowcolor(self):
        for j in range(len(self.arr)):
            if self.arr[j].getrainbowflag()==1:
                print("indside the rainbowflat part")
                self.arr[j].rainbowchangecolor()
    def returnvis(self):
        return self.vis
    def increaselevel(self):
        self.__level = self.__level + 1
    def retrunidval(self):
        return self.idarr
    def getarray(self):
        return self.arr
    def getcopy(self):
        return self.copy
    def setnewbricknumber(self,val):
        self.currentbricknumber = self.currentbricknumber - val
        print("new brick number = ",self.currentbricknumber)
    def getcurrentbrick(self):
        return self.currentbricknumber
    def checkcollisionbrick(self,xvel,yvel,xpos,ypos,thruball):
        xexp = xpos + xvel
        yexp = ypos + yvel
        if xexp >=150 or xexp<1 or yexp >34 or yexp<0:
           return xvel,yvel,-1
        tx = 100000
        ty = 100000
        targetx = (xpos + xpos + xvel)/2
        flag = 0
        iden = -1
        if xvel >= 0 and yvel < 0:
            for i in range(xpos,int(min(149,targetx+1))):
                if self.idarr[ypos-1][i]!=0:
                    val = self.idarr[ypos-1][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                #print("i am here")
                                if flag==0:
                                    #print("and i am here")
                                    #print("yvel before=",yvel)
                                    if thruball==0:
                                        yvel = -1*yvel
                                    #print("yvel after=",yvel)
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    #print("and chk = ",iden)
                                    if chk ==1:
                                        iden = val
                                        #print("and iden = ",iden)
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos][i+1]!=0:
                    val = self.idarr[ypos][i+1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag==0 and xvel!=0:
                                    if thruball==0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
            for i in range(int(min(149,targetx+1)),int(min(149,xpos+xvel+1))):
                if self.idarr[ypos-2][i]!=0:
                    val = self.idarr[ypos-2][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag==0:
                                    if thruball==0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos-1][i+1]!=0:
                    val = self.idarr[ypos-1][i+1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag==0 and xvel!=0:
                                    if thruball==0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
        
        elif xvel < 0 and yvel < 0:
            for i in range(xpos,int(max(0,targetx-1)),-1):
                if self.idarr[ypos-1][i]!=0:
                    val = self.idarr[ypos-1][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag==0:
                                    if thruball==0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos][i-1]!=0:
                    val = self.idarr[ypos][i-1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if (xpos-xcompre)==1:
                                if flag == 0:
                                    if thruball==0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
            for i in range(int(max(0,targetx+1)),int(max(0,xpos+xvel-1)),-1):
                if self.idarr[ypos-2][i]!=0:
                    val = self.idarr[ypos-2][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag == 0:
                                    if thruball==0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos-1][i-1]!=0:
                    val = self.idarr[ypos-1][i-1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag == 0 and xvel!=0:
                                    if thruball == 0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
        
        elif xvel >= 0 and yvel > 0:
            for i in range(xpos,int(min(149,targetx+1))):
                if self.idarr[ypos+1][i]!=0:
                    val = self.idarr[ypos+1][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag==0:
                                    if thruball==0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos][i+1]!=0:
                    val = self.idarr[ypos][i+1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag==0 and xvel!=0:
                                    if thruball == 0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
            for i in range(int(min(149,targetx+1)),int(min(xpos+xvel+1,149))):
                if self.idarr[ypos+2][i]!=0:
                    val = self.idarr[ypos+2][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag==0:
                                    if thruball == 0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos+1][i+1]!=0:
                    val = self.idarr[ypos+1][i+1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag==0 and xvel!=0:
                                    if thruball == 0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break

        elif xvel < 0 and yvel > 0:
            for i in range(xpos,int(max(0,targetx-1)),-1):
                if self.idarr[ypos+1][i]!=0:
                    val = self.idarr[ypos+1][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag ==0:
                                    if thruball == 0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos][i-1]!=0:
                    val = self.idarr[ypos][i-1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if (xpos-xcompre)==1:
                                if flag==0:
                                    if thruball == 0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
            for i in range(int(max(0,targetx+1)),int(max(0,xpos+xvel-1)),-1):
                if self.idarr[ypos+2][i]!=0:
                    val = self.idarr[ypos+2][i]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre:
                                if flag==0:
                                    if thruball == 0:
                                        yvel = -1*yvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                elif self.idarr[ypos+1][i-1]!=0:
                    val = self.idarr[ypos+1][i-1]
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==val:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1:
                                if flag==0 and xvel!=0:
                                    if thruball == 0:
                                        xvel = -1*xvel
                                    chk = self.arr[j].setcolofvalue(thruball)
                                    if chk ==1:
                                        iden = val
                                    flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break               
                    
        return xvel,yvel,iden
    def checkerglass(self,iden):
        for j in range(len(self.arr)):
            if self.arr[j].getid()==iden:
                return self.arr[j]

    def updateglassarr(self,arr,elem,vis):
        idx = 0
        que = []
        que.push(arr)
        while len(que)!=0:
            for i in range(len(que)):
                xcomprs,xcompre,ycomprs,ycompre = que[i].getcomps()
                for l in range(xcomprs,xcompre+1):
                                #print("x=",ycomprs-1," y=",l)
                    if self.idarr[ycomprs-1][l]!=0:
                        # vis[self.idarr[ycomprs-1][l]]=1
                        if checkglass(self.arr,self.idarr[ycomprs-1][l])==1:
                            if vis[self.idarr[ycomprs-1][l]]!=1:
                                que.push()

                                #print("x=",ycompre+1," y=",l)
                    if self.idarr[ycompre+1][l]!=0:
                        visit[self.idarr[ycompre+1][l]]=1
                for l in range(ycomprs,ycompre+1):
                                #print("x'=",l," y'=",xcompre+1)
                    if self.idarr[l][xcompre+1]!=0:
                        visit[self.idarr[l][xcompre+1]]=1
                    if self.idarr[l][xcomprs-1]!=0:
                        visit[self.idarr[l][xcomprs-1]]=1

    def removebrick(self,tdarr,iden):
        xstart=[]
        xend = []
        ystart = []
        yend = []
        visit = []
        counter = 0
        for i in range(20):
            visit.append(0)
        for j in range(len(self.arr)):
            if self.arr[j].getid()==iden:
                xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                # print("inside remove brick",xcomprs,xcompre,ycomprs,ycompre)
                for i in range(ycomprs,ycompre+1):
                    strin =""
                    for k in range(xcomprs):
                        strin+=tdarr[i][k]
                    for k in range(xcomprs,xcompre+1):
                        strin+=" "
                    for k in range(xcompre+1,150):
                        strin+=tdarr[i][k]
                    tdarr[i]=strin
                for l in range(ycomprs,ycompre+1):
                    for m in range(xcomprs,xcompre+1):
                        self.idarr[l][m]=0
                counter=counter+1
                print("counter=",counter)
                if self.arr[j].checkglass()==1:   
                    counter = counter - 1
                    que = []
                    que.append(self.arr[j])
    
                    while (len(que))!=0:
                        for t in range(len(que)):
                            xcomprs,xcompre,ycomprs,ycompre = que[t].getcomps()
                            for l in range(xcomprs,xcompre+1):
                                if self.idarr[ycomprs-1][l]!=0:
                                    varil = self.checkerglass(self.idarr[ycomprs-1][l])
                                    if varil.checkglass()==1:
                                        if visit[self.idarr[ycomprs-1][l]]!=1:
                                            visit[self.idarr[ycomprs-1][l]]=1
                                            que.append(varil)
                                    else:
                                        visit[self.idarr[ycomprs-1][l]]=1
                                if self.idarr[ycompre+1][l]!=0:
                                            #visit[self.idarr[ycompre+1][l]]=1
                                    varil = self.checkerglass(self.idarr[ycompre+1][l])
                                    if varil.checkglass()==1:
                                        if visit[self.idarr[ycompre+1][l]]!=1:
                                            visit[self.idarr[ycompre+1][l]]=1
                                            que.append(varil)
                                    else:
                                        visit[self.idarr[ycompre+1][l]]=1
                            for l in range(ycomprs,ycompre+1):
                                                #print("x'=",l," y'=",xcompre+1)
                                if self.idarr[l][xcompre+1]!=0:
                                            #visit[self.idarr[l][xcompre+1]]=1
                                    varil = self.checkerglass(self.idarr[l][xcompre+1])
                                    if varil.checkglass()==1:
                                        if visit[self.idarr[l][xcompre+1]]!=1:
                                            visit[self.idarr[l][xcompre+1]]=1
                                            que.append(varil)
                                    else:
                                        visit[self.idarr[l][xcompre+1]]=1
                                            
                                if self.idarr[l][xcomprs-1]!=0:
                                            # visit[self.idarr[l][xcomprs-1]]=1
                                    varil = self.checkerglass(self.idarr[l][xcomprs-1])
                                    if varil.checkglass()==1:
                                        if visit[self.idarr[l][xcomprs-1]]!=1:
                                            visit[self.idarr[l][xcomprs-1]]=1
                                            que.append(varil)
                                    else:
                                        visit[self.idarr[l][xcomprs-1]]=1
                        que.pop(0)
                        counter= counter+1
                    # for l in range(xcomprs,xcompre+1):
                    #     #print("x=",ycomprs-1," y=",l)
                    #     if self.idarr[ycomprs-1][l]!=0:
                    #         visit[self.idarr[ycomprs-1][l]]=1
                    #     #print("x=",ycompre+1," y=",l)
                    #     if self.idarr[ycompre+1][l]!=0:
                    #         visit[self.idarr[ycompre+1][l]]=1
                    # for l in range(ycomprs,ycompre+1):
                    #     #print("x'=",l," y'=",xcompre+1)
                    #     if self.idarr[l][xcompre+1]!=0:
                    #         visit[self.idarr[l][xcompre+1]]=1
                    #     if self.idarr[l][xcomprs-1]!=0:
                    #         visit[self.idarr[l][xcomprs-1]]=1
                    #     #print("x'=",l," y'=",xcomprs-1)        
        for i in range(20):
            #for i in range(15)
            if visit[i]!= 0:
                print("I=",i)
                for j in range(len(self.arr)):
                    if self.arr[j].getid() == i:
                        xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                        #print("break glass inside remove brick",xcomprs,xcompre,ycomprs,ycompre)
                        for t in range(ycomprs,ycompre+1):
                            strin =""
                            for k in range(xcomprs):
                                strin+=tdarr[t][k]
                            for k in range(xcomprs,xcompre+1):
                                strin+=" "
                            for k in range(xcompre+1,150):
                                strin+=tdarr[t][k]
                            tdarr[t]=strin
                            for l in range(ycomprs,ycompre+1):
                                for m in range(xcomprs,xcompre+1):
                                    self.idarr[l][m]=0




        # print("removed brick")
        # for j in range(37):
        #     print(tdarr[j])
        print("final counter value is=",counter)
        return tdarr,counter

    #def createbricks(self,tdarr):
     #   for
    # def createbullet(self,cntr,resid):



    
        