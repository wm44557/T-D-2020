import math
from math import log10, sqrt
from matplotlib import pyplot as plt

#44557 #A - 7 B - 5 C - 5

'''Częstotliwość próbkowania'''
fs = 400 
'''Liczba próbek'''
N = 400
'''Zakres dla n <0:ABC> ABC = 755''' 
tZero = 0; tN = 755
'''Częstotliwość sygnału B = 5 ''' 
f = 5 #Częstotliwość sygnału Hz
'''FI = PI * C //C = 5 ''' 
fi5 = math.pi * 5
'''Amplituda''' 
A = 1.0
'''Delta T''' 
deltaT = 1/fs

### Deklaracja tablic
X_re = []; X_im = []; M = []; M_prim = []; x = []; tab2 = []; fk = []

def x_(tn):
    return A * math.sin(( 2*  math.pi * f * tn) +fi5 )

def y(tn):
    return 2 * (x_(tn))**2 + 12 * math.cos(tn)

def z(tn):
    return math.sin((math.pi*2) * 7 * tn) * x_(tn) - 0.2 * math.log10(abs(y(tn)) + math.pi)

def u(tn):
    return math.sqrt(abs(y(tn) * y(tn) * z(tn) )) - 1.8 * math.sin(0.4 * tn * z(tn) * x_(tn) )

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
      

################################################# Wybór opcji
def wartosc2(tn,opcja):
    if(opcja == 0):
        wynik = x_(tn)

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


''' Funkcja do transformanty Furiera'''

def DFT(N,opcja):
#Wypełnienie tablic zerami
    for i in range (N):
        X_re.append(0.0)
        X_im.append(0.0)
        M.append(0.0)
        fk.append(i * (fs/N) ) #skala częstotliwości wektor z krokiem fs/N

    tn = 0.0
    n = 0

    ''' Rysowanie wykresów -> dla tonu prostego 2 wykresy (przed i po) '''
    while( tn <= tN ):
        x.append(wartosc2(tn,opcja)) ## rysowanei z wybraną opcją
        tab2.append(tn)
        tn = tZero + (n * deltaT)
        n = n + 1

#Suma
    for k in range (N):
        for nn in range (N):
            X_re[k] = X_re[k] + (x[nn] * math.cos((-2 *(math.pi * k * nn ))/N))
            X_im[k] = X_im[k] + (x[nn] * math.sin((-2 *(math.pi * k * nn ))/N))


            
#Widmo
    for jj in range (N):
        M[jj] = sqrt(X_re[jj] * X_re[jj] + X_im[jj] * X_im[jj]) # widmo amplitudowe

    threshold = abs(max(M))/10000
    
    for j in range (N):
        ''' Zastosowanie thresholda'''
        if (abs(M[j]) < threshold):
            M[j] = 0

    for y in range(N):
        if(M[y] != 0):
            M_prim.append (10 * log10(M[y])*2/N) #Amplituda w skali decybbelowej przemnozona przez 2/N
        else:
            M_prim.append(0) # zabezpieczenie przed log 0



    def IDFT(X_re,X_im):
        xff=[]
        for nnn in range(N):
            x_ri=0
            for k in range(N):
                x_ri+=(X_re[k]*math.cos((2*(math.pi*k*nnn)/N)))-(X_im[k]*math.sin((2*(math.pi*k*nnn)/N)))
            xff.append(1/N*x_ri)
        plt.figure()
        plt.plot(fk,xff,'.')


    ''' Dla opcji 0 rysuj ton prosty i DFT + IDFT'''
    if(opcja == 0):
        plt.figure()
        plt.plot(tab2,x,'.')
        IDFT(X_re,X_im)
        plt.ylabel('A')
        plt.xlabel('f(Hz)')
        
        

    plt.figure()


    # plt.plot(fk,M_prim)
    plt.plot(fk,M)
    plt.ylabel('A')
    plt.xlabel('f(Hz)')

    


DFT(N,7)
# DFT(N,1)
# DFT(N,2)
# DFT(N,3)
# DFT(N,4)
#DFT(N,7)
# DFT(N,6)
# DFT(N,7)
#plt.savefig('./wykres{}.png'.format(1))
plt.show()

