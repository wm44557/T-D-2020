import matplotlib.pyplot as plt
import math


def Zmienne(fs, tn, tN, deltaT, A, fi, ciagBinarny, Tb):
    global _fs, _tn, _tN, _deltaT, _A, _fi, _ciagBinarny, _Tb, _n, _clkF, _clkFT, _ttlFT, _nrziFT, _bamiFT, _manchesterFT, _ciagBinarny, _DnrziFT, _DbamiFT
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
    _DnrziFT = []
    _bamiFT = []
    _DbamiFT = []
    _manchesterFT = []
    _n = 1


def ASCII(tekst):
    byte_array = tekst.encode()
    binary_int = int.from_bytes(byte_array, "little")
    binary_string = format(binary_int, "08b")
    liczby = list(map(int, list(binary_string)))
    return liczby


def sT(t):
    return -1*_A * math.sin((2*math.pi * 100 * t) + _fi)


def CLK():
    global _tn, _n
    while _tn < _tN:
        _tn = (_deltaT * _n)
        if((-1*_A * math.sin((2*math.pi * 100 * _tn) + _fi)) > 0.0001):
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
        if((_Tb/2 * (x + 1)) < _tn):
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
        if _clkFT[i] == 1 and _clkFT[i+1] == 0:
            if _ttlFT[i+1] == 1:
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
    nazwy = ['Clk', 'Ttl', 'Nrzi', 'Bami', 'Manchester']

    for i in range(5):
        axs[i].set_xlabel('t[s]')
        axs[i].set_ylabel('F[t]')
        axs[i].set_title(nazwy[i])
        axs[i].grid()

    axs[0].plot(clkf, clkft, 'k')
    axs[1].plot(clkf, ttlft, 'b')
    axs[2].plot(clkf, nrzift, 'k')
    axs[3].plot(clkf, bamift, 'm')
    axs[4].plot(clkf, manchesterft, 'g')

    plt.show()
    return


def demodulacjaNRZI():
    varActually = 1
    for i in range(len(_nrziFT)):
        if _clkFT[i] == 1 and _clkFT[i+1] == 0:
            if _ttlFT[i] == 1:

                if _nrziFT[i == 1]:  # XOR 1 i 0 to 1
                    if _nrziFT[i+1] == -1:
                        varActually = 1
                    else:  # XOR 1 i 1 to 0
                        varActually = 0

                else:
                    if _nrziFT[i+1] == -1:  # XOR 0 i 0
                        varActually = 0
                    else:  # XOR 0 i 1
                        varActually = 1

        _DnrziFT.append(varActually)


def demodulacjaBAMI():
    varActually = 0
    for i in range(len(_clkF)):
        if _clkFT[i] == 1 and _clkFT[i+1] == 0:
            if _bamiFT[i+1] == 1:
                varActually = 1
            else:
                varActually = 0
        _DbamiFT.append(varActually)


if __name__ == "__main__":
    ciagBinarny = ASCII('kot')
    # ciagBinarny = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
    # ciagBinarny = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1]

    ''' 1.FS 2.tn 3.tN 4.DeltaT 5.Amplituda 6.FI 7.Ciąg  binarny, 8.Tb'''
    Zmienne(1000, 0, 1, 0.0001, 1.0, math.pi * 5, ciagBinarny, 0.01)
    CLK()
    TTL()
    NRZI()
    BAMI()
    MANCHESTER()
    demodulacjaNRZI()
    demodulacjaBAMI()
    plt.figure()
    plt.plot(_clkF, _DbamiFT)
    wyswietlanie(_clkF[0:1148], _clkFT[0:1148],
                 _ttlFT[0:1148], _nrziFT[0:1148], _bamiFT[0:1148], _manchesterFT[0:1148])
