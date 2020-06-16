import math
from math import log10, sqrt

import matplotlib.pyplot as plt

N=400
fs=500
A = 1.0
fm = 2.0
fn = 10 * fm
### Deklaracja tablic
X_re = []; X_im = []; M = []; M_prim = []; x = []; tab2 = []; fk = []

def funkcja1(kaa,kpp):
    ka = kaa
    kp = kpp
    def sygnal(t):
        return A *math.sin(2*math.pi*fm*t)

    def modulacjaA(t):
        return (ka * sygnal(t)+1) * math.cos(2 * math.pi * fn *t)

    def modulacjaF(t):
        return math.cos(2 * math.pi * fn * t + kp * sygnal(t))

    tZero = 0; tN = 1; deltaT =(1.0/1300); tn = tZero; n = 0
    tab = []; x = []; tab3 = []

    while(tn <= tN):
#### WYBROR MODULACJI
        tab.append(tn)
        #x.append( modulacjaA(tn) )
        x.append( modulacjaF(tn) )

        tab2.append(modulacjaA(tn))
        tn=tZero + (n * deltaT)
        n = n + 1
########################################### D F T #######################
    for i in range (N):
        X_re.append(0.0)
        X_im.append(0.0)
        M.append(0.0)
        fk.append(i * (fs/N) ) #skala częstotliwości wektor z krokiem fs/N

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

##############################ZAD.3
    W=max(x)-min(x)
    W2=max(tab2)-min(tab2)
    print(W)
    print(W2)
    #### PODPUNKT A
    ### ---> Dla Modulacji Amplitudy 1.9999963945630483
    ### ---> Dla Modulacji Fazowej 2.973770765224616
    #### PODPUNKT B
    ### ---> Dla Modulacji Amplitudy 1.9999848822476674
    ### ---> Dla Modulacji Fazowej 13.698094687539804
    #### PODPUNKT C
    ### ---> Dla Modulacji Amplitudy 1.9996054971375312
    ### ---> Dla Modulacji Fazowej 133.84195510558305
############################ RYSOWANIE WYKRESOW ################

    plt.plot(tab,x,'.')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.figure()
    plt.plot(fk,M_prim,'.')
    plt.figure()
    plt.plot(fk,M,'.')
    #plt.plot(tab,tab3,'.')

funkcja1(0.5,1)
#funkcja1(6,2.5)
#funkcja1(67,85)
plt.show()
