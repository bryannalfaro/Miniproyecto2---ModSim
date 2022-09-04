import matplotlib.pyplot as plt
import math
import numpy as np


def f1(x):
    return 1 - math.e**(-2 * x)


def f2(x):
    return math.e**(-x)


def integralF(n):
    x = np.random.uniform(0, 10, n)
    y = np.random.uniform(0, 0.25, n)
    count = []
    negCounts = []
    for i in range(n):
        if y[i] <= f1(x[i]) + f2(x[i]) - 1:
            count.append((x[i], y[i]))
        else:
            negCounts.append((x[i], y[i]))
    convergence = (2.5) * (len(count) / n)
    return x, y, count, negCounts, convergence


resultado1 = integralF(100)
plt.plot([x for x, y in resultado1[2]], [y for x, y in resultado1[2]],
         color='blue',
         marker='.',
         linestyle='none')
plt.plot([x for x, y in resultado1[3]], [y for x, y in resultado1[3]],
         color='red',
         marker='.',
         linestyle='none')

ln = np.linspace(0, 10, 100)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(ln, f2(ln) + f1(ln) - 1)
plt.show()

print("Convergencia con 100 iteraciones")
print(resultado1[4])


#10000 iteraciones
resultado2 = integralF(10000)
plt.plot([x for x, y in resultado2[2]], [y for x, y in resultado2[2]],
         color='blue',
         marker='.',
         linestyle='none')
plt.plot([x for x, y in resultado2[3]], [y for x, y in resultado2[3]],
         color='red',
         marker='.',
         linestyle='none')

ln = np.linspace(0, 10, 10000)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(ln, f2(ln) + f1(ln) - 1)
plt.show()

print("Convergencia con 10000 iteraciones")
print(resultado2[4])

#100000 iteraciones
resultado3 = integralF(100000)
plt.plot([x for x, y in resultado3[2]], [y for x, y in resultado3[2]],
         color='blue')
plt.plot([x for x, y in resultado3[3]], [y for x, y in resultado3[3]],
         color='red',
         marker='.',
         linestyle='none')

ln = np.linspace(0, 10, 100000)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(ln, f2(ln) + f1(ln) - 1)
plt.show()

print("Convergencia con 10000 iteraciones")
print(resultado3[4])

