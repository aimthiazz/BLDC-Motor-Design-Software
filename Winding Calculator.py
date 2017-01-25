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
aoffset1=[]
aoffset2=[]
sindex=[]
sindex1=[]
c=0
Ncph=0
A=[]
d=1
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
    print(Ncph)
    for i in range(0,Ns):
        In.append(i+1)
        Out.append((In[i]+S)%Ns)
        if(Out[i]==0):
            Out[i]=Ns
        aoffset.append(math.ceil(i * (Nm / Ns) * 180))
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
    for i in range(0,len(aoffset)):
        aoffset1.append(abs(aoffset[i]))
    aoffset2=sorted(aoffset1)
    aoffset3=aoffset2[:int(Ncph)]
    for i in range(0,len(aoffset3)):
        for j in range(0,len(aoffset)):

            if (aoffset3[i]== aoffset1[j]):
                sindex.append(j)



    ##aoffset1=sorted((aoffset))
    ##print(In)
    ##print(Out)
    print(aoffset)
    print(rindex)
    print(aoffset1)
    print(aoffset2)
    print(aoffset3)
    print(sindex)
    print(set(sindex))
    sindex1=list(set(sindex))

## PRINTING PHASE A
    print("PHASE A WINDING")
    for i in range(0, len(sindex1)):
        k = int(sindex1[i])
        print(In[k], '\t' , Out[k])

    print("")
    print("")
    print("")

## PRINTING PHASE B
    print("PHASE B WINDING")
    for i in range(0, len(sindex1)):
        k = int(sindex1[i])
        print(int((In[k]+Ko)%Ns), '\t' , int((Out[k]+Ko)%Ns))

## PRINTING PHASE C
    print("PHASE C WINDING")
    for i in range(0, len(sindex1)):
        k = int(sindex1[i])
        print(int((In[k]+2*Ko)%Ns), '\t' , int((Out[k]+2*Ko)%Ns))





else:
    print("The Slot/Pole Combination won't work")

