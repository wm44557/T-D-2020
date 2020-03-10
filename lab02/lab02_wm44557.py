import math
from matplotlib import pyplot as plt

#44557 #A - 7 B - 5 C - 5
fi = math.pi * 5
A = 1.0
fs = 100
def sT(t):
    return A * math.sin(( 2*math.pi * 5 * t) +fi )

def funkcja1():
    tZero = 0; tN = 7; deltaT =(1.0/1000); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        print(tn," ",sT(tn)," \n")


        tab.append(tn)
        tab2.append( sT(tn) )

        tn=tZero + (n * deltaT)
        n = n + 1

    plt.figure()
    plt.plot(tab,tab2,'.')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.savefig('./lab02/wykres1.png')
    



def sT2(t):
    return round(((((A * math.sin(( 2*math.pi * 5 * t) +fi )) + 1) / 2*A) * 2**16),0)


def funkcja2():
    tZero = 0; tN = 7; deltaT =(1.0/1000); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        print(tn," ",sT2(tn)," \n")


        tab.append(tn)
        tab2.append( sT2(tn) )

        tn=tZero + (n * deltaT)
        n = n + 1

    plt.figure()
    plt.plot(tab,tab2,'.')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.savefig('./lab02/wykres2.png')

def sT3(t):
    return round(((((A * math.sin(( 2*math.pi * 5 * t) +fi )) + 1) / 2*A) * 2**8),0)

def funkcja3():
    tZero = 0; tN = 7; deltaT =(1.0/500); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        print(tn," ",sT3(tn)," \n")


        tab.append(tn)
        tab2.append( sT3(tn) )

        tn=tZero + (n * deltaT)
        n = n + 1

    plt.figure()
    plt.plot(tab,tab2,'.')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.savefig('./lab02/wykres3.png')


funkcja1()
funkcja2()
funkcja3()
plt.show()

