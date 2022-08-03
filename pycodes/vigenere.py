def vigenere_encrypt(plaintext="Hello",key="leg"):
    key=str(key)
    key = key.replace(" ","")
    p = len(plaintext)
    k = len(key)
    if len(plaintext)!=len(key):
        q = p//k
        key = key*(q) + key[:p%k]
    ans = []
    for i in range(p):
        if(plaintext[i].isalpha() and plaintext[i].isupper()):
            ans.append(chr((ord(plaintext[i])+ord(key[i])-65)%26 +65))
        elif(plaintext[i].isalpha() and plaintext[i].islower()):
            ans.append(chr((ord(plaintext[i])+ord(key[i])-97)%26 +97))
        else:
            ans.append(plaintext[i])
    return "".join(ans)

def vigenere_decrypt(ciphertext, key="leg"):
    key=str(key)
    key = key.replace(" ","")
    p = len(ciphertext)
    k = len(key)
    
    if len(ciphertext)!=len(key):
        q = p//k
        key = key*(q) + key[:p%k]
    ans = []
    for i in range(p):
        if(ciphertext[i].isalpha() and ciphertext[i].isupper()):
            ans.append(chr((ord(ciphertext[i])-ord(key[i])-65+26)%26 +65))
        elif(ciphertext[i].isalpha() and ciphertext[i].islower()):
            ans.append(chr((ord(ciphertext[i])-ord(key[i])-97+26)%26 +97))
        else:
            ans.append(ciphertext[i])
    return "".join(ans)