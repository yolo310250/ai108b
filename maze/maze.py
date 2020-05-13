import numpy as np

def matrixPrint(m):
    i = 0
    j = 0
    for i in range(6):
        for j in range(8):
            print(m[i][j],end='')
        print()

def findPath(m,x,y):
    print("=========================")
    print("x=", x, " y=", y,)
    matrixPrint(m)
    if x>=6 or y>=8 :return False  
    if m[x][y] == '*' :return False  
    if m[x][y] == '+' :return False  
    if m[x][y] == ' ' :m[x][y]='.'  
    if m[x][y] == '.'  and (x == 5  or  y==7) : 
        return True
    if y<7 and m[x][y+1]==' ' : 
        m[x][y]='.'
        if findPath(m, x,y+1) :return True #向右
    if x<5 and m[x+1][y]==' ' :
        m[x][y]='.'
        if findPath(m, x+1,y) :return True #往上
    if y>0 and m[x][y-1]==' ':
        m[x][y]=''
        if findPath(m, x,y-1) :return True #往左
    if x>0 and m[x-1][y]==' ' :
        m[x][y]='.'
        if findPath(m, x-1,y) :return True #往下
    m[x][y]=' '
    return False



m=(['*','*','*','*','*','*','*','*']
    ,[' ',' ','*','*','*','*','*','*']
    ,['*',' ',' ',' ',' ',' ',' ','*']
    ,['*','*','*','*',' ','*','*','*']
    ,['*','*',' ',' ',' ',' ','*','*']
    ,['*','*','*',' ','*','*','*','*'])
findPath(m, 1, 0)
print("=========================")
matrixPrint(m)