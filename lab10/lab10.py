import matplotlib.pyplot as plt
import math
import random
from math import log10, sqrt
import numpy as np
import binascii


def Zmienne(fs, tn, tN, deltaT, A, fi, ciagBinarny, Tb):
    global _fs, _tn, _tN, _deltaT, _A, _fi, _ciagBinarny, _Tb, _n, _clkF, _clkFT, _ttlFT, _nrziFT, _bamiFT, _manchesterFT, _ciagBinarny, _DnrziFT, _DbamiFT, _DmanchesterFT, _Z, _nrziFTT, _bamiFTT, _manchesterFTT, _licznik233
    _fs = fs
    _tn = tn
    _tN = tN
    _deltaT = deltaT
    _A = A
    _fi = fi
    _ciagBinarny = ciagBinarny
    _Tb = Tb
    _clkF = []
    _clkFT = []
    _ttlFT = []
    _nrziFT = []
    _nrziFTT = []
    _DnrziFT = []
    _bamiFT = []
    _bamiFTT = []
    _DbamiFT = []
    _manchesterFT = []
    _manchesterFTT = []
    _DmanchesterFT = []
    _n = 1
    _Z = 2400


def ASCII(tekst):
    napis = ''
    for x in tekst:
        napis = napis+bin(ord(x))[2:].zfill(8)
    return list(map(int, list(napis)))


def CLK():
    global _tn, _n
    while _tn < _tN:
        _tn = (_deltaT * _n)
        if((-1*_A * math.sin((2*math.pi * 100 * _tn) + _fi)) > _deltaT):
            _clkFT.append(1)
        else:
            _clkFT.append(0)
        _n += 1
        _clkF.append(_tn)
    _tn = 0
    _n = 1


def TTL():
    global _tn, _n
    x = 0
    while(_tn <= _tN):
        if(x < len(_ciagBinarny)-1):
            _ttlFT.append(_ciagBinarny[x])
        else:
            _ttlFT.append(0)
        if((_Tb * (x + 1)) < _tn):
            x = x+1
        _tn = (_deltaT * _n)
        _n += 1
    _tn = 0
    _n = 1


def NRZI():
    varActually = 0
    for i in range(len(_clkF)):
        if _clkFT[i] == 1 and _clkFT[i+1] == 0:
            if _ttlFT[i] == 1:
                if varActually == 0:
                    varActually = -1
                else:
                    varActually *= -1
        _nrziFT.append(varActually)


def BAMI():
    varActually = 0
    varPrevious = 1
    for i in range(len(_clkF)):
        if i+1 < len(_clkF):
            if(i > 50):
                if _clkFT[i] == 1 and _clkFT[i+1] == 0:
                    if _ttlFT[i] == 1:
                        varActually = varPrevious * -1
                        varPrevious = varActually
                    else:
                        varActually = 0

                _bamiFT.append(varActually)


def MANCHESTER():
    varActually = 0
    for i in range(len(_clkF)):
        if i+1 < len(_clkF):
            if _clkFT[i] == 1 and _clkFT[i+1] == 0:
                if _ttlFT[i+1] == 1:
                    varActually = -1
                else:
                    varActually = 1
            elif _clkFT[i] == 0 and _clkFT[i+1] == 1:
                if _ttlFT[i+1] == _ttlFT[i]:
                    varActually = varActually * -1
                else:
                    varActually = _clkFT[i]
        _manchesterFT.append(varActually)


def wyswietlanie(clkf, clkft, ttlft,  nrzift, bamift, manchesterft):
    fig, axs = plt.subplots(5, 1, constrained_layout=True, figsize=(10, 8))
    fig.suptitle('Strumień danych po kodowaniu liniowym', fontsize=16)
    nazwy = ['CLK', 'TTL', 'BAMI', 'Manchester', 'NRZI']

    for i in range(5):
        axs[i].set_xlabel('t[s]')
        axs[i].set_ylabel('F[t]')
        axs[i].set_title(nazwy[i])
        axs[i].grid()

    axs[0].plot(clkf, clkft, 'k')
    axs[1].plot(clkf, ttlft, 'b')
    axs[2].plot(clkf, bamift, 'm')
    axs[3].plot(clkf, manchesterft, 'g')
    axs[4].plot(clkf, nrzift, 'k')
    # plt.show()
    return


