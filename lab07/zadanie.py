import math
from math import log10, sqrt

from matplotlib import pyplot as plt

byte_array = "kot".encode()

binary_int = int.from_bytes(byte_array, "little")
binary_string = format(binary_int, "08b")
#lista = list(binary_string)
fi = math.pi * 5
A = 1.0
fs = 100
Tb = 0.1


def ASCII(tekst):
    napis = ''
    for x in tekst:
        napis = napis+bin(ord(x))[2:].zfill(8)
    return list(map(int, list(napis)))


lista = ASCII('kot')


def sT(t):
    return -A * math.sin((2*math.pi * 10 * t) + fi)


def CLK(funkcja, lista):
    tZero = 0
    tN = 1.6
    deltaT = (1.0/100)
    tn = tZero
    n = 0
    x = 0
    tab = []
    tab2 = []
    while(tn < tN):

        tab.append(tn)
        if(funkcja(tn) > 0.00001):
            tab2.append(1)
        else:
            tab2.append(0)

        if((Tb * (x + 1)) < tn):
            x = x+1

        tn = tZero + (n * deltaT)
        n = n + 1

    return tab, tab2


def funkcja(lista):
    tZero = 0
    tN = 1.6
    deltaT = (1.0/1000)
    tn = tZero
    n = 0
    x = 0
    tab = []
    tab2 = []
    while(tn <= tN):

        tab.append(tn)
        if(x < len(lista)-1):
            tab2.append(lista[x])
        else:
            tab2.append(0)

        if((Tb * (x + 1)) < tn):
            x = x+1

        tn = tZero + (n * deltaT)
        n = n + 1

    return tab, tab2


print(lista)

#
tabCLK, tab2CLK = CLK(sT, lista)
# plt.plot(tabCLK, tab2CLK)
# plt.figure()
tabTTL, tab2TTL = funkcja(lista)

# plt.plot(tabTTL, tab2TTL)
# plt.gca().invert_yaxis()


# plt.show()

# clk[i]>clk[i+1] i ttl=1 to


def nrzi(clk, ttl):
    tZero = 0
    tN = 1.6
    deltaT = (1.0/1000)
    tn = tZero
    n = 0
    xd = 0
    x = 0
    tab = []
    tab2 = []
    zmiana = 1
    while(tn <= tN):
        tab.append(tn)

        if((clk[x*10] == 1) and (clk[x*10+1] == 0)):
            if((ttl[x] == 1) or (ttl[x] == -1)):
                tab2.append(ttl[x]*(-1))
                zmiana = ttl[x]*(-1)
            else:
                tab2.append(zmiana)

        elif((clk[x] == 0) and (clk[x-1] == 1)):
            if((ttl[x] == 1) or (ttl[x] == -1)):
                tab2.append(ttl[x]*(-1))
                zmiana = ttl[x]*(-1)
            else:
                tab2.append(zmiana)

        else:
            tab2.append(zmiana)

        if((Tb * (xd + 1)) < tn):
            xd = xd+1
        if(x < len(clk)):
            x = x+1
        tn = tZero + (n * deltaT)

        n = n + 1
    return tab, tab2


# tabNRZI, tab2NRZI = nrzi(tab2CLK, tab2TTL)
plt.gca().invert_yaxis()

plt.plot(tabTTL, tab2TTL)
plt.show()
