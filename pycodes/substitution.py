import random

an=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rn=['J', 'R', 'V', 'P', 'Z', 'Q', 'O', 'X', 'B', 'I', 'G', 'H', 'E', 'Y', 'L', 'U', 'K', 'S', 'M', 'D', 'T', 'C', 'F', 'N', 'W', 'A']
am=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rm=['n', 'o', 'x', 'i', 'w', 'z', 'r', 'f', 'p', 'b', 'g', 'd', 'm', 's', 'e', 'v', 'q', 't', 'h', 'u', 'k', 'j', 'y', 'c', 'a', 'l']

e=dict(zip(an,rn))
d=dict(zip(am,rm))
ie={v:k for k,v in e.items()}
ids={v:k for k,v in d.items()}

def substitution_encrypt(text="Hello"):
    ans=""
    for i in text:
        if(i.isalpha() and i.isupper()):
            ans=ans+e[i]
        elif(i.isalpha() and i.islower()):
            ans=ans+d[i]
        else:
            ans=ans+i
    return ans

def substitution_decrypt(cipher):
    ans=""
    for i in cipher:
        if(i.isalpha() and i.isupper()):
            ans=ans+ie[i]
        elif(i.isalpha() and i.islower()):
            ans=ans+ids[i]
        else:
            ans=ans+i
    return ans

