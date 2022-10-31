p = 28151
import math
def ListelFp(p):
    lisfp=[]
    for i in range(p):
        if(math.gcd(i,p)==1):
            lisfp.append(i)
    return lisfp
def eltgenerateur(p):
    lisgen,compteur=[],0
    list_i=range(1,p)
    for i in range(2,p):
        print(i)
        lisele=[]
        for j in range(1,p):
            a=pow(i,j,p)
            if(a in list_i and a not in lisele ):
                lisele.append(a)
                compteur+=1
                
        if(len(list_i)==compteur):
            print("Generateur",i)
            lisgen.append(i)
            exit()
        compteur=0    

print(eltgenerateur(p))