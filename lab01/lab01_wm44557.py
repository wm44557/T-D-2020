def wartosc(xd):
    return 7.0 * pow(xd,2.0) + 5.0*xd + 7.0
def funkcja():
    tZero = -10;tN = 10; deltaT =(1.0/100); tn = tZero;n = 0
   
    while(tn <= tN):
        print(tn," ",wartosc(tn)," \n")

        tn=tZero + (n*deltaT)
        n=n+1

funkcja()