file=open("data\holder.gitkeep")
have=input("Does the Female has a BRCA1,2 mutation? (Y=Yes, N=No) ")

import random
def Mutate_DNA(seq):
    mut=""
    place = random.randint(0,len(seq)-1)
    nuc=random.randint(1,4)
    for i in range (len(seq)):
      if i==place and nuc !=seq[i]:
        if nuc == 1:
            mut+="A"
        elif nuc == 2:
            mut+="T"
        elif nuc == 3:
            mut+="C"
        elif nuc == 4:
            mut+="G"
      else:
       mut+=seq[i] 
    return mut   

def Delete_DNA(seq):
    place = random.randint(0,len(seq)-1)
    mut = seq[:place] + seq[place+1:]
    return mut   

def Insert_DNA(seq):
    place = random.randint(0,len(seq)-1)
    nuc=random.randint(1,4)
    mut = seq[:place]
    if nuc == 1:
      mut+="A"
    elif nuc == 2:
      mut+="T"
    elif nuc == 3:
      mut+="C"
    elif nuc == 4:
      mut+="G"
    mut +=seq[place:]
    return mut 

def DNA_RNA_Cod(seq):
   seq= seq.upper()
   RNA = ""
   for i in range(len(seq)):
     if seq[i]=="T":
      RNA+="U"
     else:
      RNA+=seq[i]
      
   return RNA 

def Comp_seq(old,new):
  counter=0
  for i in range (len(old)-1):
    if old[i]!=new[i]:
      counter+=1
  return counter

seq=""

for line in file:
   seq+=DNA_RNA_Cod(line)
   mut=seq
count=0
sum=0
y=0
n=0
for i in range(1000):
 time=0
 while mut== seq:
   time+=1
   typ=random.randint(1,3)
   if typ==1:
     seq=Mutate_DNA(seq)
   elif typ==2:
     Delete_DNA(seq)
   elif typ==3:
      Insert_DNA(seq)
 sum+=time
 count+=1
 if have=="N" and count>=2:
   n+=1
 if have=="Y" and count>=1:
   y+=1

years=sum*24

if have=="Y":
  print("For a female that does have BRCA1,2 Mutation: The mutation that will change the P53 protein will take in average",round(y/years,4),"years.")

else:
  print("For a female that does not have BRCA1,2 Mutation: The mutation that will change the P53 protein will take in average",round(n/years,4),"years.")