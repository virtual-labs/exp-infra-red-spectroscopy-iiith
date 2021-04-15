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
class brickarray():
    def __init__(self):
        self.arr = []
        self.copy = ''
        self.vis = []
        self.fin = []
        self.idarr = []
        self.__itr = 0
        self.__level = 0
        self.currentbricknumber = 16
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
        elif self.__level == 0:
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


    def createarr(self,tdarr):
        # self.__itr = self.__itr  + 1
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
        # print(Style.RESET_ALL)
            for i in range(37):
                strin = ""
                #print(Back.RED+"abc"+Style.RESET_ALL)
                for j in range(150):
                    if i==0 or i==36:
                        strin+='-'
                    elif j==0 or j==149:
                        strin+="|"
                    elif (i>=self.arr[0].getystart() and i<=self.arr[0].getyend()) and (j>=self.arr[0].getxstart() and j<=self.arr[0].getxend()):
                        print("checking this thing=",self.arr[0].getxstart(),self.arr[0].getxend(),self.arr[0].getystart(),self.arr[0].getyend())
                        strin+=(self.arr[0].getvalue())
                        self.idarr[i][j]=(self.arr[0].getid())
                        #print("before=",self.vis[i][j])
                        #self.vis[i][j]=1
                        #
                        #print("after=",self.vis[i][j])
                    elif (i>=self.arr[1].getystart() and i<=self.arr[1].getyend()) and (j>=self.arr[1].getxstart() and j<=self.arr[1].getxend()):
                        strin+=self.arr[1].getvalue()
                        print("checking this thing2=",self.arr[1].getxstart(),self.arr[1].getxend(),self.arr[1].getystart(),self.arr[1].getyend())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[1].getid()
                    elif (i>=self.arr[2].getystart() and i<=self.arr[2].getyend()) and (j>=self.arr[2].getxstart() and j<=self.arr[2].getxend()):
                        strin+=(self.arr[2].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[2].getid()
                    elif (i>=self.arr[3].getystart() and i<=self.arr[3].getyend()) and (j>=self.arr[3].getxstart() and j<=self.arr[3].getxend()):
                        print("checking here 3rd array=",self.arr[3].getxstart())
                        strin+=(self.arr[3].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[3].getid()
                    elif (i>=self.arr[4].getystart() and i<=self.arr[4].getyend()) and (j>=self.arr[4].getxstart() and j<=self.arr[4].getxend()):
                        strin+=(self.arr[4].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[4].getid()
                    elif (i>=self.arr[5].getystart() and i<=self.arr[5].getyend()) and (j>=self.arr[5].getxstart() and j<=self.arr[5].getxend()):
                        strin+=(self.arr[5].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[5].getid()
                    elif (i>=self.arr[6].getystart() and i<=self.arr[6].getyend()) and (j>=self.arr[6].getxstart() and j<=self.arr[6].getxend()):
                        strin+=(self.arr[6].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[6].getid()
                    elif (i>=self.arr[7].getystart() and i<=self.arr[7].getyend()) and (j>=self.arr[7].getxstart() and j<=self.arr[7].getxend()):
                        strin+=(self.arr[7].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[7].getid()
                    elif (i>=self.arr[8].getystart() and i<=self.arr[8].getyend()) and (j>=self.arr[8].getxstart() and j<=self.arr[8].getxend()):
                        strin+=(self.arr[8].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[8].getid()
                    elif (i>=self.arr[9].getystart() and i<=self.arr[9].getyend()) and (j>=self.arr[9].getxstart() and j<=self.arr[9].getxend()):
                        strin+=(self.arr[9].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[9].getid()
                    elif (i>=self.arr[10].getystart() and i<=self.arr[10].getyend()) and (j>=self.arr[10].getxstart() and j<=self.arr[10].getxend()):
                        strin+=(self.arr[10].getvalue())
                        #self.vis[i][j] = 1
                        self.idarr[i][j]=self.arr[10].getid()
                    elif (i>=self.arr[11].getystart() and i<=self.arr[11].getyend()) and (j>=self.arr[11].getxstart() and j<=self.arr[11].getxend()):
                        strin+=(self.arr[11].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[11].getid()
                    elif (i>=self.arr[12].getystart() and i<=self.arr[12].getyend()) and (j>=self.arr[12].getxstart() and j<=self.arr[12].getxend()):
                        strin+=(self.arr[12].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[12].getid()
                    elif (i>=self.arr[13].getystart() and i<=self.arr[13].getyend()) and (j>=self.arr[13].getxstart() and j<=self.arr[13].getxend()):
                        strin+=(self.arr[13].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[13].getid()
                    elif (i>=self.arr[14].getystart() and i<=self.arr[14].getyend()) and (j>=self.arr[14].getxstart() and j<=self.arr[14].getxend()):
                        strin+=(self.arr[14].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[14].getid()
                    elif (i>=self.arr[15].getystart() and i<=self.arr[15].getyend()) and (j>=self.arr[15].getxstart() and j<=self.arr[15].getxend()):
                        strin+=(self.arr[15].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[15].getid()
                    else:
                        strin+=" "
                self.copy.append(strin)
                print("checking this itr flag:(",self.__itr)
            return self.copy
        elif self.__level == 0:  

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
        # print(Style.RESET_ALL)
            for i in range(37):
                strin = ""
                #print(Back.RED+"abc"+Style.RESET_ALL)
                for j in range(150):
                    if i==0 or i==36:
                        strin+='-'
                    elif j==0 or j==149:
                        strin+="|"
                    elif (i>=self.arr[0].getystart() and i<=self.arr[0].getyend()) and (j>=self.arr[0].getxstart() and j<=self.arr[0].getxend()):
                        
                        strin+=(self.arr[0].getvalue())
                        self.idarr[i][j]=(self.arr[0].getid())
                        #print("before=",self.vis[i][j])
                        #self.vis[i][j]=1
                        #
                        #print("after=",self.vis[i][j])
                    elif (i>=self.arr[1].getystart() and i<=self.arr[1].getyend()) and (j>=self.arr[1].getxstart() and j<=self.arr[1].getxend()):
                        strin+=self.arr[1].getvalue()
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[1].getid()
                    elif (i>=self.arr[2].getystart() and i<=self.arr[2].getyend()) and (j>=self.arr[2].getxstart() and j<=self.arr[2].getxend()):
                        strin+=(self.arr[2].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[2].getid()
                    elif (i>=self.arr[3].getystart() and i<=self.arr[3].getyend()) and (j>=self.arr[3].getxstart() and j<=self.arr[3].getxend()):
                        strin+=(self.arr[3].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[3].getid()
                    elif (i>=self.arr[4].getystart() and i<=self.arr[4].getyend()) and (j>=self.arr[4].getxstart() and j<=self.arr[4].getxend()):
                        strin+=(self.arr[4].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[4].getid()
                    # elif (i>=12 and i<=13) and (j>=50 and j<=55):
                    #     strin+=(self.arr[12].getvalue())
                    #     #self.vis[i][j]=1
                    #     self.idarr[i][j]=self.arr[12].getid()
                    elif (i>=self.arr[5].getystart() and i<=self.arr[5].getyend()) and (j>=self.arr[5].getxstart() and j<=self.arr[5].getxend()):
                        strin+=(self.arr[5].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[5].getid()
                    elif (i>=self.arr[6].getystart() and i<=self.arr[6].getyend()) and (j>=self.arr[6].getxstart() and j<=self.arr[6].getxend()):
                        strin+=(self.arr[6].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[6].getid()
                    elif (i>=self.arr[7].getystart() and i<=self.arr[7].getyend()) and (j>=self.arr[7].getxstart() and j<=self.arr[7].getxend()):
                        strin+=(self.arr[7].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[7].getid()
                    elif (i>=self.arr[8].getystart() and i<=self.arr[8].getyend()) and (j>=self.arr[8].getxstart() and j<=self.arr[8].getxend()):
                        strin+=(self.arr[8].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[8].getid()
                    elif (i>=self.arr[9].getystart() and i<=self.arr[9].getyend()) and (j>=self.arr[9].getxstart() and j<=self.arr[9].getxend()):
                        strin+=(self.arr[9].getvalue())
                        #self.vis[i][j] = 1
                        self.idarr[i][j]=self.arr[9].getid()
                    elif (i>=self.arr[10].getystart() and i<=self.arr[10].getyend()) and (j>=self.arr[10].getxstart() and j<=self.arr[10].getxend()):
                        strin+=(self.arr[10].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[10].getid()
                    elif (i>=self.arr[11].getystart() and i<=self.arr[11].getyend()) and (j>=self.arr[11].getxstart() and j<=self.arr[11].getxend()):
                        strin+=(self.arr[11].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[11].getid()
                    elif (i>=self.arr[12].getystart() and i<=self.arr[12].getyend()) and (j>=self.arr[12].getxstart() and j<=self.arr[12].getxend()):
                        strin+=(self.arr[12].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[12].getid()
                    elif (i>=self.arr[13].getystart() and i<=self.arr[13].getyend()) and (j>=self.arr[13].getxstart() and j<=self.arr[13].getxend()):
                        strin+=(self.arr[13].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[13].getid()
                    elif (i>=self.arr[14].getystart() and i<=self.arr[14].getyend()) and (j>=self.arr[14].getxstart() and j<=self.arr[14].getxend()):
                        strin+=(self.arr[14].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[14].getid()
                    elif (i>=self.arr[15].getystart() and i<=self.arr[15].getyend()) and (j>=self.arr[15].getxstart() and j<=self.arr[15].getxend()):
                        strin+=(self.arr[15].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[15].getid()
                    else:
                        strin+=" "
                self.copy.append(strin)
            # print("checking visited")
            # for i in range(37):
            #     for j in range(150):
            #         print(self.vis[i][j],end='')
            #     print()
            # print("checking idarr")
            # for i in range(37):
            #     for j in range(150):
            #         print(self.idarr[i][j],end='')
            #     print()
            return self.copy
        else:
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
        # print(Style.RESET_ALL)
            for i in range(37):
                strin = ""
                #print(Back.RED+"abc"+Style.RESET_ALL)
                for j in range(150):
                    if i==0 or i==36:
                        strin+='-'
                    elif j==0 or j==149:
                        strin+="|"
                    elif (i>=10 and i<=11) and (j>=52 and j<=53):
                        
                        strin+=(self.arr[0].getvalue())
                        self.idarr[i][j]=(self.arr[0].getid())
                        #print("before=",self.vis[i][j])
                        #self.vis[i][j]=1
                        #
                        #print("after=",self.vis[i][j])
                    elif (i>=12 and i<=13) and (j>=44 and j<=45):
                        strin+=self.arr[1].getvalue()
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[1].getid()
                    elif (i>=10 and i<=11) and (j>=54 and j<=55):
                        strin+=(self.arr[2].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[2].getid()
                    elif (i>=12 and i<=17) and (j>=56 and j<=57):
                        strin+=(self.arr[3].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[3].getid()
                    elif (i>=12 and i<=13) and (j>=48 and j<=49):
                        strin+=(self.arr[4].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[4].getid()
                    elif (i>=12 and i<=13) and (j>=50 and j<=55):
                        strin+=(self.arr[12].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[12].getid()
                    elif (i>=14 and i<=15) and (j>=42 and j<=43):
                        strin+=(self.arr[5].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[5].getid()
                    elif (i>=14 and i<=15) and (j>=44 and j<=45):
                        strin+=(self.arr[6].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[6].getid()
                    elif (i>=14 and i<=15) and (j>=46 and j<=48):
                        strin+=(self.arr[7].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[7].getid()
                    elif (i>=16 and i<=17) and (j>=42 and j<=43):
                        strin+=(self.arr[8].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[8].getid()
                    elif (i>=16 and i<=17) and (j>=44 and j<=46):
                        strin+=(self.arr[9].getvalue())
                        #self.vis[i][j] = 1
                        self.idarr[i][j]=self.arr[9].getid()
                    elif (i>=16 and i<=17) and (j>=47 and j<=48):
                        strin+=(self.arr[10].getvalue())
                        #self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[10].getid()
                    elif (i>=16 and i<=17) and (j>=49 and j<=50):
                        strin+=(self.arr[11].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[11].getid()
                    elif (i>=12 and i<=13) and (j>=50 and j<=55):
                        strin+=(self.arr[12].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[12].getid()
                    elif (i>=12 and i<=13) and (j>=38 and j<=39):
                        strin+=(self.arr[13].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[13].getid()
                    elif (i>=12 and i<=13) and (j>=36 and j<=37):
                        strin+=(self.arr[14].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[14].getid()
                    elif (i>=14 and i<=15) and (j>=40 and j<=41):
                        strin+=(self.arr[15].getvalue())
                    # self.vis[i][j]=1
                        self.idarr[i][j]=self.arr[15].getid()
                    else:
                        strin+=" "
                self.copy.append(strin)
                print("checking this itr flag:(",self.__itr)
            return self.copy
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
                    

        # if self.idarr[yexp][xexp] != 0:
        #     val = self.idarr[yexp][xexp]
        #     for i in range(len(self.arr)):
        #         if self.arr[i].getid()==val:
        #             xcomprs,xcompre,ycomprs,ycompre = self.arr[i].getcomps()
        #             if abs(xpos-xcompre)<abs(xpos-xcomprs):
        #                 reflx = xcompre
        #             else:
        #                 reflx = xcomprs
        #             if abs(ypos-ycompre)<abs(ypos-ycomprs):
        #                 refly = ycompre
        #             else:
        #                 refly = ycomprs
        #             if xvel!=0:
        #                 tx= float(reflx/xvel)
        #             if yvel!=0:
        #                 ty = float(refly/yvel)
        #             if ty < tx:
        #                 yvel = -1*yvel
        #             else:
        #                 xvel = -1*xvel
        #             print("i am here pringint",xcomprs,xcompre,ycomprs,ycompre)
        #             chk = self.arr[i].setcolofvalue()
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



    
        