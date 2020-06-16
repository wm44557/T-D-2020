import random

_iterator = 0


def ASCII(tekst):
    napis = ''
    for x in tekst:
        napis = napis+bin(ord(x))[2:].zfill(8)
    return list(map(int, list(napis)))


def podzialNaCztery(iterator):
    tab = []

    for i in range(_len):
        tab.append([])
        for y in range(4):
            tab[i].append(binary[iterator])
            iterator = iterator+1
    return tab


def Hamming(slowoBinarne, _len):
    tab = []
    tab = slowoBinarne
    for i in range(_len):
        p1 = (tab[i][0] + tab[i][1] + tab[i][3]) % 2
        p2 = (tab[i][0] + tab[i][2] + tab[i][3]) % 2
        p3 = (tab[i][1] + tab[i][2] + tab[i][3]) % 2
        # print("p1-> ", p1, "p2-> ", p2, "p3-> ", p3)
        tab[i].insert(0, p1)
        tab[i].insert(1, p2)
        tab[i].insert(3, p3)
        p1 = []
        p2 = []
        p3 = []
    return tab


def Hamming2(slowoBinarne, _len):
    tab = []
    tab = slowoBinarne
    for i in range(_len):
        p1 = (tab[i][0] + tab[i][1] + tab[i][3]) % 2
        p2 = (tab[i][0] + tab[i][2] + tab[i][3]) % 2
        p3 = (tab[i][1] + tab[i][2] + tab[i][3]) % 2
        # print("p1-> ", p1, "p2-> ", p2, "p3-> ", p3)
        tab[i].insert(0, p1)
        tab[i].insert(1, p2)
        tab[i].insert(3, p3)
        p1 = []
        p2 = []
        p3 = []
    return tab


def awariaBitu(tab, i):
    _random = random.randint(1, 6)
    tab2 = []
    tab2 = tab
    if(tab2[i][_random-1] == 0):
        tab2[i][_random-1] = 1
    else:
        tab2[i][_random-1] = 0
    return tab2


def podwojnaAwariaBitu(tab, i):
    tab2 = []
    tab2 = tab
    _random = random.randint(1, 6)
    _random2 = random.randint(1, 6)

    if(tab2[i][_random-1] == 0):
        tab2[i][_random-1] = 1
    else:
        tab2[i][_random-1] = 0
    if(tab2[i][_random2-1] == 0):
        tab2[i][_random2-1] = 1
    else:
        tab2[i][_random2-1] = 0
    return tab2


def losowanieAwarii(tab, i):
    tab2 = []
    tab2 = tab
    losowanie = random.randint(0, 1)
    if(losowanie == 1):
        podwojnaAwariaBitu(tab2, i)
    else:
        awariaBitu(tab2, i)
    return tab2


def DemodulacjaHamming(tab2, _len):
    for i in range(_len):
        p1 = (tab2[i][0] + tab2[i][2] + tab2[i][4] + tab2[i][6]) % 2
        p2 = (tab2[i][1] + tab2[i][2] + tab2[i][5] + tab2[i][6]) % 2
        p3 = (tab2[i][3] + tab2[i][4] + tab2[i][5] + tab2[i][6]) % 2
        n = p1 * 2**0 + p2 * 2**1 + p3 * 2**2
        if(tab2[i][n-1] == 0):
            tab2[i][n-1] = 1
        else:
            tab2[i][n-1] = 0
        p1 = []
        p2 = []
        p3 = []

    return tab2


def DodanieP4(tab, _len):
    tab2 = []
    tab2 = tab
    for i in range(_len):
        p4 = (tab2[i][0] + tab2[i][1] + tab2[i][2] +
              tab2[i][3]+tab2[i][4]+tab2[i][5]+tab2[i][6]) % 2
        tab2[i].append(p4)
    return tab2


