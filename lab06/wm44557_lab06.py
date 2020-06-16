import math
from math import log10, sqrt
from matplotlib import pyplot as plt

byte_array = "abc".encode()
binary_int = int.from_bytes(byte_array, "little")
binary_string = format(binary_int, "08b")
lista = list(binary_string)

# print(lista) #['1', '1', '0', '0', '0', '1']

N = 1
ts = 0.05

A1 = 0
A0 = 1.0
fi = math.pi
Tb = 0.1
fi0 = 0
fi1 = math.pi
A = 1
ft = N * pow(Tb, -1)
ft0 = (N + 1) / Tb
ft1 = (N + 2) / Tb

fs = 1000
Tbp = int(Tb*fs)


def za(m, tn, opcja):
    if ((m == '0') and (opcja == 0)):
        return A1 * math.sin(2 * math.pi * ft * tn + fi)
    else:
        return A0 * math.sin(2 * math.pi * ft * tn + fi)


def zf(m, tn, opcja):
    if ((m == '0') and (opcja == 0)):
        return A * math.sin(2 * math.pi * ft0 * tn + fi)
    else:
        return A * math.sin(2 * math.pi * ft1 * tn + fi)


def zp(m, tn, opcja):
    if ((m == '0') or (opcja == 10)):
        return A * math.sin(2 * math.pi * ft * tn + fi0)
    if(opcja == 11):
        return A * math.sin(2 * math.pi * ft * tn + fi1)
    else:
        return A * math.sin(2 * math.pi * ft * tn + fi1)


def funkcja1(funkcja, opcja):
    tZero = 0
    tN = 2.4
    deltaT = (1.0/fs)
    tn = tZero
    n = 0
    # To zadania 2 ustawiam tN na 2.4 ponieważ abc * 8 bitów to 2.4 ( eby wyświetlić cały sygnał)
    x = 0
    # do zadania 3 tn = 1
    tab = []
    tab2 = []
    while(tn <= tN):

        tab.append(tn)
        if(x < len(lista)-1):
            m = lista[x]
            tab2.append(funkcja(m, tn, opcja))
        else:
            tab2.append(0)

        if((Tb * (x + 1)) < tn):
            x = x+1

        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def mnozenie(Z_tablica, S_tablica):
    tZero = 0
    tN = 2.4
    deltaT = (1.0/fs)
    tn = tZero
    n = 0
    tab = []
    tab2 = []
    while(tn <= tN):
        tab.append(tn)
        tab2.append(Z_tablica[n]*S_tablica[n])
        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def calka(X_tablica):
    tZero = 0
    tN = 2.4
    deltaT = (1.0/fs)
    tn = tZero
    n = 0
    tab = []
    tab2 = []
    while(tn <= tN):
        tab.append(tn)
        var = X_tablica[n]
        for j in range(0, n % Tbp, 1):
            var = var + X_tablica[n-j]
        tab2.append(var)
        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def calkaFSK(X_tablica, X2_tablica):
    tZero = 0
    tN = 2.4
    deltaT = (1.0/fs)
    tn = tZero
    n = 0
    tab = []
    tab2 = []
    while(tn <= tN):
        tab.append(tn)
        var = X_tablica[n]
        var2 = X2_tablica[n]
        for j in range(0, n % Tbp, 1):
            var = var + X_tablica[n-j]
            var2 = var2 + X2_tablica[n-j]
        tab2.append(var-var2)
        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def end(P_tablica, H):
    tZero = 0
    tN = 2.4
    deltaT = (1.0/fs)
    tn = tZero
    n = 0
    tab = []
    tab2 = []
    while(tn <= tN):
        tab.append(tn)
        if(P_tablica[n] > H):
            tab2.append(1)
        else:
            tab2.append(0)
        tn = tZero + (n * deltaT)
        n = n + 1
    return tab, tab2


def wyswietlanie(nazwa, ylabel, sygnal):
    plt.plot(ylabel, sygnal)
    plt.title(nazwa)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.show()
    return


tab, tab2 = funkcja1(za, 0)
tabb, tabb2 = funkcja1(zf, 0)
tabbb, tabbb2 = funkcja1(zp, 0)

tab_s, tab2_s = funkcja1(za, 1)
tabb_s, tabb2_s = funkcja1(zf, 1)
tabbb_s, tabbb2_s = funkcja1(zp, 10)  # bo tutaj biorę sf1(t)
fsk_, fsk_2 = funkcja1(zp, 11)  # fsk2

tab_xs, tab2_xs = mnozenie(tab2, tab2_s)
tabb_xs, tabb2_xs = mnozenie(tabb2, tabb2_s)
tabbb_xs, tabbb2_xs = mnozenie(tabbb2, tabbb2_s)
fsk_s, fsk_s2 = mnozenie(tabbb2, fsk_2)

tab_calka, tab2_calka = calka(tab2_xs)
tabb_calka, tabb2_calka = calka(tabb2_xs)
tabbb_calka, tabbb2_calka = calka(tabbb2_xs)
fsk_calka, fsk2_calka = calkaFSK(tabbb2_xs, fsk_s2)  # fsk sf1 - sf2


tab_end, tab2_end = end(tab2_calka, 10)  # wysokość 10
tabb_end, tabb2_end = end(tabb2_calka, 20)  # wysokość 20
tabbb_end, tabbb2_end = end(fsk2_calka, -10)  # - 10 bo rysuje do góry nogami

# FSK sf1 - sf2


wyswietlanie('ASK: z(t)', tab, tab2)
wyswietlanie('ASK MNOŻENIE: x(t)', tab_xs, tab2_xs)
wyswietlanie('ASK CAŁKA: p(t)', tab_calka, tab2_calka)
wyswietlanie('ASK END: m(t)', tab_end, tab2_end)

wyswietlanie('PSK: z(t)', tabb, tabb2)
wyswietlanie('PSK MNOŻENIE: x(t)', tabb_xs, tabb2_xs)
wyswietlanie('PSK CAŁKA: p(t)', tabb_calka, tabb2_calka)
wyswietlanie('PSK END: m(t)', tabb_end, tabb2_end)

wyswietlanie('FSK: z(t)', tabbb, tabbb2)
wyswietlanie('FSK MNOŻENIE: x(t)', tabbb_xs, tabbb2_xs)
wyswietlanie('FSK CAŁKA: p(t)', tabbb_calka, tabbb2_calka)
wyswietlanie('FSK CAŁKA: sf1 - sf2', fsk_calka, fsk2_calka)
wyswietlanie('FSK END: m(t)', tabbb_end, tabbb2_end)
