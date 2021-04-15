from colorama import Fore, Back, Style
class paddl:
    def __init__(self):
        self.__strin=""
        self.__var = 1
        self.__txt = '='
        self.__cntr =3
        self.__len = 5
        self.__resid = 2
        self.__activatepaddlarr = []
        self.__activategrabpaddle = 0
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
            strint+=("=")
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

    def paddlegrabset(self,arr):
        print('Nun')
    def paddledegrab(self):
        if self.__activategrabpaddle==1:
            for i in range(len(self.__activatepaddlarr)):
                # print("xvel = ")
                # print(self.__activatepaddlarr[i].getxvel())
                self.__activatepaddlarr[i].setflagandgrab(0)
            #self.__activatepaddlarr = []
        
        

