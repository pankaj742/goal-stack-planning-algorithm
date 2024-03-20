import pygame,sys,time,random
from pygame.locals import *
pygame.init()
windowSurface=pygame.display.set_mode((900,650),0,32)
pygame.display.set_caption("Goal Stack Planning")
WHITE=(255,255,255)
black=(0,0,0)
green=(57, 198, 132)
thoda_green=(48, 232, 183)
sunehra=(255, 176, 7)
thoda_sunehra=(255, 139, 7)
nila=(178, 255, 244)
textBack=(54, 118, 130)
strt_color=(180, 255, 119)
succ_color=(201, 18, 134)
goal_color=(81, 205, 239)
#clock
clock=pygame.time.Clock()
#data structure for storing blocks
side1=[]
side2=[]
#arm
arm=None
state=1
def mainloop():
    #print(pygame.font.get_fonts())
    #main loop
    while(True):
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
        windowSurface.fill(WHITE)
        nameplate()
        button("Start",100,550,100,60,green,thoda_green,"start")
        button("Randomize",600,550,100,60,sunehra,thoda_sunehra,"randomize")
        drawSides("side1")
        drawSides("side2")
        first_indicator()
        pygame.display.update()
        #time.sleep(0.01)
        clock.tick(9)
def nameplate():
    rect1=pygame.Rect((360,5,170,50))
    basicFont=pygame.font.SysFont("comicsansms",14)
    text1=basicFont.render("developed by pankaj shah",True,black,strt_color)
    text1Rect=text1.get_rect()
    text1Rect.centerx=rect1.centerx
    text1Rect.centery=rect1.centery
    pygame.draw.rect(windowSurface,strt_color,rect1)
    windowSurface.blit(text1,text1Rect)
def drawSides(side):
    #draw two sides
    if side=="side1":
        for i in range(3):
            colum=side1[i]
            for j in range(3):
                box=colum[j]
                pygame.draw.rect(windowSurface,box["color"],box["rect"],2)
                drawText(box["tag"],box["centerx"],box["centery"])
    elif side=="side2":
        for i in range(3):
            colum=side2[i]
            for j in range(3):
                box=colum[j]
                pygame.draw.rect(windowSurface,box["color"],box["rect"],2)
                drawText(box["tag"],box["centerx"],box["centery"])

def first_indicator():
    #print("in first_indicator and case:"+str(case))
    if(state == 1):
        indicators("Start Position","Goal Position",strt_color)
    elif(state == 2):
        indicators("Goal Achived","Goal Position",succ_color)
def indicators(msg1,msg2,fcolor):
    rect1=pygame.Rect((75,400,250,100))
    basicFont=pygame.font.SysFont(None,48)
    text1=basicFont.render(msg1,True,black,fcolor)
    text1Rect=text1.get_rect()
    text1Rect.centerx=rect1.centerx
    text1Rect.centery=rect1.centery

    rect2=pygame.Rect((575,400,250,100))
    text2=basicFont.render(msg2,True,WHITE,goal_color)
    text2Rect=text2.get_rect()
    text2Rect.centerx=rect2.centerx
    text2Rect.centery=rect2.centery

    pygame.draw.rect(windowSurface,fcolor,rect1)
    pygame.draw.rect(windowSurface,goal_color,rect2)
    windowSurface.blit(text1,text1Rect)
    windowSurface.blit(text2,text2Rect)
    
