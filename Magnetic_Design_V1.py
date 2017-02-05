#Magnetic Design
#Author Imthiaz
#Started 04-02-2017
#Equations which calculate flux density on the motor
#Inner rotor motor is assuemed
#involves simpler calculation
import math
import matplotlib.pyplot as plt
Ns=int(input("Enter the Number of Slots"))
Nm=int(input("Enter the Number of Poles"))
Rs=float(input("Enter the stator radius")) ## temporary)
Rr=float(input("Enter the rotor radius"))
Rm=float(input("Enter the radius at which the magnet ends"))
amc=float(input("Enter the manget fraction")) ## Remember pole embrace in Maxwell tool
Br=float(input("Enter the Br"))
kl=0.95
kr=1.1
pi=math.pi
uo=4*pi*1e-7
uair=4*pi*1e-7
lm=float(input("Enter the length of Magnet"))
g=float(input("Enter the airgap"))
urair=uo/uair
Co=1
Pc=lm/(g*Co)
Bg=(kl*Co)*Br/(1+kr*(urair/Pc))
g1=[]
ksl=[]
print(Bg)
tetat=float(input("Enter the teeth angle"))
tetas=float(input("Enter the slot angle"))
#for i in range(0,int((tetas*100/2)-(tetat*100/2))+1):
#    g1.append(1-((180/Nm)*(Rs/g)*(((float(i)/100)+tetas/2)+tetat/2)))
#for j in range(0,int((tetas*100/2)-(tetat*100/2))+1):
#    ksl.append((1+(lm/(g*urair)))/(g1[i]+(lm/(g*urair))))
teta=[]
teta.append(0)
teta.append((tetas/2)-(tetat/2))
teta.append(tetat)
teta.append((tetas/2)-(tetat/2)+tetat)
ksl.append(0)
ksl.append(Bg)
ksl.append(Bg)
ksl.append(0)

print(teta)
print(ksl)
plt.interactive(True)
plt.plot(teta,ksl)
input("Enter something")
