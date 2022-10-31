import os
import hashlib
import requests
import time

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
URL= "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"

cipher_text = requests.get("http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/").json()['ciphertext']
print(cipher_text)
res = requests.get(URL).text
words_file_path=f"{path}\\words.txt"
with open(words_file_path,"w",encoding='utf-8') as f:
    f.write(res)
i=0
with open(words_file_path,"r",encoding='utf-8') as f:
    start_time=time.time()    
    for word in f.read().split('\n'):
        password_hash=hashlib.md5(word.strip().encode()).hexdigest()
        
        decrypt_response=requests.get(f'http://aes.cryptohack.org/passwords_as_keys/decrypt/{cipher_text}/{password_hash}/')
        print(f"code {decrypt_response.status_code}, word n°{i}")
        if(decrypt_response.status_code<400):
            plain_text=decrypt_response.json()['plaintext']
            if(plain_text):
                plain_text=bytes.fromhex(plain_text)
                if(b'crypto' in plain_text):
                    print(f"The flag is {plain_text} ,taken {time.time()-start_time}")
                    break
        i+=1        
# Delete word file
os.remove(words_file_path)            