def wyswietlanieNRZI(clkf, clkft, TTL, NRZI, SZUM, DFT, SZUMDFT):
    fig, axs = plt.subplots(6, 1, constrained_layout=True, figsize=(10, 8))
    fig.suptitle('Strumień danych po kodowaniu NRZI', fontsize=16)
    nazwy = ['CLK', 'TTL', 'NRZI', 'NRZI-SZUM', 'NRZI-DFT', 'NRZI-SZUMDFT']

    for i in range(6):
        axs[i].set_xlabel('t[s]')
        axs[i].set_ylabel('F[t]')
        axs[i].set_title(nazwy[i])
        axs[i].grid()

    axs[0].plot(clkf, clkft, 'k')
    axs[1].plot(clkf, TTL, 'b')
    axs[2].plot(clkf, NRZI, 'k')
    axs[3].plot(clkf, SZUM, 'm')
    axs[4].plot(clkf, DFT, 'g')
    axs[5].plot(clkf, SZUMDFT, 'c')
    # plt.show()
    return


def wyswietlanieBAMI(clkf, clkft, TTL, BAMI, SZUM, DFT, SZUMDFT):
    fig, axs = plt.subplots(6, 1, constrained_layout=True, figsize=(10, 8))
    fig.suptitle('Strumień danych po kodowaniu BAMI', fontsize=16)
    nazwy = ['CLK', 'TTL', 'BAMI', 'BAMI-SZUM', 'BAMI-DFT', 'BAMI-SZUMDFT']

    for i in range(6):
        axs[i].set_xlabel('t[s]')
        axs[i].set_ylabel('F[t]')
        axs[i].set_title(nazwy[i])
        axs[i].grid()

    axs[0].plot(clkf, clkft, 'k')
    axs[1].plot(clkf, TTL, 'b')
    axs[2].plot(clkf, BAMI, 'm')
    axs[3].plot(clkf, SZUM, 'k')
    axs[4].plot(clkf, DFT, 'g')
    axs[5].plot(clkf, SZUMDFT, 'c')
    # plt.show()
    return


def wyswietlanieMANCHESTER(clkf, clkft, TTL, MANCHESTER, SZUM, DFT, SZUMDFT):
    fig, axs = plt.subplots(6, 1, constrained_layout=True, figsize=(10, 8))
    fig.suptitle('Strumień danych po kodowaniu MANCHESTER', fontsize=16)
    nazwy = ['CLK', 'TTL', 'MANCHESTER', 'MANCHESTER-SZUM',
             'MANCHESTER-DFT', 'MANCHESTER-SZUMDFT']

    for i in range(6):
        axs[i].set_xlabel('t[s]')
        axs[i].set_ylabel('F[t]')
        axs[i].set_title(nazwy[i])
        axs[i].grid()

    axs[0].plot(clkf, clkft, 'k')
    axs[1].plot(clkf, TTL, 'b')
    axs[2].plot(clkf, MANCHESTER, 'g')
    axs[3].plot(clkf, SZUM, 'k')
    axs[4].plot(clkf, DFT, 'm')
    axs[5].plot(clkf, SZUMDFT, 'c')
    # plt.show()
    return


