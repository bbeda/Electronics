from machine import Pin
import time

COLS=8
ROWS=12

columns=[]
rows=[]
state=[]

def initPortrait():
    COLS=8
    ROWS=12    
    for ix in range(0,COLS):
        columns.append(Pin(ix, Pin.OUT))
    for iy in range(COLS,COLS+ROWS+1):
        rows.append(Pin(iy, Pin.OUT))

    for ix in range (0,ROWS):
        row=[]
        for iy in range(0,COLS):
            row.append(0)
        state.append(row)
    return (ROWS,COLS)

def initLandscape():
    COLS=12
    ROWS=8
    for ix in range(ROWS,COLS+ROWS):
        columns.append(Pin(ix, Pin.OUT))
        
    for iy in range(0,ROWS):
        rows.append(Pin(ROWS-1-iy, Pin.OUT))

    for ix in range (0,ROWS):
        row=[]
        for iy in range(0,COLS):
            row.append(0)
        state.append(row)
    return (ROWS,COLS)

def clear():
    for row in range(0,ROWS):        
        for column in range(0,COLS):
            state[row][column]=0

def Draw(rows, columns, statesList, refreshInterval):
    stateIndex=0
    scanInterval=0.0025
    while True:
        r=0;
        clear()
        statesList[stateIndex]()        
        rc=0
        while True:
            rows[r].value(1)
            for cx,c in enumerate(columns):                
                if state[r][cx]==1:
                    c.value(1)
            time.sleep(scanInterval)
            rows[r].value(0)
            for cx in columns:
                cx.value(0)
            r+=1
            if r>=ROWS:
                r=0
                
            rc+=1            
            if rc*scanInterval>refreshInterval:
                break
            
        stateIndex+=1
        if stateIndex>=len(statesList):
            stateIndex=0            
        
def point(x,y):
    if x>=0 and x<ROWS and y>=0 and y<COLS:
        state[x][y]=1

def hLine(x,y,len):
    for ix in range(0,len):                
            point(x,y+ix)

def vLine(x,y,len):
    for ix in range(0,len):        
        point(x+ix,y);

def char(char, x,y):
    printA(x,y)

def A(x,y):
    hLine(x,y+1,3)
    vLine(x,y,5)
    vLine(x,y+4,5)
    hLine(x+2,y+1,3)
    
def B(x,y):
    vLine(x,y,5)
    hLine(x,y,5)
    vLine(x,y+4,2)
    hLine(x+2,y,4)
    vLine(x+3,y+4,2)
    hLine(x+4,y,5)
    
def C(x,y):
    hLine(x,y,4)
    vLine(x,y,5)
    hLine(x+4,y,4)
    
def D(x,y):
    vLine(x,y,5)
    hLine(x,y,3)
    vLine(x+1,y+3,3)
    hLine(x+4,y,3)

def E(x,y):
    vLine(x,y,5)
    hLine(x,y,4)
    hLine(x+2,y,4)
    hLine(x+4,y,4)
    
def F(x,y):
    vLine(x,y,5)
    hLine(x,y,4)
    hLine(x+2,y,3)
    
def G(x,y):
    vLine(x,y,5)
    hLine(x,y,4)
    hLine(x+4,y,4)
    vLine(x+2,y+3,3)
    hLine(x+2,y+2,2)

def H(x,y):
    vLine(x,y,5)
    vLine(x,y+3,5)
    hLine(x+2,y,4)
    
def I(x,y):
    vLine(x,y+2,5)
    hLine(x,y+1,3)
    hLine(x+4,y+1,3)
    
def J(x,y):
    vLine(x,y,5)
    hLine(x+4,y,4)
    vLine(x+2,y+3,3)
    hLine(x+2,y+2,2)

def K(x,y):
    vLine(x,y,5)
    point(x+2,y+1)
    point(x+1,y+2)
    point(x+3,y+2)
    point(x,y+3)
    point(x+4,y+3)
    
def L(x,y):
    vLine(x,y,5)
    hLine(x+4,y,4)
    
