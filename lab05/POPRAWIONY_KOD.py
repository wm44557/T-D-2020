import math
from math import log10, sqrt

from matplotlib import pyplot as plt

byte_array = "abc".encode()

binary_int = int.from_bytes(byte_array, "little")
binary_string = format(binary_int, "08b")
lista = list(binary_string)

# print(lista) #['1', '1', '0', '0', '0', '1']

# ZAD.2

# N=2  # zad.3
N = 1  # zad.2
ts = 0.05

ft = 2.0
X_re = []
X_im = []
M = []
M_prim = []
x = []
tab2 = []
fk = []

A1 = 0
A0 = 1.0
fi = math.pi
Tb = 0.1
fi0 = 0
fi1 = math.pi
A = 1
ft = N/Tb
ft0 = (N + 1) / Tb
ft1 = (N + 2) / Tb


def za(m, tn):
    if (m == '0'):
        return A1 * math.sin(2 * math.pi * ft * tn + fi)
    else:
        return A0 * math.sin(2 * math.pi * ft * tn + fi)


def zf(m, tn):
    if (m == '0'):
        return A * math.sin(2 * math.pi * ft0 * tn + fi)
    else:
        return A * math.sin(2 * math.pi * ft1 * tn + fi)


def zp(m, tn):
    if (m == '0'):
        return A * math.sin(2 * math.pi * ft * tn + fi0)
    else:
        return A * math.sin(2 * math.pi * ft * tn + fi1)


def funkcja1(funkcja):
    tZero = 0
    tN = 2.4
    # tN = 1
    deltaT = (1.0/1000)
    tn = tZero
    n = 0
    # To zadania 2 ustawiam tN na 2.4 ponieważ abc * 8 bitów to 2.4 ( eby wyświetlić cały sygnał)
    x = 0
    # do zadania 3 tn = 1
    tab = []
    tab2 = []
    tab2.append(0)
    tab.append(0)
    while(tn <= tN):
        if((Tb * (x + 1)) < tn):
            x = x+1
        tab.append(tn)

        if(x < len(lista)-1):
            m = lista[x]
            tab2.append(funkcja(m, tn))
        else:
            tab2.append(0)
        # if((tab2[len(tab2)-2] > 0) and(tab2[len(tab2)-1] <= 0)):
        #     tab2[len(tab2)-1] = 0

            # tab2[len(tab2)-1] = 0

        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def DFT(tab, tab2):
    # Wypełnienie tablic zerami
    N = len(tab)
    for i in range(N):
        X_re.append(0.0)
        X_im.append(0.0)
        M.append(0.0)
        fk.append(i * (10000/N))  # skala częstotliwości wektor z krokiem fs/N


# Suma
    for k in range(N):
        for nn in range(N):
            X_re[k] = X_re[k] + \
                (tab2[nn] * math.cos((-2 * (math.pi * k * nn))/N))
            X_im[k] = X_im[k] + \
                (tab2[nn] * math.sin((-2 * (math.pi * k * nn))/N))


# Widmo
    for jj in range(N):
        M[jj] = sqrt(X_re[jj] * X_re[jj] + X_im[jj]
                     * X_im[jj])  # widmo amplitudowe

    threshold = abs(max(M))/10000

    for j in range(N):
        ''' Zastosowanie thresholda'''
        if (abs(M[j]) < threshold):
            M[j] = 0

    for y in range(N):
        if(M[y] != 0):
            # Amplituda w skali decybbelowej przemnozona przez 2/N
            M_prim.append(10 * log10(M[y])*2/N)
        else:
            M_prim.append(0)  # zabezpieczenie przed log 0

    plt.title('DFT FSK')
    plt.xlabel('f[hz]')
    plt.ylabel('A')
    # plt.figure()
    plt.plot(fk, M_prim)
    # zad.5
    W2 = max(tab2)-min(tab2)
    print(W2)
    # Dla za 1.9960534568565447
    # Dla zf 2.0
    # Dla zp 1.9960534568565447


tab, tab2 = funkcja1(za)
# plt.plot(tab, tab2)
# plt.title("ASK")
# plt.ylabel('zASK(t)')
# plt.xlabel('t(s)')
# plt.figure()

tabb, tabb2 = funkcja1(zf)
# plt.plot(tabb, tabb2)
# plt.title("FSK")
# plt.ylabel('zFSK(t)')
# plt.xlabel('t(s)')
# plt.figure()

tabbb, tabbb2 = funkcja1(zp)
# plt.plot(tabbb, tabbb2)
# plt.title("PSK")
# plt.ylabel('zPSK(t)')
# plt.xlabel('t(s)')
# plt.figure()

DFT(tabbb, tabbb2)
# DFT(tabb,tabb2)
# DFT(tabbb,tabbb2)
# plt.xlabel('f')
# plt.ylabel('f(t)')
# plt.plot(tab,tab2)
# plt.figure()
# plt.xlabel('f')
# plt.ylabel('f(t)')
# plt.plot(tabb,tabb2)
# plt.figure()
# plt.xlabel('f')
# plt.ylabel('f(t)')
# plt.plot(tabbb,tabbb2)
# plt.figure()
plt.show()
