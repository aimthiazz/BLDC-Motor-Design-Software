#Magnetic Design
#Author Imthiaz
#Started 04-02-2017
#Equations which calculate flux density on the motor
#Inner rotor motor is assuemed
#involves simpler calculation
import math
Br=0.4
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
g=[]
print(Bg)
