from time import time
import random

def gen1(x):
    a = 5**5
    m = (2**35)-1
    return ((a*x)%(m)),((a*x)%(m))/(float(m))

def gen2(x):
    return (((7**5)*x)%((2**31)-1)),(((7**5)*x)%((2**31)-1))/(2**31-1)

#Get from: https://appdividend.com/2022/06/23/how-to-calculate-a-percentage-in-python/
def calc_porcentaje(part, alls):
  return str(100 * float(part)/float(alls)) + "%"

x = time()

print("Simulacion, 100 iteraciones")
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
print("Generador 1")
alls = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print(alls)
print("0.0-0.1: ","*"*(cont1),cont1,calc_porcentaje(cont1,alls))
print("0.1-0.2: ","*"*(cont2),cont2,calc_porcentaje(cont2,alls))
print("0.2-0.3: ","*"*(cont3),cont3,calc_porcentaje(cont3,alls))
print("0.3-0.4: ","*"*(cont4),cont4,calc_porcentaje(cont4,alls))
print("0.4-0.5: ","*"*(cont5),cont5,calc_porcentaje(cont5,alls))
print("0.5-0.6: ","*"*(cont6),cont6,calc_porcentaje(cont6,alls))
print("0.6-0.7: ","*"*(cont7),cont7,calc_porcentaje(cont7,alls))
print("0.7-0.8: ","*"*(cont8),cont8,calc_porcentaje(cont8,alls))
print("0.8-0.9: ","*"*(cont9),cont9,calc_porcentaje(cont9,alls))
print("0.9-1.0: ","*"*(cont10), cont10,calc_porcentaje(cont10,alls))

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
print("Generador 2")
alls = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print("0.0-0.1: ","*"*(cont1),cont1,calc_porcentaje(cont1,alls))
print("0.1-0.2: ","*"*(cont2),cont2,calc_porcentaje(cont2,alls))
print("0.2-0.3: ","*"*(cont3),cont3,calc_porcentaje(cont3,alls))
print("0.3-0.4: ","*"*(cont4),cont4,calc_porcentaje(cont4,alls))
print("0.4-0.5: ","*"*(cont5),cont5,calc_porcentaje(cont5,alls))
print("0.5-0.6: ","*"*(cont6),cont6,calc_porcentaje(cont6,alls))
print("0.6-0.7: ","*"*(cont7),cont7,calc_porcentaje(cont7,alls))
print("0.7-0.8: ","*"*(cont8),cont8,calc_porcentaje(cont8,alls))
print("0.8-0.9: ","*"*(cont9),cont9,calc_porcentaje(cont9,alls))
print("0.9-1.0: ","*"*(cont10), cont10,calc_porcentaje(cont10,alls))


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
print("Generador 3")
alls = cont1 + cont2 + cont3 + cont4 + cont5 + cont6 + cont7 + cont8 + cont9 + cont10
print("0.0-0.1: ","*"*(cont1),cont1,calc_porcentaje(cont1,alls))
print("0.1-0.2: ","*"*(cont2),cont2,calc_porcentaje(cont2,alls))
print("0.2-0.3: ","*"*(cont3),cont3,calc_porcentaje(cont3,alls))
print("0.3-0.4: ","*"*(cont4),cont4,calc_porcentaje(cont4,alls))
print("0.4-0.5: ","*"*(cont5),cont5,calc_porcentaje(cont5,alls))
print("0.5-0.6: ","*"*(cont6),cont6,calc_porcentaje(cont6,alls))
print("0.6-0.7: ","*"*(cont7),cont7,calc_porcentaje(cont7,alls))
print("0.7-0.8: ","*"*(cont8),cont8,calc_porcentaje(cont8,alls))
print("0.8-0.9: ","*"*(cont9),cont9,calc_porcentaje(cont9,alls))
print("0.9-1.0: ","*"*(cont10), cont10,calc_porcentaje(cont10,alls))
x = time()

print("Simulacion, 5000 iteraciones")
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

for i in range(5000):
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
    x = new
