
#coding=utf-8
#AI
#target :blank
import random

def f(x,y):
    match x:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 4
        case 3:
            return 9^(y-1)
        case 4:
            return 64^y
        case _:
            return 625^y

def weight(x,y):#b1:player
    a1, b1 = 10, 13
    return judge(x,y,1) * a1 + judge(x,y,2) * b1

#1:AI 2:player
def judge(m,n,x):
    grade= 0
    num1,num2,blank = -1,0,0
    data[m + w * n] = x
    for i in range(m,-1,-1):
        if data[i + w * n] == x:
            num1 += 1
        else:
            if data[i + w * n] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if data[i + w * n] == x:
            num2 += 1
        else:
            if data[i + w * n] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f(num1 + num2,blank)
    num1,num2,blank = -1,0,0#y
    for i in range(n,-1,-1):
        if data[m + w * i] == x:
            num1 += 1
        else:
            if data[m + w * i] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(n,h):
        if data[m + w * i] == x:
            num2 += 1
        else:
            if data[m + w * i] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f(num1 + num2,blank)
    num1,num2,blank = -1,0,0#x = y
    for i in range(m,-1,-1):
        if data[i + w * (i + n - m)] == x:
            num1 += 1
        else:
            if data[i + w * (i + n - m)] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if n - m + i >= 15 or n - m + i < 0:
            break
        if data[i + w * (i + n - m)] == x:
            num2 += 1
        else:
            if data[i + w * (i + n - m)] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f(num1 + num2,blank)
    num1,num2,blank = -1,0,0#x = -y
    for i in range(m,-1,-1):
        if m + n - i >= 15 or m + n - i < 0:
            break
        if data[i + w * (n + m - i)] == x:
            num1 += 1
        else:
            if data[i + w * (n + m - i)] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if data[i + w * (n + m - i)] == x:
            num2 += 1
        else:
            if data[i + w * (n + m - i)] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f(num1 + num2,blank)
    data[m + w * n] = 0
    return grade

def max():
    xx,yy,weight1 = 0,0,0
    wei = 0
    for j in range(h):
        for i in range(w):
            if data[i + w * j] == 0:
                wei = weight(i,j)
                if weight1 < wei:
                    weight1,xx,yy = wei,i,j
                if weight1 == wei and random.choice(range(100)) < 15:
                    weight1,xx,yy = wei,i,j
    return xx + yy * w

def main(x):
    global data,h,w
    data, h, w= x, 15, 15
    return max()
#ai2
def f1(x,y):
    match x:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 4
        case 3:
            return 9
        case 4:
            return 64
        case _:
            return 625

def weight1(x,y):#b1:player
    a1, b1 = 10, 13
    return judge1(x,y,1) * a1 + judge1(x,y,2) * b1

#1:AI2
def judge1(m,n,x):
    grade= 0
    num1,num2,blank = -1,0,0
    data[m + w * n] = x
    for i in range(m,-1,-1):
        if data[i + w * n] == x:
            num1 += 1
        else:
            if data[i + w * n] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if data[i + w * n] == x:
            num2 += 1
        else:
            if data[i + w * n] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f1(num1 + num2,blank)
    num1,num2,blank = -1,0,0#y
    for i in range(n,-1,-1):
        if data[m + w * i] == x:
            num1 += 1
        else:
            if data[m + w * i] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(n,h):
        if data[m + w * i] == x:
            num2 += 1
        else:
            if data[m + w * i] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f1(num1 + num2,blank)
    num1,num2,blank = -1,0,0#x = y
    for i in range(m,-1,-1):
        if data[i + w * (i + n - m)] == x:
            num1 += 1
        else:
            if data[i + w * (i + n - m)] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if n - m + i >= 15 or n - m + i < 0:
            break
        if data[i + w * (i + n - m)] == x:
            num2 += 1
        else:
            if data[i + w * (i + n - m)] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f1(num1 + num2,blank)
    num1,num2,blank = -1,0,0#x = -y
    for i in range(m,-1,-1):
        if m + n - i >= 15 or m + n - i < 0:
            break
        if data[i + w * (n + m - i)] == x:
            num1 += 1
        else:
            if data[i + w * (n + m - i)] == 0 and num1 != 0:
                blank = blank + 1
            break
    for i in range(m,w):
        if data[i + w * (n + m - i)] == x:
            num2 += 1
        else:
            if data[i + w * (n + m - i)] == 0 and num2 != 1 or num1 != 0:
                blank = blank + 1
            break
    grade += f1(num1 + num2,blank)
    data[m + w * n] = 0
    return grade

def max1():
    xx,yy,weight2 = 0,0,0
    wei = 0
    for j in range(h):
        for i in range(w):
            if data[i + w * j] == 0:
                wei = weight1(i,j)
                if weight2 < wei:
                    weight2,xx,yy = wei,i,j
                if weight2 == wei and random.choice(range(100)) < 15:
                    weight2,xx,yy = wei,i,j
    return xx + yy * w

def main1(x):
    global data,h,w
    data, h, w= x, 15, 15
    return max1()