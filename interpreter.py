import cv2
import random

def rgb(i,x,y):
    return list(img[y,x])[::-1]
#         emptyspace    output  stop          input         65535-x      gotopleft  rng           turnleft    turn180deg   if           adjacentsum   turnright   moveright    moveleft    subtractone   addone      divide        multiply    valueforward  valuebackward
colors = [[255,255,255],[0,0,0],[195,195,195],[127,127,127],[185,122,87],[136,0,21],[255,174,201],[237,28,36],[255,201,14],[255,127,39],[239,228,176],[255,242,0],[181,230,29],[34,177,76],[153,217,234],[0,162,232],[112,146,190],[63,72,204],[200,191,231],[163,73,164]]

a = chr(3)

def turn(d,x):
    for x1 in range(x):
        if d==[1,0]:
            d=[0,1]
            continue
        elif d==[0,1]:
            d=[-1,0]
            continue
        elif d==[-1,0]:
            d=[0,-1]
            continue
        elif d==[0,-1]:
            d=[1,0]
            continue
    return d

def wrap(x):
    while x < 0:
        x += 65536
    while x > 65535:
        x -= 65536
    return x

print("hi there this the is paint++ interpreter")
img = cv2.imread(input("image directory: "))
width,height = img.shape[1],img.shape[0]
corner = [width-1,height-1]
tape,end = [0],0
codepoint,datapoint=[0,0],0
direc = [1,0]
#print(rgb(img,4,1))
# remember the chr(int) function

while True:
    '''print(codepoint)
    print(tape)'''
    move_flag = True
    color = list(img[codepoint[1]][codepoint[0]])
    try:
        i = colors.index(color[::-1])
    except:
        color,i = [255,255,255],0
    #print(i)

    
    ### I/O
    if i==1:
        try:
            print(chr(tape[datapoint]),end='')
        except:
            print('',end='')
    elif i==2:
        break
    elif i==3:
        tape[datapoint] = ord(input()[0])

    ### The Miscellaneous(TM)
    elif i==4:
        tape[datapoint] = 65535 - tape[datapoint]
    elif i==5:
        moveflag = False
        m_direc = list(map(lambda x: 2*x-x,direc))
        codepoint[0]+=m_direc[0]
        codepoint[1]+=m_direc[1]
    elif i==6:
        tape[datapoint] = random.randint(0,65535)
    elif i==10:
        if datapoint+1 > end:
            tape[datapoint]=tape[datapoint-1]
        elif datapoint == 0:
            tape[datapoint]=tape[datapoint+1]
        else:
            tape[datapoint]=tape[datapoint-1]+tape[datapoint+1]

    ### Turning
    elif i==11:
        direc=turn(direc,1)
    elif i==8:
        direc=turn(direc,2)
    elif i==7:
        direc=turn(direc,3)
    
    ### Conditional
    elif i==9:
        if tape[datapoint] > 0:
            direc=[0,-1]
        else: 
            direc=[0,1]

    ### Moving data pointer
    elif i==12:
        datapoint+=1
        if datapoint > end:
            end+=1
            tape.append(0)
    elif i==13:
        datapoint = max(0,datapoint-1)

    ### Adding/subtracting 1
    elif i==14:
        tape[datapoint]-=1
    elif i==15:
        tape[datapoint]+=1

    ### Division/multiplication
    elif i==16:
        if datapoint+1 > end:
            end+=1
            tape.append(0)
        if tape[datapoint+1] == 0:
            tape[datapoint] = 0
        else:
            tape[datapoint] = tape[datapoint] // tape[datapoint+1]
    elif i==17:
        if datapoint+1 > end:
            end+=1
            tape.append(0)
        tape[datapoint] *= tape[datapoint+1]
    
    ### Moving X steps
    elif i==18:
        moveflag = False
        m_direc = list(map(lambda x: (-tape[datapoint])*x-x,direc))
        codepoint[0]+=m_direc[0]
        codepoint[1]+=m_direc[1]
    elif i==19:
        moveflag = False
        m_direc = list(map(lambda x: tape[datapoint]*x-x,direc))
        codepoint[0]+=m_direc[0]
        codepoint[1]+=m_direc[1]

    tape[datapoint] = wrap(tape[datapoint])
    if move_flag:
        codepoint[0]+=direc[0]
        codepoint[1]+=direc[1]
    #print(tape)
    if codepoint[0] < 0 or codepoint[0] > corner[0]:
        break
    if codepoint[1] < 0 or codepoint[1] > corner[1]:
        break

print()
print(tape)