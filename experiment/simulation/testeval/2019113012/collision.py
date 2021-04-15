class collide:
    def collidpaddle(xorg,yorg,xvel,yvel,cntr,lent):
        if yorg == 35:
            if xorg >= cntr-lent and xorg <= cntr + lent:
                if xorg > cntr:
                    xvel+=abs(cntr-xorg)
                elif xorg < cntr:
                    xvel-=abs(cntr-xorg)
        return xorg,yorg,xvel,yvel
    def collidwalls(xorg,xvel):
        if xorg >= 149 or xorg <= 0:
            print("enter inside xorg = 149")
            xvel=(-1*xvel)
        return xvel
        
        


        

        

