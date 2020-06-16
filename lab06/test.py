import matplotlib.pyplot as plt
import math

def ASCII(tekst):
    napis=''
    for x in tekst:
        napis=napis+bin(ord(x))[2:].zfill(8)
    return list(map(int, list(napis)))

m=ASCII('dj')
A1=1.5
A2=2.5
fs=500
Ts=2
Tb=Ts/len(m)
Tbp=int(Tb*fs)
print(Tbp)
N=int(Ts*fs)

t=[]
fn=[]
fn1=[]
fn2=[]
fk=[]

for n in range(int(N+1)):
    t.append(n/fs)
    fn.append(n/Tb)
    fn1.append((n+1)/Tb)
    fn2.append((n+2)/Tb)
    fk.append(n*fs/N)

m =  [ele for ele in m for i in range (Tbp)] 
m.append(m[-1])

zA=[]
zF=[]
zP=[]

for i in range(len(m)):
    if (m[i] == 0):
        zA.append(A1*math.sin(2*math.pi*fn[i]*t[i]))
        zF.append(math.sin(2*math.pi*fn1[i]*t[i]))
        zP.append(math.sin(2*math.pi*fn[i]*t[i]))
    else:
        zA.append(A2*math.sin(2*math.pi*fn[i]*t[i]))
        zF.append(math.sin(2*math.pi*fn2[i]*t[i]))
        zP.append(math.sin(2*math.pi*fn[i]*t[i]+math.pi))

sa=[]
sn1=[]
sn2=[]
sp=[]

for i in range(len(m)):
    sa.append(A1*math.sin(2*math.pi*fn[i]*t[i]))
    sn1.append(math.sin(2*math.pi*fn1[i]*t[i]))
    sn2.append(math.sin(2*math.pi*fn2[i]*t[i]))
    sp.append(math.sin(2*math.pi*fn[i]*t[i]))


xA=[]
xP=[]
xF1=[]
xF2=[]
for i in range (len(m)):
    xA.append(zA[i]*sa[i])
    xP.append(zP[i]*sp[i])
    xF1.append(zF[i]*sn1[i])
    xF2.append(zF[i]*sn2[i])

pA=[]
pP=[]
pF=[]
for i in range (len(m)):
    A=xA[i]
    P=xP[i]
    F1=xF1[i]
    F2=xF2[i]
    for j in range(i-1,i%Tbp-1,-1):
        A=A+xA[i-j]
        P=P+xP[i-j]
        F1=F1+xF1[i-j]
        F2=F2+xF2[i-j]

    pA.append(A)
    pP.append(P)
    pF.append(F1-F2)

hA=45.0
hP=30.0
hF=30.0
mA=[]
mP=[]
mF=[]
for i in range (len(m)):
    if (pA[i]>hA):
        mA.append(1)
    else:
        mA.append(0)
    if (pP[i]>hP):
        mP.append(1)
    else:
        mP.append(0)
    if (pF[i]>hF):
        mF.append(1)
    else:
        mF.append(0)

def wyswietlanie(nazwa,ylabel,sygnal):
    plt.plot(t[:len(sygnal)], sygnal)
    plt.title(nazwa)    
    plt.xlabel('t')
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()
    return

wyswietlanie('ASK: z(t)', 'z(t)', zA)
wyswietlanie('ASK: x(t)', 'x(t)', xA)
wyswietlanie('ASK: p(t)', 'p(t)', pA)
wyswietlanie('ASK: m(t)', 'm(t)', mA)

wyswietlanie('PSK: z(t)', 'z(t)', zP)
wyswietlanie('PSK: x(t)', 'x(t)', xP)
wyswietlanie('PSK: p(t)', 'p(t)', pP)
wyswietlanie('PSK: m(t)', 'm(t)', mP)

wyswietlanie('fsk, z(t)', 'z(t)', zF)
wyswietlanie('fsk, x1(t)', 'x1(t)', xF1)
wyswietlanie('fsk, x2(t)', 'x2(t)', xF2)
wyswietlanie('fsk p(t)', 'p(t)', pF)
wyswietlanie('FSK m(t)', 'p(t)', mF)