def button(msg,x,y,w,h,ic,ac,action=None):
    #find button
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    #print(click)
    #print(mouse)
    if(x+w>mouse[0]>x and y+h > mouse[1] >y):
        pygame.draw.rect(windowSurface,ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            if action == "start":
                start()
                print("start")
            elif action == "randomize":
                randomize()
    else:
        pygame.draw.rect(windowSurface,ic,(x,y,w,h))
    smallText=pygame.font.SysFont(None,20)
    textSurf=smallText.render(msg,True,black,ic)
    textRect=textSurf.get_rect()
    textRect.centerx= x+(w/2)
    textRect.centery= y+(h/2)
    windowSurface.blit(textSurf,textRect)
def randomize():
    global state
    state =1
    initialize_blocks()
    pos1=list(range(0,9))
    pos2=list(range(0,9))
    newpos1=[]
    newpos2=[]
    lettors=["A","B","C"]
    for i in range(3):
        rand1=random.randint(0,len(pos1)-1)
        rand2=random.randint(0,len(pos2)-1)
        newpos1.append(pos1[rand1])
        newpos2.append(pos2[rand2])
        pos1.remove(pos1[rand1])
        pos2.remove(pos2[rand2])
    print(newpos1)
    print(newpos2)
    for j in range(3):
        side1[newpos1[j]//3][newpos1[j]%3]["tag"]=lettors[j]
        side2[newpos2[j]//3][newpos2[j]%3]["tag"]=lettors[j]
    gravity()

#start function
def start():
    work=[]
    for i in range(3):
        colum=side2[i]
        for j in range(3):
            if((j in (0,1)) and (colum[j+1]["tag"] != None) and (colum[j]["tag"] != None)):
                t=["on",colum[j]["tag"],colum[j+1]["tag"]]
                work.append(t)
            if((j==2) and (colum[j-1]["tag"] == None) and (colum[j]["tag"] != None)):
                t=["ont",colum[j]["tag"]]
                work.append(t)
            else:
                continue
    print(work)
    x=None
    xarg=None
    y=None
    yarg=None
    z=None
    zarg=None
    length=len(work)
    for i in range(len(work)):
        opname=work[i][0]
        if(i==0):
            if(opname=="on"):
                x=on
                xarg=(work[i][1],work[i][2])
            elif(opname=="ont"):
                x=onT
                xarg=work[i][1]
        if(i==1):
            if(opname=="on"):
                y=on
                yarg=(work[i][1],work[i][2])
            elif(opname=="ont"):
                y=onT
                yarg=work[i][1]
        if(i==2):
            if(opname=="on"):
                z=on
                zarg=(work[i][1],work[i][2])
            elif(opname=="ont"):
                z=onT
                zarg=work[i][1]
    start_planning(x,xarg,y,yarg,z,zarg,length)
    #print("just below state:"+str(state))
    global state
    state =2
def start_planning(x,xarg,y,yarg,z,zarg,length):
    flip1=0
    flip2=0
    case1=0
    case2=0
    case3=0
    if(length==1):
        if(x==on):
            x(xarg[0],xarg[1])
            if(x(xarg[0],xarg[1]) == True):
                return True
        elif(x==onT):
            x(xarg)
            if(x(xarg) == True):
                return True
    elif(length==2):
        if(x==on):
            x(xarg[0],xarg[1])
        elif(x==onT):
            flip1=1
            x(xarg)
        if(y==on):
            y(yarg[0],yarg[1])
        elif(y==onT):
            flip2=1
            y(yarg)
        if(flip1==0 and flip2==0):
            if((y(yarg[0],yarg[1]) and (x(xarg[0],xarg[1]))) == True ):
                return True
        elif(flip1==0 and flip2==1):
            if((y(yarg) and x(xarg[0],xarg[1])) == True ):
                return True
        elif(flip1==1 and flip2==0):
            if((y(yarg[0],yarg[1]) and x(xarg)) == True ):
                return True
        elif(flip1==1 and flip2==1):
            if((y(yarg) and x(xarg)) == True ):
                return True
        
    elif(length==3):
        if(x==on):
            x(xarg[0],xarg[1])
        elif(x==onT):
            case1=1
            x(xarg)
        if(y==on):
            y(yarg[0],yarg[1])
        elif(y==onT):
            case2=1
            y(yarg)
        if(z==on):
            z(zarg[0],zarg[1])
        elif(z==onT):
            case3=1
            z(zarg)
        if(case1==0 and case2==0 and case3==0):
            if((z(zarg[0],zarg[1]) and y(yarg[0],yarg[1]) and x(xarg[0],xarg[1]) ) == True):
                return True
        elif(case1==0 and case2==0 and case3==1):
            if((z(zarg) and y(yarg[0],yarg[1]) and x(xarg[0],xarg[1])) == True):
                return True
        elif(case1==0 and case2==1 and case3==0):
            if((z(zarg[0],zarg[1]) and y(yarg) and x(xarg[0],xarg[1])) == True):
                return True
        elif(case1==0 and case2==1 and case3==1):
            if((z(zarg) and y(yarg) and x(xarg[0],xarg[1])) == True):
                return True
        elif(case1==1 and case2==0 and case3==0):
            if((z(zarg[0],zarg[1]) and y(yarg[0],yarg[1]) and x(xarg)) == True):
                return True
        elif(case1==1 and case2==0 and case3==1):
            if((z(zarg) and y(yarg[0],yarg[1]) and x(xarg)) == True):
                return True
        elif(case1==1 and case2==1 and case3==0):
            if((z(zarg[0],zarg[1]) and y(yarg) and x(xarg)) == True):
                return True
        elif(case1==1 and case2==1 and case3==1):
            if((z(zarg) and y(yarg) and x(xarg)) == True):
                    return True
def find_id(tag):
    for i in range(3):
        for j in range(3):
            if(side1[i][j]["tag"] == tag):
                return(side1[i][j]["pos"])
def initialize_blocks():
    for i in range(9):
        side1[i//3][i%3]["tag"]=None
        side2[i//3][i%3]["tag"]=None
        
def gravity():
    for i in range(3):
        for j in range(2,-1,-1):
            tag=side1[i][j]["tag"]
            if(j in (2,1)):
                uptag=side1[i][j-1]["tag"]
                if((tag==None) and (uptag != None) and j!=1):
                    (side1[i][j]["tag"],side1[i][j-1]["tag"])=(side1[i][j-1]["tag"],side1[i][j]["tag"])
                elif(j==1):
                    downtag=side1[i][j+1]["tag"]
                    if((tag==None) and (uptag != None) and (downtag==None)):
                        (side1[i][j+1]["tag"],side1[i][j-1]["tag"])=(side1[i][j-1]["tag"],side1[i][j+1]["tag"])
                    elif((tag==None) and (uptag != None) and (downtag!=None)):
                        (side1[i][j]["tag"],side1[i][j-1]["tag"])=(side1[i][j-1]["tag"],side1[i][j]["tag"])
            
        
    for i in range(3):
        for j in range(2,-1,-1):
            tag=side2[i][j]["tag"]
            if(j in (2,1)):
                uptag=side2[i][j-1]["tag"]
                if((tag==None) and (uptag != None) and j!=1):
                    (side2[i][j]["tag"],side2[i][j-1]["tag"])=(side2[i][j-1]["tag"],side2[i][j]["tag"])
                elif(j==1):
                    downtag=side2[i][j+1]["tag"]
                    if((tag==None) and (uptag != None) and (downtag==None)):
                        (side2[i][j+1]["tag"],side2[i][j-1]["tag"])=(side2[i][j-1]["tag"],side2[i][j+1]["tag"])
                    elif((tag==None) and (uptag != None) and (downtag!=None)):
                        (side2[i][j]["tag"],side2[i][j-1]["tag"])=(side2[i][j-1]["tag"],side2[i][j]["tag"])
            
def createBlocks(side1,side2):
    #create blocks
    for i in range(3):
        side1.append([])
        for j in range(3):
            box={}
            box["pos"]=(i*3+j)
            box["rect"]=pygame.Rect(0,0,100,100)
            box["centerx"]=i*100+100
            box["centery"]=j*100+100
            box["rect"].centerx=box["centerx"]
            box["rect"].centery=box["centery"]
            box["tag"]=None
            box["color"]=nila
            side1[i].append(box)
    for i in range(3):
        side2.append([])
        for j in range(3):
            box={}
            box["pos"]=(i*3+j)
            box["rect"]=pygame.Rect(0,0,100,100)
            box["centerx"]=i*100+100+500
            box["centery"]=j*100+100
            box["rect"].centerx=box["centerx"]
            box["rect"].centery=box["centery"]
            box["tag"]=None
            box["color"]=nila
            side2[i].append(box)
def drawText(msg,x,y):
    basicFont=pygame.font.SysFont(None,48)
    text=basicFont.render(msg,True,WHITE,textBack)
    textRect=text.get_rect()
    textRect.centerx=x
    textRect.centery=y
    windowSurface.blit(text,textRect)

#starting of all the robot and planning functions
def pickup(x):
    #print("in pickup")
    position=find(x)
    xpos=position[0]
    tag=side1[xpos//3][xpos%3]["tag"]
    #clear(x)
    onT(x)
    armempty()
    if(armempty() and onT(x)):
        position=find(x)
        xpos=position[0]
        arm=xpos
        print("pickup"+x)
        return True
        
def putdown(x):
    #print("in putdown")
    position=find(x)
    xpos=position[0]
    tag=side1[xpos//3][xpos%3]["tag"]
    if(holding(x)):
        arm=None
        print("putdown"+x)
        return True
        
def stack(x,y):
    #print("in stack"+x+","+y)
    position=find(x,y)
    xpos=position[0]
    ypos=position[1]
    tag1=side1[xpos//3][xpos%3]["tag"]
    tag2=side1[ypos//3][ypos%3]["tag"]
    clear(y)
    holding(x)
    if( clear(y) == True):
        position=find(x,y)
        xpos=position[0]
        ypos=position[1]
        (side1[xpos//3][xpos%3]["tag"] ,side1[ypos//3][ypos%3-1]["tag"] )=(side1[ypos//3][ypos%3-1]["tag"] ,side1[xpos//3][xpos%3]["tag"] )
        arm=ypos-1
        print("stack"+x+","+y)
        return True
        
    
    
def unstack(x,y):
    #print("in unstack"+x+","+y)
    position=find(x,y)
    xpos=position[0]
    ypos=position[1]
    tag1=side1[xpos//3][xpos%3]["tag"]
    tag2=side1[ypos//3][ypos%3]["tag"]
    clear(x)
    on(x,y)
    armempty()
    if(armempty() and on(x,y) and clear(x)):
        position=find(x,y)
        xpos=position[0]
        ypos=position[1]
        arm=xpos
        for i in range(3):
            if(side1[i][2]["tag"] == None):
                (side1[i][2]["tag"] ,side1[arm//3][arm%3]["tag"] )=(side1[arm//3][arm%3]["tag"] ,side1[i][2]["tag"] )
                if(i==0):
                    arm=2
                elif(i==1):
                    arm=5
                elif(i==2):
                    arm=8
                break
        print("unstack"+x+','+y)
        return True
        
        
#checkin functions
def armempty():
    if arm == None:
        #print("in arm_empty None")
        return True
    else:
        armstring=side1[arm//3][arm%3]["tag"]
        #print("in arm_empty "+armstring)
        if(putdown(armstring) == True):
            return True
        return False
def onT(x):
    #print("in onTable:"+x)
    position=find(x)
    xpos=position[0]
    tag=side1[xpos//3][xpos%3]["tag"]
    if(xpos%3==2 and clear(x)):
        return True
    else:
        position=find(x)
        xpos=position[0]
        xstring=side1[xpos//3][xpos%3]["tag"]
        xplus=side1[xpos//3][xpos%3+1]["tag"]
        if(unstack(xstring,xplus) == True):
            return True
        return False
def clear(x):
    #print("in clear:"+x)
    position=find(x)
    xpos=position[0]
    if(xpos%3==0):
        return True
    else:
        tag=side1[xpos//3][xpos%3-1]["tag"]
        if(tag == None):
            return True
        else:
            position=find(x)
            xpos=position[0]
            xstring=side1[xpos//3][xpos%3]["tag"]
            xminus=side1[xpos//3][xpos%3-1]["tag"]
            if(unstack(xminus,xstring) == True):
                return True
            else:
                return False
def holding(x):
    #print("in holding:"+x)
    position=find(x)
    xpos=position[0]
    if(arm==xpos):
        return True
    else:
        if(pickup(x) == True):
            return True
        return False
def on(x,y):
    #print("in on:"+x+","+y)
    position=find(x,y)
    xpos=position[0]
    ypos=position[1]
    if(xpos%3 ==2):
        if(stack(x,y) == True):
            return True
        return False
    if(xpos+1 == ypos):
        return True
    else:
        if(stack(x,y) == True):
            return True
        return False

#very important function find
def find(x,y=None):
    xpos=None
    ypos=None
    if(y == None):
        for i in range(9):
            tag=side1[i//3][i%3]["tag"]
            if(tag == x):
                return (i,None)
    else:
        for i in range(9):
            tag=side1[i//3][i%3]["tag"]
            if(tag == x):
                xpos=i
            elif(tag == y):
                ypos=i
            if((xpos != None) and (ypos != None)):
                break
        return((xpos,ypos))
#main loop call
createBlocks(side1,side2)
mainloop()

       
