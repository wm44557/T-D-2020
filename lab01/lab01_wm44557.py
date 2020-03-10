from matplotlib import pyplot as plt
import math
# def check(xd):

    # wFunkcji= 7 * xd**2 + 5*xd + 7
    # bKwadrat = (5*xd)**2
    # czteryAc = 4 * 7
    # delta = bKwadrat-czteryAc
    # iks1 = (-(5*xd) - math.sqrt(delta))/(2*7)
    # iks2 = (-(5*xd) + math.sqrt(delta))/(2*7)
    # if(delta < 0):
    #     return print("Brak miejsc zerowych")
    # print("Wartosc funkcji: ", wFunkcji, "Delta: ", delta, "X.1: ", iks1, "X.2: ",iks2)



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
 #        plt.ylabel('f(t)')
#         plt.xlabel('t(s)')
#         tn=tZero + (n*deltaT)
#         n=n+1
        

# funkcja()
# plt.show()

###-----------------------------------ZAD.2------------------------------------###
def x(tn):
    return 7 * tn**2 + 5*tn + 5

def y(tn):
    return 2 * (x(tn))**2 + 12 * math.cos(tn)

def z(tn):
    return math.sin((math.pi*2) * 7 * tn) * x(tn) - 0.2 * math.log10(abs(y(tn)) + math.pi)

def u(tn):
    return math.sqrt(abs(y(tn) * y(tn) * z(tn) )) - 1.8 * math.sin(0.4 * tn * z(tn) * x(tn) )

def v(tn):
    if(0.22 > tn and tn >= 0):
        return (1 - 7 * tn) * math.sin((2 * math.pi * tn * 10) / (tn + 0.04))
    if(0.22 <= tn and tn <= 0.7):
        return 0.63 * tn * math.sin(125 * tn)
    if(1 >= tn and tn >= 0.7):
        return tn**(-0.662) + 0.77 * math.sin(8 * tn)

def p_2(tn):
    wynik = 0
    for n in range(1,3):   
        wynik = wynik + ( ( ( math.cos((12 * tn) * n**2 )) + ( math.cos( 16 * tn * n ) ) ) / n**2 )
    return wynik
       
def p_4(tn):
    wynik = 0
    for n in range(1,5):   
        wynik = wynik + ( ( ( math.cos((12 * tn) * n**2 )) + ( math.cos( 16 * tn * n ) ) ) / n**2 )
    return wynik
       
def p_AB(tn): ## A= 7* B = 5 = 35 +1 = 36
    wynik = 0
    for n in range(1,36):   
        wynik = wynik + ( ( ( math.cos((12 * tn) * n**2 )) + ( math.cos( 16 * tn * n ) ) ) / n**2 )
    return wynik
       



def wartosc2(tn,opcja):
    if(opcja == 1):
        wynik = y(tn)

    if(opcja == 2):
        wynik = z(tn)

    if(opcja == 3):
        wynik = u(tn)

    if(opcja == 4):
        wynik = v(tn)

    if(opcja == 5):
        wynik = p_2(tn)

    if(opcja == 6):
        wynik = p_4(tn)

    if(opcja == 7):
        wynik = p_AB(tn)

    return wynik
    
    
def funkcja2(opcja):
    tZero = 0; tN = 1; deltaT =(1.0/22050); tn = tZero; n = 0
    tab = []; tab2 = []
    while(tn <= tN):
        #print(tn," ",wartosc2(tn,opcja)," \n")
        tab.append(tn)
        tab2.append( wartosc2(tn,opcja) )
        tn=tZero + (n * deltaT)
        n = n + 1

    plt.figure()
    plt.plot(tab,tab2)
    plt.ylabel('f(t)')
    plt.xlabel('t(s)')
    plt.savefig('./lab01/wykres {} .png'.format(opcja))

   

        
funkcja2(opcja=1)
funkcja2(opcja=2)
funkcja2(opcja=3)
funkcja2(opcja=4)
funkcja2(opcja=5)
funkcja2(opcja=6)
funkcja2(opcja=7)
plt.show()
