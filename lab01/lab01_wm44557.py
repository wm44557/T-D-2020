from matplotlib import pyplot as plt
import math
# def check(xd):

#     wFunkcji= 7 * xd**2 + 5*xd + 7
#     bKwadrat = (5*xd)**2
#     czteryAc = 4 * 7
#     delta = bKwadrat-czteryAc
#     iks1 = (-(5*xd) - math.sqrt(delta))/(2*7)
#     iks2 = (-(5*xd) + math.sqrt(delta))/(2*7)
#     if(delta < 0):
#         return print("Brak miejsc zerowych")
#     print("Wartosc funkcji: ", wFunkcji, "Delta: ", delta, "X.1: ", iks1, "X.2: ",iks2)



# def wartosc(x):
#     x = 7.0 * pow(x,2.0) + 5.0*x + 7.0
#     return x

# def funkcja():
#     tZero = -10; tN = 10; deltaT =(1.0/100); tn = tZero; n = 0
#     tab = []; tab2 = []
#     while(tn <= tN):
#         print(tn," ",wartosc(tn)," \n")
#         tab.append(tn)
#         tab2.append(wartosc(tn))
#         plt.plot(tab,tab2)
#         tn=tZero + (n*deltaT)
#         n=n+1
        

# funkcja()
# plt.show()

###----------------------------------------------------------------------------###
def x(xd):
    return 7 * xd**2 + 5*xd + 5


def wartosc2(tn,opcja):
    if(opcja == 1):
         a = 7.0 * pow(tn,2.0) + 5.0*tn + 5.0
    if(opcja == 2):
         a = 2 * (x(tn))**2 + 12 * math.cos(tn)
    return a
    
    
def funkcja2(opcja):
    tZero = 0; tN = 1; deltaT =(1.0/22050); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        print(tn," ",wartosc2(tn,opcja)," \n")
        tab.append(tn)
        tab2.append(wartosc2(tn,opcja))
        
        tn=tZero + (n*deltaT)
        n=n+1
    plt.plot(tab,tab2)

        

funkcja2(opcja=2)
plt.show()