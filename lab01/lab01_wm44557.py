from matplotlib import pyplot as plt
import math
def check(xd):

    wFunkcji= 7 * xd**2 + 5*xd + 7
    bKwadrat = (5*xd)**2
    czteryAc = 4 * 7
    delta = bKwadrat-czteryAc
    iks1 = (-(5*xd) - math.sqrt(delta))/(2*7)
    iks2 = (-(5*xd) + math.sqrt(delta))/(2*7)
    if(delta < 0):
        return print("Brak miejsc zerowych")
    print("Wartosc funkcji: ", wFunkcji, "Delta: ", delta, "X.1: ", iks1, "X.2: ",iks2)

    
check(2)


def wartosc(x):
    return 7.0 * pow(x,2.0) + 5.0*x + 7.0
def funkcja():
    tZero = -10; tN = 10; deltaT =(1.0/100); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        print(tn," ",wartosc(tn)," \n")
        tab.append(tn)
        tab2.append(wartosc(tn))
        plt.plot(tab,tab2)
        tn=tZero + (n*deltaT)
        n=n+1
        

#funkcja()
plt.show()