print("Generador 1")
print("0.0-0.1: ","*"*int((cont1/10)),cont1,calc_porcentaje(cont1,5000))
print("0.1-0.2: ","*"*int((cont2/10)),cont2,calc_porcentaje(cont2,5000))
print("0.2-0.3: ","*"*int((cont3/10)),cont3,calc_porcentaje(cont3,5000))
print("0.3-0.4: ","*"*int((cont4/10)),cont4,calc_porcentaje(cont4,5000))
print("0.4-0.5: ","*"*int((cont5/10)),cont5,calc_porcentaje(cont5,5000))
print("0.5-0.6: ","*"*int((cont6/10)),cont6,calc_porcentaje(cont6,5000))
print("0.6-0.7: ","*"*int((cont7/10)),cont7,calc_porcentaje(cont7,5000))
print("0.7-0.8: ","*"*int((cont8/10)),cont8,calc_porcentaje(cont8,5000))
print("0.8-0.9: ","*"*int((cont9/10)),cont9,calc_porcentaje(cont9,5000))
print("0.9-1.0: ","*"*int((cont10/10)), cont10,calc_porcentaje(cont10,5000))
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
for i in range(5000):
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
print("Generador 2")
print("0.0-0.1: ","*"*int((cont1/10)),cont1,calc_porcentaje(cont1,5000))
print("0.1-0.2: ","*"*int((cont2/10)),cont2,calc_porcentaje(cont2,5000))
print("0.2-0.3: ","*"*int((cont3/10)),cont3,calc_porcentaje(cont3,5000))
print("0.3-0.4: ","*"*int((cont4/10)),cont4,calc_porcentaje(cont4,5000))
print("0.4-0.5: ","*"*int((cont5/10)),cont5,calc_porcentaje(cont5,5000))
print("0.5-0.6: ","*"*int((cont6/10)),cont6,calc_porcentaje(cont6,5000))
print("0.6-0.7: ","*"*int((cont7/10)),cont7,calc_porcentaje(cont7,5000))
print("0.7-0.8: ","*"*int((cont8/10)),cont8,calc_porcentaje(cont8,5000))
print("0.8-0.9: ","*"*int((cont9/10)),cont9,calc_porcentaje(cont9,5000))
print("0.9-1.0: ","*"*int((cont10/10)), cont10,calc_porcentaje(cont10,5000))
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
for i in range(5000):
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
print("Generador 3")
print("0.0-0.1: ","*"*int((cont1/10)),cont1,calc_porcentaje(cont1,5000))
print("0.1-0.2: ","*"*int((cont2/10)),cont2,calc_porcentaje(cont2,5000))
print("0.2-0.3: ","*"*int((cont3/10)),cont3,calc_porcentaje(cont3,5000))
print("0.3-0.4: ","*"*int((cont4/10)),cont4,calc_porcentaje(cont4,5000))
print("0.4-0.5: ","*"*int((cont5/10)),cont5,calc_porcentaje(cont5,5000))
print("0.5-0.6: ","*"*int((cont6/10)),cont6,calc_porcentaje(cont6,5000))
print("0.6-0.7: ","*"*int((cont7/10)),cont7,calc_porcentaje(cont7,5000))
print("0.7-0.8: ","*"*int((cont8/10)),cont8,calc_porcentaje(cont8,5000))
print("0.8-0.9: ","*"*int((cont9/10)),cont9,calc_porcentaje(cont9,5000))
print("0.9-1.0: ","*"*int((cont10/10)), cont10,calc_porcentaje(cont10,5000))
x = time()

print("Simulacion, 100000 iteraciones")
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

for i in range(100000):
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
print("Generador 1")
#print(cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10)
print("0.0-0.1: ","*"*int((cont1/100)),cont1,calc_porcentaje(cont1,100000))
print("0.1-0.2: ","*"*int((cont2/100)),cont2,calc_porcentaje(cont2,100000))
print("0.2-0.3: ","*"*int((cont3/100)),cont3,calc_porcentaje(cont3,100000))
print("0.3-0.4: ","*"*int((cont4/100)),cont4,calc_porcentaje(cont4,100000))
print("0.4-0.5: ","*"*int((cont5/100)),cont5,calc_porcentaje(cont5,100000))
print("0.5-0.6: ","*"*int((cont6/100)),cont6,calc_porcentaje(cont6,100000))
print("0.6-0.7: ","*"*int((cont7/100)),cont7,calc_porcentaje(cont7,100000))
print("0.7-0.8: ","*"*int((cont8/100)),cont8,calc_porcentaje(cont8,100000))
print("0.8-0.9: ","*"*int((cont9/100)),cont9,calc_porcentaje(cont9,100000))
print("0.9-1.0: ","*"*int((cont10/100)), cont10,calc_porcentaje(cont10,100000))

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
for i in range(100000):
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
print("Generador 2")
#print(cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10)
print("0.0-0.1: ","*"*int((cont1/100)),cont1,calc_porcentaje(cont1,100000))
print("0.1-0.2: ","*"*int((cont2/100)),cont2,calc_porcentaje(cont2,100000))
print("0.2-0.3: ","*"*int((cont3/100)),cont3,calc_porcentaje(cont3,100000))
print("0.3-0.4: ","*"*int((cont4/100)),cont4,calc_porcentaje(cont4,100000))
print("0.4-0.5: ","*"*int((cont5/100)),cont5,calc_porcentaje(cont5,100000))
print("0.5-0.6: ","*"*int((cont6/100)),cont6,calc_porcentaje(cont6,100000))
print("0.6-0.7: ","*"*int((cont7/100)),cont7,calc_porcentaje(cont7,100000))
print("0.7-0.8: ","*"*int((cont8/100)),cont8,calc_porcentaje(cont8,100000))
print("0.8-0.9: ","*"*int((cont9/100)),cont9,calc_porcentaje(cont9,100000))
print("0.9-1.0: ","*"*int((cont10/100)), cont10,calc_porcentaje(cont10,100000))

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
for i in range(100000):
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
print("Generador 3")
#print(cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10)
print("0.0-0.1: ","*"*int((cont1/100)),cont1,calc_porcentaje(cont1,100000))
print("0.1-0.2: ","*"*int((cont2/100)),cont2,calc_porcentaje(cont2,100000))
print("0.2-0.3: ","*"*int((cont3/100)),cont3,calc_porcentaje(cont3,100000))
print("0.3-0.4: ","*"*int((cont4/100)),cont4,calc_porcentaje(cont4,100000))
print("0.4-0.5: ","*"*int((cont5/100)),cont5,calc_porcentaje(cont5,100000))
print("0.5-0.6: ","*"*int((cont6/100)),cont6,calc_porcentaje(cont6,100000))
print("0.6-0.7: ","*"*int((cont7/100)),cont7,calc_porcentaje(cont7,100000))
print("0.7-0.8: ","*"*int((cont8/100)),cont8,calc_porcentaje(cont8,100000))
print("0.8-0.9: ","*"*int((cont9/100)),cont9,calc_porcentaje(cont9,100000))
print("0.9-1.0: ","*"*int((cont10/100)), cont10,calc_porcentaje(cont10,100000))