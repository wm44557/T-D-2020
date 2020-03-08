from matplotlib import pyplot as plt
def wartosc(xd):
    return 7.0 * pow(xd,2.0) + 5.0*xd + 7.0
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
        

funkcja()
plt.show()