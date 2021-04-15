from colorama import Fore, Back, Style
class bullet:
    def __init__(self):
        self.__visflag = 0
        self.__xpos = 0
        self.__ypos = 34
        self.__yvel = -1
        self.__char = '@'
        self.prev = ''
        self.startflag = 0
        self.yprev = ''
    def setxpos(self,val):
        self.__xpos = val
    def setypos(self):
        self.__ypos = self.__ypos - 1
    def setstopflag(self,val):
        self.__visflag = val
    def getypos(self):
        return self.__ypos
    def getxpos(self):
        return self.__xpos
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
class paddl:
    def __init__(self):
        self.__strin=""
        self.__var = 1
        self.__txt = '='
        self.__cntr =3
        self.__len = 5
        self.__resid = 2
        self.__cannon = 0
        self.__paddlehealth = 4
        self.__activatepaddlarr = []
        self.__activategrabpaddle = 0
        self.__bulletarr = []
        for i in range(150):
            if i==0 or i==149:
                self.__strin+="|"
            elif i>=1 and i<=5:
                self.__strin+=("=")
    def __movright(self,arr):
        #print("lengthright=",self.__len)
        #print("length of activatepaddlarr = ",len(self.__activatepaddlarr))
        if(self.__var<=142):
            #for i in range(len(self.__activatepaddlarr)):
                #print("unupdated pos")
                #print(self.__activatepaddlarr[i].getxpos())
            self.__var+=2
            self.__cntr+=2
            for i in range(len(self.__activatepaddlarr)):
                self.__activatepaddlarr[i].setxypos(self.__activatepaddlarr[i].getxpos()+2,34)
            #for i in range(len(self.__activatepaddlarr)):
                #print("updated pos")
                #print(self.__activatepaddlarr[i].getxpos())
            
            self.__strin=("")
            for i in range(0,self.__var):
                if i==0:
                    self.__strin+="|"
                else:
                    self.__strin+=" "
            for i in range(self.__var,self.__var+self.__len):
                if i==self.__var or i==self.__var+self.__len-1:
                    if self.__cannon == 1:
                        self.__strin+='C'
                    else:
                        self.__strin+='='
                else:
                    self.__strin+=("=")
            for i in range(self.__var+self.__len,150):
                if i==149:
                    self.__strin+="|"
                else:
                    self.__strin+=" "
            arr[35]=self.__strin
            self.__strin=""
            for i in range(150):
                chk = 0
                for j in range(len(self.__activatepaddlarr)):
                    if self.__activatepaddlarr[j].getxpos()==i:
                        chk = 1
                if chk == 1:
                    self.__strin+='o'
                else:
                    if i==0 or i==149:
                        self.__strin+='|'
                    else:
                        self.__strin+=' '
                    
                    
            arr[34]=self.__strin
        return arr,self.__activategrabpaddle
    def __movleft(self,arr):
        #print("length = ",self.__len)
        #print("length checker",len(self.__activatepaddlarr))
        if(self.__var>=3):
            self.__var-=2
            self.__strin=""
            self.__cntr-=2
            #for i in range(len(self.__activatepaddlarr)):
                #print("unupdated pos")
                #print(self.__activatepaddlarr[i].getxpos())
            for i in range(len(self.__activatepaddlarr)):
                self.__activatepaddlarr[i].setxypos(self.__activatepaddlarr[i].getxpos()-2,34)
            # for i in range(len(self.__activatepaddlarr)):
            #     print("updated pos")
            #     print(self.__activatepaddlarr[i].getxpos())
            for i in range(0,self.__var):
                if i==0:
                    self.__strin+="|"
                else:
                    self.__strin+=" "
            for i in range(self.__var,self.__var+self.__len):
                if i==self.__var or i==self.__len+self.__var-1:
                    if self.__cannon == 1:
                        self.__strin+='C'
                    else:
                        self.__strin+='='
                else:
                    self.__strin+=("=")
                # self.__strin+=("=")
            for i in range(self.__var+self.__len,150):
                if i==149:
                    self.__strin+="|"
                else:
                    self.__strin+=" "
            arr[35]=self.__strin
            self.__strin=""
            for i in range(150):
                chk = 0
                for j in range(len(self.__activatepaddlarr)):
                    if self.__activatepaddlarr[j].getxpos()==i:
                        chk = 1
                if chk == 1:
                    self.__strin+='o'
                else:
                    if i==0 or i==149:
                        self.__strin+='|'
                    else:
                        self.__strin+=' '
                    
            arr[34]=self.__strin
        return arr,self.__activategrabpaddle
    def initializepaddle(self):
        strin = ""
        self.__len = 5
        self.__var = 1
        self.__resid = 2
        for i in range(150):
            if i>=1 and i<=5:
                strin += self.__txt
            else:
                strin+=" "
        return strin
    def padlrightpos(self):
        #print("var=",self.var)
        if self.__var+self.__len+1<=148:
            return 1
        else:
            return 0
    def padlleftpos(self):
        if self.__var-2>=0:
            return 1
        else:
            return 0
    def returnpaddle(self,tdarr):
        strint=''
        for i in range(0,self.__var):
            if i==0:
                strint+="|"
            else:
                strint+=" "
        for i in range(self.__var,self.__var+self.__len):
            if i==self.__var or i==self.__len+self.__var-1:
                    if self.__cannon == 1:
                        strint+='C'
                    else:
                        strint+='='
            else:
                strint+=("=")
            # strint+=("=")
        for i in range(self.__var+self.__len,150):
            if i==149:
                strint+="|"
            else:
                strint+=" "
        tdarr[35] = strint
        if self.__activategrabpaddle != 0:
            self.__strin=""
            for i in range(150):
                chk = 0
                for j in range(len(self.__activatepaddlarr)):
                    if self.__activatepaddlarr[j].getxpos()==i:
                        chk = 1
                if chk == 1:
                    self.__strin+='o'
                else:
                    if i==0 or i==149:
                        self.__strin+='|'
                    else:
                        self.__strin+=' '
                        
            tdarr[34]=self.__strin
        return tdarr
    def getpadlcentr(self):
        return self.__cntr
    def callmoveleft(self,arr):
        return self.__movleft(arr)
    def callmoveright(self,arr):
        return self.__movright(arr)
    def getpadlresid(self):
        return self.__resid
    def resetpadlpos(self):
        self.__var = 1
        self.__cntr = 3
        self.__resid = 2
    def increasepadllength(self):
        self.__len+=2
        self.__cntr+=1
        self.__resid+=1
    def decreasepadllength(self):
        if self.__len >=5:
            self.__len-=2
            self.__cntr-=1
            self.__resid-=1
    def getactivategrabpaddle(self):
        return self.__activategrabpaddle
    def setactivagegrabpaddle(self,val):
        self.__activategrabpaddle = val
        
    def getactivatepaddlearr(self):
        var = self.__activatepaddlarr
        self.__activatepaddlarr = []
        self.setactivagegrabpaddle(0)
        return var
    def setactivatepaddlearr(self,val):
        for i in range(len(val)):
            self.__activatepaddlarr.append(val[i])
        #print("enter activate paddle")
        self.setactivagegrabpaddle(1)
        # self.__activategrabpaddlearr = val
        #print("flag=",self.__activategrabpaddle)
        #print(len(self.__activatepaddlarr))
        #print(len(val))
        # for i in range(len(self.__activatepaddlarr)):
        #     print(self.__activatepaddlarr[i].getxpos())

    def getpaddlehealth(self):
        return self.__paddlehealth
    def setpaddlehealth(self,val):
        self.__paddlehealth = val
    def redpaddlehealth(self):
        self.__paddlehealth = self.__paddlehealth - 1
        return self.__paddlehealth
    def paddlegrabset(self,arr):
        print('Nun')
    def paddledegrab(self):
        if self.__activategrabpaddle==1:
            for i in range(len(self.__activatepaddlarr)):
                # print("xvel = ")
                # print(self.__activatepaddlarr[i].getxvel())
                self.__activatepaddlarr[i].setflagandgrab(0)
            #self.__activatepaddlarr = []
    def setcannon(self,var):
       self.__cannon = var

    def getcannon(self):
        return self.__cannon
    def resetbulletarray(self):
        self.__bulletarr = []
    def createbullet(self):
        newbullet1 = bullet()
        newbullet2 = bullet()
        newbullet1.setxpos(self.__cntr-self.__resid)
        newbullet2.setxpos(self.__cntr+self.__resid)
        self.__bulletarr.append(newbullet1)
        self.__bulletarr.append(newbullet2)
    def cleartdarr(self,tdarr,brick):
        idtemp = brick.retrunidval()
        for i in range(37):
            strin = ''
            for j in range(150):
                if idtemp[i][j]==0:
                    if tdarr[i][j]=='#' or tdarr[i][j]=='*' or tdarr[i][j]=='G' or tdarr[i][j]=='R':
                        strin+=' '
                    else:
                        strin+=tdarr[i][j]
                else:
                    strin+=tdarr[i][j]
            tdarr[i]=strin
        return tdarr

    def updatebulletpos(self,tdarr,brick):
        for i in range(len(self.__bulletarr)):
            y = self.__bulletarr[i].getypos()
            x = self.__bulletarr[i].getxpos()
            strin = ''
            tempr = ''
            idtemp = brick.retrunidval()
            if self.__bulletarr[i].getstartflag()==0:
                for t in range(len(tdarr[y])):
                    if tdarr[y][t] == '@'or tdarr[y][t] == 'o' :
                        tempr += ' '
                    else:
                        if (tdarr[y][t]=='#' or tdarr[y][t]=='G' or tdarr[y][t]=='*') and idtemp[y][t]==0:
                            tempr+=' '
                        else:
                            tempr +=tdarr[y][t]
                
                self.__bulletarr[i].setprev(tempr)
                self.__bulletarr[i].setyprev(y)
                for j in range(150):
                    if j == x:
                        strin+=self.__bulletarr[i].getchar()
                    else:
                        strin+=tdarr[y][j]
                tdarr[y] = strin
                self.__bulletarr[i].setstartflag(1)
                tempr = ''
                
                    
                
                self.__bulletarr[i].setyprev(y)
                self.__bulletarr[i].setypos()
            else:
                tdarr[self.__bulletarr[i].getyprev()]= self.__bulletarr[i].getprev()
                strin = ''
                for j in range(150):
                    if j == x:
                        strin+=self.__bulletarr[i].getchar()
                    else:
                        strin+=tdarr[y][j]
                for t in range(len(tdarr[y])):
                    if tdarr[y][t] == '@'or tdarr[y][t] == 'o' :
                        tempr += ' '
                    else:
                        if (tdarr[y][t]=='#' or tdarr[y][t]=='G' or tdarr[y][t]=='*') and idtemp[y][t]==0:
                            tempr+=' '
                        else:
                            tempr +=tdarr[y][t]
                
                self.__bulletarr[i].setprev(tempr)
                # self.__bulletarr[i].setprev(tdarr[y])
                print("ypos=",self.__bulletarr[i].getypos())
                if self.__bulletarr[i].getypos()==1:
                    self.__bulletarr.pop(i)
                    return tdarr,brick,-1
                ynew = self.__bulletarr[i].getypos()
                xnew = self.__bulletarr[i].getxpos()
                idtemp = brick.retrunidval()
                removebrickflag = -1
                flag = 0
                if idtemp[ynew][xnew]!=0:
                    array1 =  brick.getarray()
                    for p in range(len(array1)):
                        if array1[p].getid()==idtemp[ynew][xnew]:
                            chk = array1[p].setcolofvalue(0)
                            if chk ==1:
                                removebrickflag = idtemp[ynew][xnew]
                            flag = 1
                        if flag==1:
                            break
                    self.__bulletarr.pop(i),brick,removebrickflag
                    return tdarr,brick,removebrickflag
                tdarr[y]=strin
                self.__bulletarr[i].setyprev(y)
                
                self.__bulletarr[i].setypos()
        return tdarr,brick,-1

        # temp = ""
        # tempr = ""

        
        

