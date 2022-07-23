from functools import reduce
from math import gcd
def inv_mod(a,n):
    if(gcd(a,n)!=1):
        return "A et N ne sont pas premiers entre eux"
    for i in range(1,n):
        if((i*a)%n==1):
            return i

def chinese_theorem(**all_primes):
    N=reduce(lambda x,y:x*y,list(all_primes.values()))
    answer_n=0
    for residu,prime_val in all_primes.items():
        mi=N//prime_val
        answer_n+=int(residu)*mi*inv_mod(mi,prime_val)
    return answer_n%N

print(chinese_theorem(**{"2":5,"3":11,"5":17}))