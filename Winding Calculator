# BLDC Winding Calculator
#Author Imthiaz
#Started on 22_01_2017
#Calculates winding pattern for BLDC Motor with coilspan of 120deg and 3 Phase
import math
Ns=int(input("Enter the Number of Slots"))
Nm=int(input("Enter the Number of Poles"))
q=1
Ko=0.5
count=0
In=[]
Out=[]
aoffset=[]
angle=[]
rindex=[]
c=0
while(q<=((Nm/2)-1) and Ko%1!=0):
    Ko=((2*Ns)/(3*Nm))*(1+3*q)
    q=q+1
print(Ko) # Delete this
if(Ko%1==0 and Nm%2==0 and Ns%3==0 ):
    ##Program Proceeds
    print("Here we go")
    S= max(math.floor(Ns/Nm),1) # Coil Span
    print(S) #Delete this
    Ncph=Ns/3 #Number of Coils / Phase (3 phase is considered in this case)
    for i in range(0,Ns):
        In.append(i+1)
        Out.append((In[i]+S)%Ns)
        if(Out[i]==0):
            Out[i]=Ns
        aoffset.append(i * (Nm / Ns) * 180)
        if(abs(aoffset[i])>180):
            aoffset[i]=((aoffset[i]+180)%360)-180
        if(abs(aoffset[i])>90 and aoffset[i]>0):
            aoffset[i]=aoffset[i]-180
            rindex.append(i)
        elif(abs(aoffset[i])>90 and aoffset[i]<0):
            aoffset[i]=(aoffset[i]-180) % 360
            rindex.append(i)
    for i in range(0,len(rindex)):
        ##print(rindex[i])
        c=In[rindex[i]]
        In[rindex[i]]=Out[rindex[i]]
        Out[rindex[i]]=c

    print(In)
    print(Out)
    print(aoffset)
    print(rindex)




else:
    print("The Slot/Pole Combination won't work")