def M(x,y):
    vLine(x,y,5)
    vLine(x,y+4,5)
    point(x+1,y+1)
    point(x+1,y+3)
    point(x+2,y+2)
    
def N(x,y):
    vLine(x,y,5)
    vLine(x,y+4,5)
    point(x+1,y+1)
    point(x+2,y+2)
    point(x+3,y+3)
    point(x+4,y+4)
    
def O(x,y):
    vLine(x+1,y,3)
    vLine(x+1,y+4,3)
    hLine(x,y+1,3)
    hLine(x+4,y+1,3)
    
def P(x,y):
    hLine(x,y,3)
    vLine(x,y,5)
    vLine(x,y+3,2)
    hLine(x+2,y,3)
    
def Q(x,y):
    vLine(x+1,y,3)
    vLine(x+1,y+4,3)
    hLine(x,y+1,3)
    hLine(x+4,y+1,3)
    point(x+3,y+3)
    point(x+4,y+4)

def R(x,y):
    hLine(x,y,3)
    vLine(x,y,5)
    vLine(x,y+3,2)
    hLine(x+2,y,3)
    point(x+3,y+1)
    point(x+4,y+2)

def S(x,y):
    hLine(x,y+1,4)
    vLine(x,y+1,2)
    hLine(x+2,y+1,2)
    vLine(x+2,y+3,2)
    hLine(x+4,y,4)
    

def T(x,y):
    hLine(x,y,5)
    vLine(x,y+2,5)

def U(x,y):
    vLine(x,y,5)
    vLine(x,y+3,5)
    hLine(x+4,y,4)

def V(x,y):
    vLine(x,y,3)
    vLine(x,y+4,3)
    point(x+3,y+1)
    point(x+3,y+3)
    point(x+4,y+2)

def W(x,y):
    vLine(x,y,4)    
    point(x+4,y+1)
    point(x+3,y+2)
    point(x+4,y+3)
    point(x+3,y+4)
    vLine(x,y+4,4)
    
def X(x,y):
    point(x,y)
    point(x+1,y+1)
    point(x+2,y+2)
    point(x+3,y+3)
    point(x+4,y+4)
    point(x,y+4)
    point(x+1,y+3)
    point(x+2,y+2)
    point(x+3,y+1)
    point(x+4,y)
   
def Y(x,y):
    vLine(x+2,y+2,3)
    point(x,y)
    point(x+1,y+1)
    point(x+1,y+3)
    point(x,y+4)
    
def Z(x,y):
    hLine(x,y,5)
    hLine(x+4,y,5)
    point(x+1,y+3)
    point(x+2,y+2)
    point(x+3,y+1)

def comma(x,y):
    point(x+4,y+4)
    point(x+5,y+3)

def exclamation(x,y):
    vLine(x,y+4,3)
    point(x+4,y+4)
    
def nop(x,y):
    pass
        
statesList=[]

def addState(func):
    statesList.append(func)
    
writers=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]   
def getWriter(char):    
    if char==',':
        return comma    
    if char=='!':        
        return exclamation
    
    pos=ord(char)-65
    if pos<0 or pos>len(writers):
        return nop
    return writers[ord(char)-65]

def writeC(char,x,y):
    writer=getWriter(char)
    if writer:
        addState(lambda xx=x,yy=y: writer(xx,yy))
                           
def write(text, x,y):
    def writer(txt=text,xx=x,yy=y):
        for ix,c in enumerate(txt):
            cWriter=getWriter(c)            
            cPos=yy+ix*5+ix
            cWriter(xx,cPos)
    addState(writer)
 
def scrollText(text, pos):
    text=text.upper()
    length=len(text)*5+5+COLS+COLS
    for p in range(COLS,-length,-1):
        write(text,pos,p)   
 
(ROWS,COLS)=initPortrait()
#(ROWS,COLS)=initLandscape()

scrollText("Hello World !",3)

Draw(rows, columns, statesList,0.1)