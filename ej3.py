from time import time
import random

def gen1(x):
    a = 5**5
    m = (2**35)-1
    return ((a*x)%(m)),((a*x)%(m))/(float(m))

def gen2(x):
    return (((7**5)*x)%((2**31)-1)),(((7**5)*x)%((2**31)-1))/(2**31-1)

x = time()

cont1 =0
cont2 =0
cont3 =0
cont4 =0
cont5 =0
cont6 =0
cont7 =0
cont8 =0
cont9 =0
cont10 =0

for i in range(100):
    #print("Vino x:", x)
    new = gen1(x)[0]
    hist = gen1(x)[1]
    if hist <=0.1 and hist >=0.0:
        cont1 += 1
    elif hist <=0.2 and hist >0.1:
        cont2 += 1
    elif hist <=0.3 and hist >0.2:
        cont3 += 1
    elif hist <=0.4 and hist >0.3:
        cont4 += 1
    elif hist <=0.5 and hist >0.4:
        cont5 += 1
    elif hist <=0.6 and hist >0.5:
        cont6 += 1
    elif hist <=0.7 and hist >0.6:
        cont7 += 1
    elif hist <=0.8 and hist >0.7:
        cont8 += 1
    elif hist <=0.9 and hist >0.8:
        cont9 += 1
    elif hist <=1.0 and hist >0.9:
        cont10 += 1
    #print("new value: ",new)
    x = new

print(cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10)

cont1 =0
cont2 =0
cont3 =0
cont4 =0
cont5 =0
cont6 =0
cont7 =0
cont8 =0
cont9 =0
cont10 =0
for i in range(100):
    #print("Vino x:", x)
    new = gen2(x)[0]
    hist = gen2(x)[1]
    if hist <=0.1 and hist >=0.0:
        cont1 += 1
    elif hist <=0.2 and hist >0.1:
        cont2 += 1
    elif hist <=0.3 and hist >0.2:
        cont3 += 1
    elif hist <=0.4 and hist >0.3:
        cont4 += 1
    elif hist <=0.5 and hist >0.4:
        cont5 += 1
    elif hist <=0.6 and hist >0.5:
        cont6 += 1
    elif hist <=0.7 and hist >0.6:
        cont7 += 1
    elif hist <=0.8 and hist >0.7:
        cont8 += 1
    elif hist <=0.9 and hist >0.8:
        cont9 += 1
    elif hist <=1.0 and hist >0.9:
        cont10 += 1
    #print("new value: ",new)
    x = new

print(cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10)
cont1 =0
cont2 =0
cont3 =0
cont4 =0
cont5 =0
cont6 =0
cont7 =0
cont8 =0
cont9 =0
cont10 =0
for i in range(100):
    #print("Vino x:", x)
    new = random.random()
    hist = new
    if hist <=0.1 and hist >=0.0:
        cont1 += 1
    elif hist <=0.2 and hist >0.1:
        cont2 += 1
    elif hist <=0.3 and hist >0.2:
        cont3 += 1
    elif hist <=0.4 and hist >0.3:
        cont4 += 1
    elif hist <=0.5 and hist >0.4:
        cont5 += 1
    elif hist <=0.6 and hist >0.5:
        cont6 += 1
    elif hist <=0.7 and hist >0.6:
        cont7 += 1
    elif hist <=0.8 and hist >0.7:
        cont8 += 1
    elif hist <=0.9 and hist >0.8:
        cont9 += 1
    elif hist <=1.0 and hist >0.9:
        cont10 += 1
    #print("new value: ",new)

print(cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, cont10)