def dPrim(tab2, _len):
    tab3 = []
    tab3 = tab2
    for i in range(_len):
        tab3[i].pop(0)
        tab3[i].pop(0)
        tab3[i].pop(1)
    return tab3


def dPrim2(tab2, _len):
    tab3 = []
    tab3 = tab2
    for i in range(_len):
        tab3[i].pop(0)
        tab3[i].pop(0)
        tab3[i].pop(1)
        tab3[i].pop(4)
    return tab3


def sprwadzenieP4(tab2, i):
    xx = []
    p4 = (tab2[i][0] + tab2[i][1] + tab2[i][2] + tab2[i]
          [3]+tab2[i][4]+tab2[i][5]+tab2[i][6]) % 2
    if(tab2[i][7] == p4):
        xx = "NORMALNA SZANSA BO P4 JEST ZGODNY"
    else:
        xx = "P4 NIEZGODNY -> 50% SZANS IDZIEMY DALEJ"
    return xx


def naprawianiePakietu(tab2, i):
    p1 = (tab2[i][0] + tab2[i][2] + tab2[i][4] + tab2[i][6]) % 2
    p2 = (tab2[i][1] + tab2[i][2] + tab2[i][5] + tab2[i][6]) % 2
    p3 = (tab2[i][3] + tab2[i][4] + tab2[i][5] + tab2[i][6]) % 2
    n = p1 * 2**0 + p2 * 2**1 + p3 * 2**2
    if(n > 1):
        if(tab2[i][n-1] == 0):
            tab2[i][n-1] = 1
        else:
            tab2[i][n-1] = 0
    ponownieP4 = (tab2[i][0] + tab2[i][1] + tab2[i][2] +
                  tab2[i][3]+tab2[i][4]+tab2[i][5]+tab2[i][6]) % 2
    if(tab2[i][7] == ponownieP4):
        print(
            "-------------NAPRAWA ZAKOŃCZONA--------------------------------->   SUKCES", tab2[i])
    else:
        print(
            "-------------NAPRAWA ZAKOŃCZONA-------------------------------->   WYSLIJ TRANSMISJE PONOWNIE ", tab2[i])
    return tab2


# def secdedDemodulacja(tab2):
binary = ASCII("kot")
# binary = [1, 1, 1, 0]
_len = int(len(binary)/4)

xd = podzialNaCztery(_iterator)
print("-------------PODZIAL NA 4 BITY------------------------------->  ", xd)

Hamming = Hamming(xd, _len)
print("-------------HAMMING 7.4 PO DODANIU BITOW PARZYSTOSCI-------->  ", Hamming)

for i in range(_len):
    HammingAwaria = awariaBitu(Hamming, i)
print("-------------HAMMING 7.4 PO STWIERDZENIU AWARII-------------->  ", HammingAwaria)

HammingDemodulacja = DemodulacjaHamming(HammingAwaria, _len)
Prim = dPrim(HammingDemodulacja, _len)
print("-------------HAMMING 7.4 PO DEMODULACJI---------------------->  ", Prim)


print("--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--")
print("--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--")
print("--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~--")

Hamming2 = Hamming2(xd, _len)

print("-------------NA PODSTAWIE HAMMINGA ZAKODUJE SECED--------------->  ", Hamming2)

secdedDodanieP4 = DodanieP4(Hamming2, _len)
print("-------------DODANIE P4 DO SECDED------------------------------->  ", secdedDodanieP4)

for i in range(_len):
    secdedAwaria = losowanieAwarii(secdedDodanieP4, i)
print("-------------AWARIA BITU---------------------------------------->  ", secdedAwaria)

for i in range(_len):
    trelele = sprwadzenieP4(secdedAwaria, i)
    # print("-------------WERYFIKACJA P4------------------------------------->  ", trelele)
    naprawa = naprawianiePakietu(secdedAwaria, i)  # naprawa

Prim2 = dPrim2(naprawa, _len)
print("-------------SECDED PO ZDEKODOWAIU------------------------------>  ", Prim2)
