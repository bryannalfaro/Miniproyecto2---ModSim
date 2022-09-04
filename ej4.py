import numpy as np
import math
import matplotlib.pyplot as plt


def operation(x):
    res = math.e**(-x**2)
    return res

def integral(n):
    x = np.random.uniform(-5, 5, n)
    y = np.random.uniform(0, 1, n)
    mask = (y <= operation(x))
    count = 0
    for i in range(0, len(list(y))):
        if list(y)[i] <= list(operation(x))[i]:
            count += 1
    convergence = count * 10 / float(n) 

    return convergence, x, y, mask

x = np.linspace(-5, 5, 100)
plt.plot(x, operation(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()


#100 iteraciones
resultado1 = integral(100)
plt.plot(resultado1[1], resultado1[2], '.', color='blue')
plt.plot(resultado1[1][resultado1[3]],
         resultado1[2][resultado1[3]],
         '.',
         color='red')

plt.plot(x, operation(x))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

print("Convergencia con 100 iteraciones")
print(resultado1[0])


#10000 iteraciones
resultado2 = integral(10000)
plt.plot(resultado2[1], resultado2[2], '.', color='blue')
plt.plot(resultado2[1][resultado2[3]],
         resultado2[2][resultado2[3]],
         '.',
         color='red')

plt.plot(x, operation(x))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()


#100000 iteraciones
print("Convergencia con 10000 iteraciones")
print(resultado2[0])

resultado3 = integral(100000)
plt.plot(resultado3[1], resultado3[2], '.', color='blue')
plt.plot(resultado3[1][resultado3[3]],
         resultado3[2][resultado3[3]],
         '.',
         color='red')

plt.plot(x, operation(x))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

print("Convergencia con 100000 iteraciones")
print(resultado3[0])