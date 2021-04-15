#import colorama
from colorama import Fore, Back, Style
import time
import os
import sys
#colorama.init(autoreset=True)
class printboard:
    #tdarr = []
    def __init__(self):
        self.__tdarr = []
        self.__scr = 0
        self.__timeplayed = 0
        self.__liferemain = 4
    def __updategrid(self,arr):
        self.__tdarr = arr
    def getscore(self):
        return self.__scr
    def updatescore(self,val):
        self.__scr = val
    def copygrid(self):
        return self.__tdarr
   # def updatepadl(self,arr):
    #    self.tdarr[]
    def __printscreeninit(self):
        scr =0
        self.__tdarr = []
        print('\n')
        print("YOUR SCORE:",scr)
        for i in range(37):
            strin=""
            for j in range(150):
                if i==0 or i==36:
                    strin+="-"
                else:
                    if i==35:
                        if j >= 1 and j<=5:
                            txt = '='
                            txt = Back.RED+txt+Style.RESET_ALL
                            #Back.RESET
                            strin+=txt
                        elif j==0 or j==149:
                            strin+=("|")
                        else:
                            strin+=" "
                    elif j==0 or j==149:
                        strin+=("|")
                    else:
                        strin+=" "
            self.__tdarr.append(strin)
        #return tdarr
    def __printscreen(self,vis,idarr,getarr):
        tempo = ""
        for i in range(150):
            tempo+=" "
        print(' ')
        print("YOUR SCORE IS", self.__scr,"  TIME ACTIVE:",int(time.time()-self.__timeplayed),"s"," Lives Remaining:",self.__liferemain)
        # for i in range(len(getarr)):
        #     print(getarr[i].getid())
        # for i in range(37):
        #     for j in range(150):
        #         print(idarr[i][j],end='')
        #     print()
        for i in range(37):
            for j in range(150):
                color = Back.BLUE
                if vis[i][j] != 0:
                    ident = idarr[i][j]
                    for k in range(len(getarr)):
                        if getarr[k].getid() == ident:
                            color = getarr[k].getcolor()
                    #print("color is",color)
                    print(color+self.__tdarr[i][j]+Back.RESET,end='')
                    #print("color=",color)
                else:
                    print(self.__tdarr[i][j],end='')
            print()
        #os.system('clear')
        #for i in range(15):
        #    print(tempo)

    def setupdategrid(self,arr):
        return self.__updategrid(arr)
    def callprintscreen(self,vis,idarr,getarr):
        #os.system('clear')
        self.__printscreen(vis,idarr,getarr)
    def getinitalscreen(self):
        return self.__printscreeninit()
    def initializetime(self):
        self.__timeplayed = time.time()
    def getlives(self):
        if self.__liferemain==0:
            print("Game Over")
            sys.exit()
        self.__liferemain-=1
    




            
    