def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8], 2)) for i in range(len(s)//8))


def demodulacjaNRZI(tab):
    varActually = 1
    licznik2 = 1
    tab2 = []
    for i in range(len(tab[0:_Z+100])):
        if _clkFT[i] == 0 and _clkFT[i+1] == 1:
            if tab[i-100] == 1 and tab[i] == -1:
                varActually = 1
            elif tab[i-100] == -1 and tab[i] == 1:
                varActually = 1
            elif tab[i-100] == -1 and tab[i] == -1:
                varActually = 0
            elif tab[i-100] == 1 and tab[i] == 1:
                varActually = 0
            # print("XOR", varActually)
        licznik2 = licznik2 + 1
        if(licznik2 > 100):
            tab2.append(varActually)
    return tab2


def demodulacjaBAMI(tab):
    tab2 = []

    licznik2 = 1
    varActually = 1
    for i in range(len(tab[0:_Z+100])):
        if i+1 < len(tab):
            if _clkFT[i] == 0 and _clkFT[i+1] == 1:
                if tab[i+1] == 1 or tab[i+1] == -1:
                    varActually = 1
                else:
                    varActually = 0
        licznik2 = licznik2 + 1

        tab2.append(varActually)
    return tab2


def demodulacjaMANCHESTER(tab):
    tab2 = []
    varActually = 1
    licznik2 = 1
    for i in range(_Z+100):
        if i+1 < len(tab):
            if _clkFT[i] == 1 and _clkFT[i+1] == 0:
                if tab[i] == 1:
                    varActually = 0
                else:
                    varActually = 1

        licznik2 = licznik2 + 1
        if(licznik2 > 100):
            tab2.append(varActually)
    return tab2


def podzialNaCztery(iterator, binary):
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


def Hamming3(slowoBinarne, _len):
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


def DemodulacjaHamming(tab2, _len):
    for i in range(_len):
        p1 = (tab2[i][0] + tab2[i][2] + tab2[i][4] + tab2[i][6]) % 2
        p2 = (tab2[i][1] + tab2[i][2] + tab2[i][5] + tab2[i][6]) % 2
        p3 = (tab2[i][3] + tab2[i][4] + tab2[i][5] + tab2[i][6]) % 2
        n = p1 * 2**0 + p2 * 2**1 + p3 * 2**2
        if(n != 0):
            if(tab2[i][n-1] == 0):
                tab2[i][n-1] = 1
            else:
                tab2[i][n-1] = 0
        p1 = []
        p2 = []
        p3 = []

    return tab2


def dPrim(tab2, _len):
    tab3 = []
    tab3 = tab2
    for i in range(_len):
        tab3[i].pop(0)
        tab3[i].pop(0)
        tab3[i].pop(1)
    return tab3


def awariaBituU(ciagBinarny, dekodowanie, siedemD):
    global _licznik233
    _licznik233 = 0
    tabX = []
    tabY = siedemD
    mod = 0
    dzielenie = 0
    d = 0
    for i in range(len(ciagBinarny)):
        if ciagBinarny[i] != dekodowanie[i]:
            _licznik233 = _licznik233 + 1
            tabX.append(i)
    for j in range(len(tabX)):
        mod = tabX[j] % 4
        dzielenie = tabX[j]/4
        c = int(dzielenie)
        if(mod == 0):
            d = 2
        if(mod == 1):
            d = 4
        if(mod == 2):
            d = 5
        if(mod == 3):
            d = 6
        if(siedemD[c][d] == 1):
            siedemD[c][d] = 0
        else:
            siedemD[c][d] = 1
    return tabY


def convert(s):

    # initialization of string to ""
    str1 = ""

    # using join function join the list s by
    # separating words by str1
    return(str1.join(s))


def awariaBitu(tab, i):
    _random = random.randint(1, 6)
    tab2 = []
    tab2 = tab
    if(tab2[i][_random-1] == 0):
        tab2[i][_random-1] = 1
    else:
        tab2[i][_random-1] = 0
    return tab2


def BinaryToDecimal(binary):

    # Using int function to convert to
    # string
    string = int(binary)

    return string


def BinaryToDecimal2(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)


def DFT(tab, tab2):
    # Wypełnienie tablic zerami
    X_re = []
    fk = []
    X_im = []
    M = []
    M_prim = []
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

    threshold = abs(max(M))/100000

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

    # plt.title('DFT FSK')
    # plt.xlabel('f[hz]')
    # plt.ylabel('A')
    # # plt.figure()
    # plt.plot(fk, M_prim)
    return fk, M_prim


if __name__ == "__main__":
    ciagBinarny = ASCII('kot')

    print(ciagBinarny, "   --- Ciag Binarny")

    ''' 1.FS 2.tn 3.tN 4.DeltaT 5.Amplituda 6.FI 7.Ciąg  binarny, 8.Tb'''
    Zmienne(10000, 0, 2.4, 0.0001, 1.0, math.pi * 5, ciagBinarny, 0.01)

    CLK()
    TTL()
    NRZI()
    BAMI()
    MANCHESTER()
    szum = []
    szumNormalizacja = []
    for dlugosc in range(2400):
        szum.append(np.random.normal(0, 0.5))

    minimum = min(szum)
    maksimum = max(szum)
    for x in range(2400):
        szumNormalizacja.append(
            2 * (szum[x]-minimum)/(maksimum-minimum) - 1)

    alfa = 0.30
    nrziP = []
    bamiP = []
    manchesterP = []
    for i in range(2400):
        nrziP.append((_nrziFT[i] * alfa) + szumNormalizacja[i]*(1-alfa))
        # bamiP.append((_bamiFT[i] * alfa) + szumNormalizacja[i]*(1-alfa))
        # manchesterP.append(
        #     (_manchesterFT[i] * alfa) + szumNormalizacja[i]*(1-alfa))

    fk_nrzi, M_prim_nrzi = DFT(_clkF[0:_Z], _nrziFT[0:_Z])
    fk_nrziSZ, M_prim_nrziSZ = DFT(_clkF[0:_Z], nrziP)
    wyswietlanieNRZI(_clkF[0:_Z], _clkFT[0:_Z],
                     _ttlFT[0:_Z], _nrziFT[0:_Z], nrziP, M_prim_nrzi, M_prim_nrziSZ)
    # fk_bami, M_prim_bami = DFT(_clkF[0:_Z], _bamiFT[0:_Z])
    # fk_bamiSZ, M_prim_bamiSZ = DFT(_clkF[0:_Z], bamiP)
    # wyswietlanieBAMI(_clkF[0:_Z], _clkFT[0:_Z],
    # #                  _ttlFT[0:_Z], _bamiFT[0:_Z], bamiP, M_prim_bami, M_prim_bamiSZ)
    # fk_manchester, M_prim_manchester = DFT(_clkF[0:_Z], _manchesterFT[0:_Z])
    # fk_manchesterSZ, M_prim_manchesterSZ = DFT(_clkF[0:_Z], manchesterP)
    # wyswietlanieMANCHESTER(_clkF[0:_Z], _clkFT[0:_Z],
    #                        _manchesterFT[0:_Z], _manchesterFT[0:_Z], manchesterP, M_prim_manchester, M_prim_manchesterSZ)
for i in range(2400):
    if(nrziP[i] > 0.34):
        nrziP[i] = 1
    elif(nrziP[i] < -0.34):
        nrziP[i] = -1
    else:
        nrziP[i] = 0
# for i in range(2400):
#     if(bamiP[i] > 0.34):
#         bamiP[i] = 1
#     elif(bamiP[i] < -0.34):
#         bamiP[i] = -1
#     else:
#         bamiP[i] = 0
# for i in range(2400):
#     if(manchesterP[i] > 0):
#         manchesterP[i] = 1
#     else:
#         manchesterP[i] = -1

tab2 = demodulacjaNRZI(nrziP)
# tab3 = demodulacjaBAMI(bamiP)
# tab4 = demodulacjaMANCHESTER(manchesterP)
# demodulacjaBAMI()
# demodulacjaMANCHESTER()
# print(_bamiFTT, "   --- Ciag Binarny po demodulacji Bami")

bityNrziD = tab2[0:_Z:100]
print(bityNrziD, ' --- Bity po Dekodowaniu NRZI')
# bityBami = tab3[0:_Z:100]
# print(bityBami, ' --- Bity po Dekodowaniu BAMI')
# bityManchesterD = tab4[0:_Z:100]
# print(bityManchesterD, ' --- Bity po Dekodowaniu MANCHESTER')
# print(bityNrziD, "BITY PO DEKODOWANIU NRZI")
# # plt.figure()
# # plt.title('Dekoder Nrzi')
# # plt.plot(_clkF[0:2400], _DnrziFT[0:2400])

# bityBamiD = _DbamiFT[0:_Z:100]
# print(bityBamiD, "BITY PO DEKODOWANIU BAMI")
# # plt.figure()
# # plt.title('Dekoder Nrzi')
# # plt.plot(_clkF[0:_Z], _DbamiFT[0:_Z])

# bityManchesterD = _DmanchesterFT[0:_Z:100]
# print(bityManchesterD, "BITY PO DEKODOWANIU MANCHESTER")
# # plt.figure()
# # plt.title('Dekoder MANCHESTER')
# # plt.plot(_clkF[0:_Z], _DmanchesterFT[0:_Z])

_len = int(len(ciagBinarny)/4)
_iterator = 0
print("------------------------------------------------------------>  ")

xd = podzialNaCztery(_iterator, ciagBinarny)
print(xd, "PODZIAL NA 4 BITY Ciągu Binarnego")

Hamming = Hamming(xd, _len)
print(Hamming, "HAMMING 7.4 PO DODANIU BITOW PARZYSTOSCI")

HammingAwariaNrzi = awariaBituU(ciagBinarny, bityNrziD, Hamming)
print(HammingAwariaNrzi, "HAMMING 7.4 PO UWZGLĘDNIENIU AWARII w NRZI")

# xd2 = podzialNaCztery(_iterator, ciagBinarny)
# Hamming2 = Hamming2(xd2, _len)
# HammingAwariaBami = awariaBituU(ciagBinarny, bityBami, Hamming)
# print(HammingAwariaBami, "HAMMING 7.4 PO SPRAWDZENIU AWARII w BAMI")

# xd3 = podzialNaCztery(_iterator, ciagBinarny)
# Hamming3 = Hamming3(xd3, _len)

# HammingAwariaManchester = awariaBituU(
#     ciagBinarny, bityManchesterD, Hamming)
# print(HammingAwariaManchester, "HAMMING 7.4 PO SPRAWDZENIU AWARII w MANCHESTER")

HammingDemodulacja = DemodulacjaHamming(Hamming, _len)
Prim = dPrim(HammingDemodulacja, _len)
print(Prim,
      "HAMMING 7.4 PO DEKODOWANIU MANCHESTER ")

x = ''
for i in range(6):
    x = x+(''.join(map(str, Prim[i])))
print(x)
# HammingDemodulacjaBami = DemodulacjaHamming(HammingAwariaBami, _len)
# Prim2 = dPrim(HammingDemodulacjaBami, _len)
# print(Prim2,
#       "HAMMING 7.4 PO DEMODULACJI BAMI ")

# HammingDemodulacjaManchester = DemodulacjaHamming(
#     HammingAwariaManchester, _len)
# Prim3 = dPrim(HammingDemodulacjaManchester, _len)
# print(Prim3,
#       "HAMMING 7.4 PO DEMODULACJI MANCHESTER ")
# print(type(Prim))
print("Współcznikkik BER", _licznik233/24)
print("Słowo: ")
print(chr(int(x[:8], 2)), chr(int(x[8:16], 2)), chr(int(x[16:24], 2)))

plt.show()
