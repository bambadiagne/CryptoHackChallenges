# Determination de l'age
age=input('Quel est votre âge?')
#Determination du prix
prix_total=0
if(age<18):#Si la personne est mineure
    print("Le prix du billet est de 7 £")
    prix_total+=7
else:#Si la personne est majeure
    print("Le prix du billet est de 12 £")
    prix_total+=12
popcorn_request=""
while(popcorn_request!='OUI' and popcorn_request!="NON"):
    popcorn_request=input('Voulez vous du popcorn?(OUI|NON)').upper()
    if(popcorn_request=="OUI"):
        print('Le prix du popcorn est de 5 £')
        prix_total+=5
print("Le prix total est {}".format(prix_total))            