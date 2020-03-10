import math
from matplotlib import pyplot as plt

#44557 #A - 7 B - 5 C - 5
fi = math.pi * 5
A = 1.0
fs = 100

def sT(t):
    return A * math.sin(( 2*math.pi * 5 * t) +fi )


def funkcja2():
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


   
funkcja2()
plt.savefig('./lab02/foo2.png')

plt.show()
