#Magnetic Design
#Author Imthiaz
#Started 02-02-2017
#Equations which calculate flux density on the motor
#Inner rotor motor is assuemed
import math
Ns=int(input("Enter the Number of Slots"))
Nm=int(input("Enter the Number of Poles"))
Rs=float(input("Enter the stator radius")) ## temporary)
Rr=float(input("Enter the rotor radius"))
Rm=float(input("Enter the radius at which the magnet ends"))
amc=float(input("Enter the manget fraction")) ## Remember pole embrace in Maxwell tool
n=1 ## Assume Fundamental component
pi=math.pi
uo=4*pi*1e-7
uair=4*pi*1e-7
urair=uo/uair
beta=n*(Nm/2)
Br=1.26 # NdFeB 38/15 Br value
#Rs=Rs*1e-3
#Rr=Rr*1e-3
#Rm=Rm*1e-3
krn=amc*(math.sin((n*amc*pi)/2)/(n*amc*pi)/2)
K0n=0
delr=(urair+1)*(pow((Rr/Rm),(2*beta))-pow((Rs/Rm),(2*beta))) + (urair-1)*(1-(pow((Rr/Rm),(2*beta))*pow((Rs/Rm),(2*beta))))
Kmc=krn/(1-(beta*beta))
Ka=((Kmc*krn)/delr)*(1-pow((Rr/Rm),(2*beta)))*((beta+1)*pow((Rr/Rm),(2*beta))-(2*beta)*pow((Rr/Rm),(beta+1))+(beta-1))
Barn=-(Br*Ka)*((pow((Rs/Rm),(beta-1)))+(pow((Rs/Rm),(2*beta))*pow((Rm/Rs),(beta+1))))
print(pi)
print(krn)
print(urair)
print(delr)
print(Kmc)
print(Ka)
print(Barn)
