import math

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = math.sqrt(t) if t>0 else complex(0,math.sqrt(abs(t))) ##因為複數的英文就是 complex number，所以在Python要表示複數就可以使用：complex(x, y)來表示。x代表實部的數字，y代表虛部的數字。

    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]


print("root of 1x^2+4x+0=", root2(1,4,0))
