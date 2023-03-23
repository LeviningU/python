
#coding=utf-8
from functools import partial
from tkinter import *
import AI
import time
import random
import tkinter.messagebox

def read():
    global data,h,w
    #data = pd.read_excel('map_data.xlsx')
    #h,w = data.shape
    data = [0]*255
    h, w = 15, 15
    

def color(co):
    match co:
        case 0:
            return '#d3aa72'
        case 1:
            return '#fcf8ef'
        case 2:
            return '#171715'
        case _:
            return '#ff8c94'

def output():
    global buttonlist
    buttonlist = []
    for j in range(h):
        for i in range(w):
            buttonlist.append(i + j * w)
            buttonlist[i + j * w] = Button(win,bg=color(data[i + j * w]),command = partial(step,i + j * w))
            buttonlist[i + j * w].place(relx = i * 1 / 15,rely = 1 / 16 + j * 1 / 16,relheight = 1 / 16,relwidth = 1 / 15)

def step(a):
    global play,buttonlist
    if play == 0 and data[a] == 0:
        data[a] = 1
        play = 1 - play
        lab["text"]='AI1\'s turn'
        judge(a%w,a//w,play)
        buttonlist[a].configure(bg = color(data[a]))
        win.update()
        time.sleep(0.1)
        if endor == 0:
            step(AI.main1(data))
    elif play == 1 and data[a] == 0:
        data[a] = 2
        play = 1 - play
        lab["text"]='AI2\'s turn'
        judge(a%w,a//w,play)
        buttonlist[a].configure(bg = color(data[a]))
        win.update()
        time.sleep(0.1)
        if endor == 0:
            step(AI.main(data))
    

def judge(m,n,play):
    maxnum,max1,max2= 0,0,0
    number = 0
    num1,num2 = -1,0#x
    for i in range(m,-1,-1):
        if data[i+n*w] == data[m+n*w]:
            num1 += 1
        else:
            break
    for i in range(m,w):
        if data[i+n*w] == data[m+n*w]:
            num2 += 1
        else:
            break
    if num1 + num2 > maxnum:
        maxnum,max1,max2 = num1 + num2,num1,num2
        number = 1
    num1,num2 = -1,0#y
    for i in range(n,-1,-1):
        if data[m+i*w] == data[m+n*w]:
            num1 += 1
        else:
            break
    for i in range(n,h):
        if data[m+i*w] == data[m+n*w]:
            num2 += 1
        else:
            break
    if num1 + num2 > maxnum:
        maxnum,max1,max2 = num1 + num2,num1,num2
        number = 2
    num1,num2 = -1,0#x = y
    for i in range(m,-1,-1):
        if data[i+(i + n - m)*w] == data[m+n*w]:
            num1 += 1
        else:
            break
    for i in range(m,w):
        if i + n - m >= 15 or i + n - m < 0:
            break
        if data[i+(i + n - m)*w] == data[m+n*w]:
            num2 += 1
        else:
            break
    if num1 + num2 > maxnum:
        maxnum,max1,max2 = num1 + num2,num1,num2
        number = 3
    num1,num2 = -1,0#x = -y
    for i in range(m,-1,-1):
        if m + n - i >= 15 or m + n - i < 0:
            break
        if data[i+(n + m - i)*w] == data[m+n*w]:
            num1 += 1
        else:
            break
    for i in range(m,w):
        if data[i+(n + m - i)*w] == data[m+n*w]:
            num2 += 1
        else:
            break
    if num1 + num2 > maxnum:
        maxnum,max1,max2 = num1 + num2,num1,num2
        number = 4
    if maxnum >= 5:
        ends()
        global endor
        endor = 1
        if play == 1:
            lab["text"]='game over,AI2 win'
        else:
            lab["text"]='game over,AI1 win'
        cut = data[m+n*w]+3
        for i in range(5):
            end(number,m,n,max1,max2,cut)
            win.update()
            time.sleep(0.1)
        
        #end(number,m,n,max1,max2,data.iloc[m,n]+3)

def ends():
    global buttonlist
    for j in range(h):
        for i in range(w):
            buttonlist[i + j * w]['state']=DISABLED

def AIfirst():
    global play
    play = 1 - play
    i = random.choice([5,6,7,8,9,10])
    j = random.choice([5,6,7,8,9,10])
    data[i + j * w] = 1
    buttonlist[i + j * w].configure(bg = color(data[i + j * w]))

def starts():
    global buttonlist,play,endor
    endor = 0
    for j in range(h):
        for i in range(w):
            buttonlist[i + j * w]['state']=NORMAL
    play = int(tkinter.messagebox.askyesno('start','Do you want to get a head start?'))
    if play == 0:
        AIfirst()
    lab['text'] = 'player\'s turn'

def windows():#creat win window
    global win,lab,play,endor
    endor = 0
    play = int(tkinter.messagebox.askyesno('start','Do you want to get a head start?'))
    win = Tk()
    win.title('hello world')
    win.geometry('720x768')
    lab = Label(win,font=('Consolas', 24))
    lab['text'] = 'player\'s turn'
    lab.place(relx = 0,rely = 0,relheight = 1 / 16,relwidth = 1)

def updates():
    global buttonlist
    for j in range(h):
        for i in range(w):
            buttonlist[i + j * w].configure(bg = color(data[i + j * w]))
    
def clear(event):
    for j in range(h):
        for i in range(w):
            data[i + j * w] = 0
    starts()
    updates()

def end(kind,xx,yy,n1,n2,col):
    if kind == 1:
        for i in range(xx-n1,xx+n2):
            data[i + w * yy] = col - data[i + w * yy]
            buttonlist[i + w * yy].configure(bg = color(data[i + w * yy]))
    elif kind == 2:
        for i in range(yy-n1,yy+n2):
            data[xx + w * i] = col - data[xx + w * i]
            buttonlist[xx + w * i].configure(bg = color(data[xx + w * i]))
    elif kind == 3:
        for i in range(xx-n1,xx+n2):
            data[i + w * (i + yy - xx)] = col - data[i + w * (i + yy - xx)]
            buttonlist[i + w * (i + yy - xx)].configure(bg = color(data[i + w * (i + yy - xx)]))
    elif kind == 4:
        for i in range(xx-n1,xx+n2):
            data[i + w * (yy + xx - i)] = col - data[i + w * (yy + xx - i)]
            buttonlist[i + w * (yy + xx - i)].configure(bg = color(data[i + w * (yy + xx - i)]))
    #updates()
    

read()
windows()
output()
if play == 0:
    AIfirst()

win.bind('<space>',clear)
win.focus_set()
win.mainloop()