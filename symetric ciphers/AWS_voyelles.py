voyelles=['a', 'e', 'i', 'o', 'u', 'y']
count=0
word = input('Entrer un mot !')
for letter in word:
    if(letter in voyelles):
        count+=1
print('Le nombre de voyelles est : {}'.format(count))        