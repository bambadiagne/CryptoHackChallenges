# from itertools import count
# import requests
# BASE_URL="http://aes.cryptohack.org/ecb_oracle"
# plain_text='41'        
# count=1
# cipher_text=requests.get(f'{BASE_URL}/encrypt/{plain_text}/').json()['ciphertext']
# tmp=cipher_text
# while(count<3):
#     cipher_text=requests.get(f'{BASE_URL}/encrypt/{plain_text}/').json()['ciphertext']
#     if(len(cipher_text)>len(tmp)):
#         print(cipher_text,len(plain_text)/2)
#         count+=1
#     plain_text+="41"
#     tmp=cipher_text
    
# print(count,cipher_text)
