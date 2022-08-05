import random


def affine_encrypt(text="Hello", a=17, b=20):
    a = int(a)
    b = int(b)
    ans = ""
    for i in text:
        if(i.isupper()):
            temp = chr((a*(ord(i)-65)+b) % 26+65)
            ans = ans+temp
        elif(i.islower()):
            temp = chr((a*(ord(i)-97)+b) % 26+97)
            ans = ans+temp
        else:
            ans = ans+i
    return ans


def affine_decrypt(txt, a=17, b=20):
    a = int(a)
    b = int(b)
    ans = ""
    for i in txt:
        if(i.isupper()):
            temp = chr((pow(a, -1, 26)*(ord(i)-65-b)) % 26+65)
            ans = ans+temp
        elif(i.islower()):
            temp = chr((pow(a, -1, 26)*(ord(i)-97-b)) % 26+97)
            ans = ans+temp
        else:
            ans = ans+i
    return ans


def caesar_encrypt(x="Hello", key=4):
    key = int(key)
    y = ""
    for i in x:
        if(i.isupper()):
            y = y+chr((ord(i)+key-65) % 26+65)
        elif(i.islower()):
            y = y+chr((ord(i)+key-97) % 26+97)
        else:
            y = y+i
    return y


def caesar_decrypt(x, key=4):
    key = int(key)
    y = ""
    for i in x:
        if(i.isupper()):
            y = y+chr((ord(i)+26-key-65) % 26+65)
        elif(i.islower()):
            y = y+chr((ord(i)+26-key-97) % 26+97)
        else:
            y = y+i
    return y


def columnar_encrypt(text="Hello", key="hack"):
    key = str(key)
    temp_key = list(key.strip())
    temp_key.sort()
    temp_key = "".join(temp_key)
    d = []
    for i in range(len(temp_key)):
        d.append(key.index(temp_key[i]))
    ans = ""
    c = 0
    l = []
    if(len(text) <= len(key)):
        return text
    for i in range(len(text)//len(key)):
        temp = []
        for j in range(len(key)):
            temp.append(text[c])
            c = c+1
        l.append(temp)
    if(len(text) % len(key) > 0):
        tp = list(text[(len(text)//len(key))*len(key):].strip())
        l.append(tp+[0]*(len(key)-len(tp)))
    for i in range(len(d)):
        tmp = ""
        for j in range(len(l)):
            if(l[j][d[i]]):
                tmp = tmp+l[j][d[i]]
        ans = ans+tmp
    return ans


def columnar_decrypt(text, key="hack"):
    key = str(key)
    temp_key = list(key.strip())
    temp_key.sort()
    temp_key = "".join(temp_key)
    d = []
    for i in range(len(temp_key)):
        d.append(temp_key.index(key[i]))
    ans = ""
    c = 0
    l = []
    if(len(text) <= len(key)):
        return text
    tmp = []
    for i in range(len(text) % len(key)):
        tmp.append(d[i])
    n = len(text)//len(key)
    f = len(text)//len(key)
    for i in range(len(d)):
        temp = []
        if i in tmp:
            n = (len(text)//len(key))+1
            f = n
        else:
            n = len(text)//len(key)
        for k in range(n):
            temp.append(text[c])
            c = c+1
        l.append(temp)
    li = []
    for i in d:
        li.append(l[i])
    for i in range(f):
        for j in range(len(li)):
            try:
                ans = ans+li[j][i]
            except:
                continue
    return ans


def otp_encrypt(text="Hello", key="XMCKL"):
    ans = ""
    for i in range(len(text)):
        if(text[i].isalpha() and text[i].isupper()):
            ans = ans + \
                chr((((ord(text[i])-65)+(ord(key[i].upper())-65)) % 26)+65)
        elif(text[i].isalpha() and text[i].islower()):
            ans = ans + \
                chr(((((ord(text[i])-97)+(ord(key[i].lower())-97))) % 26)+97)
        else:
            ans = ans+text[i]
    return ans


def otp_decrypt(text="Eqnvz", key="XMCKL"):
    ans = ""
    for i in range(len(text)):
        if(text[i].isalpha() and text[i].isupper()):
            ans = ans + \
                chr(((((ord(text[i])-65)-(ord(key[i].upper())-65))) % 26)+65)
        elif(text[i].isalpha() and text[i].islower()):
            ans = ans + \
                chr(((((ord(text[i])-97)-(ord(key[i].lower())-97))) % 26)+97)
        else:
            ans = ans+text[i]
    return ans


def find_me(l, a):
    x, y, z = 0, 0, 0
    for i in l:
        try:
            y = i.index(a)
            x = z
            z = z+1
            break
        except:
            z = z+1
            continue
    return (x, y)


def cleaner(s):
    i = 0
    s = list(s.strip())
    while i < len(s):
        if (ord(s[i]) < ord('A') or ord(s[i]) > ord('Z') and ord(s[i]) < ord('a') or ord(s[i]) > ord('z')):
            del s[i]
            i -= 1
        i += 1
    return "".join(s).upper().replace("J", "I")


def lets_pair(a):
    groups = []
    for i in range(0, len(a), 2):
        temp = []
        temp2 = []
        try:
            if(a[i] != a[i+1]):
                temp.append(a[i])
                temp.append(a[i+1])
            else:
                temp.append(a[i])
                temp.append("X")
                if(i+2 < len(a)):
                    temp2.append(a[i+1])
                    temp2.append(a[i+2])
                else:
                    temp2.append(a[i+1])
                    temp2.append("Z")
        except:
            temp.append(a[i])
            temp.append("Z")
        groups.append(temp)
        if(len(temp2) > 0):
            groups.append(temp2)

    return groups


def box_it(b):
    b = b.upper()
    l = [["o" for i in range(5)] for j in range(5)]
    b = list(b.strip())
    temp = []
    for i in b:
        if i not in temp:
            temp.append(i)

    b = "".join(temp)

    z = len(b)
    c = 0
    x = 0
    temp = [chr(i) for i in range(65, 91)]
    temp.remove("J")

    for i in b:
        if i in temp:
            temp.remove(i)

    if "J" in b:
        b = b.replace("J", "I")

    for i in range(5):
        for j in range(5):
            if(c < z):
                l[i][j] = b[c]
            else:
                l[i][j] = temp[x]
                x = x+1
            c = c+1
    return l


def play_fair_encrypt(x="Hello", y="key"):
    enc = ""
    l = []
    x = cleaner(x)
    z = lets_pair(x)
    box = box_it(y)
    for i in z:
        pi, pj = find_me(box, i[0])
        qi, qj = find_me(box, i[1])
        if pj == qj:
            l.append(box[(pi+1) % 5][pj]+box[(qi+1) % 5][qj])
            enc = enc+l[-1]
        elif pi == qi:
            l.append(box[pi][(pj+1) % 5]+box[qi][(qj+1) % 5])
            enc = enc+l[-1]
        else:
            l.append(box[pi][qj]+box[qi][pj])
            enc = enc+l[-1]
    return enc


def play_fair_decrypt(x, y="key"):
    denc = ""
    l = []
    x = cleaner(x)
    z = lets_pair(x)
    box = box_it(y)
    for i in z:
        pi, pj = find_me(box, i[0])
        qi, qj = find_me(box, i[1])
        if pj == qj:
            l.append(box[(pi-1) % 5][pj]+box[(qi-1) % 5][qj])
            denc = denc+l[-1]
        elif pi == qi:
            l.append(box[pi][(pj-1) % 5]+box[qi][(qj-1) % 5])
            denc = denc+l[-1]
        else:
            l.append(box[pi][qj]+box[qi][pj])
            denc = denc+l[-1]
    return denc


def Rail_Fence_encrypt(text="Hello", rails=3):
    rails = int(rails)
    l = len(text)
    mat = [["^" for i in range(l)] for j in range(rails)]
    i, j = 0, 0
    c = False
    for k in text:
        if(i == 0 or i == rails-1):
            c = not c
        mat[i][j] = k
        j = j+1
        if(c):
            i = i+1
        else:
            i = i-1
    ans = ""
    for i in mat:
        ans = ans+"".join(i)
    ans = ans.replace("^", "")
    return ans


def Rail_Fence_decrypt(cipher, key=3):
    key = int(key)
    ans = ""
    l = [['^' for i in range(len(cipher))] for j in range(key)]
    z = 0
    m = 0
    while(z < key):
        i, j = 0, 0
        c = False
        for k in range(len(cipher)):
            if(i == 0 or i == key-1):
                c = not c
            if(z == i):
                l[i][j] = cipher[m]
                m = m+1
            j = j+1
            if(c):
                i = i+1
            else:
                i = i-1
        z = z+1
    i, j = 0, 0
    c = False
    for k in cipher:
        if(i == 0 or i == key-1):
            c = not c
        ans = ans+l[i][j]
        j = j+1
        if(c):
            i = i+1
        else:
            i = i-1
    return ans


an = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rn = ['J', 'R', 'V', 'P', 'Z', 'Q', 'O', 'X', 'B', 'I', 'G', 'H', 'E',
      'Y', 'L', 'U', 'K', 'S', 'M', 'D', 'T', 'C', 'F', 'N', 'W', 'A']
am = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rm = ['n', 'o', 'x', 'i', 'w', 'z', 'r', 'f', 'p', 'b', 'g', 'd', 'm',
      's', 'e', 'v', 'q', 't', 'h', 'u', 'k', 'j', 'y', 'c', 'a', 'l']

e = dict(zip(an, rn))
d = dict(zip(am, rm))
ie = {v: k for k, v in e.items()}
ids = {v: k for k, v in d.items()}


def substitution_encrypt(text="Hello"):
    ans = ""
    for i in text:
        if(i.isalpha() and i.isupper()):
            ans = ans+e[i]
        elif(i.isalpha() and i.islower()):
            ans = ans+d[i]
        else:
            ans = ans+i
    return ans


def substitution_decrypt(cipher):
    ans = ""
    for i in cipher:
        if(i.isalpha() and i.isupper()):
            ans = ans+ie[i]
        elif(i.isalpha() and i.islower()):
            ans = ans+ids[i]
        else:
            ans = ans+i
    return ans


def vigenere_encrypt(plaintext="Hello", key="leg"):
    key = str(key)
    key = key.replace(" ", "")
    p = len(plaintext)
    k = len(key)
    if len(plaintext) != len(key):
        q = p//k
        key = key*(q) + key[:p % k]
    ans = []
    for i in range(p):
        if(plaintext[i].isalpha() and plaintext[i].isupper()):
            ans.append(chr((ord(plaintext[i])+ord(key[i])-65) % 26 + 65))
        elif(plaintext[i].isalpha() and plaintext[i].islower()):
            ans.append(chr((ord(plaintext[i])+ord(key[i])-97) % 26 + 97))
        else:
            ans.append(plaintext[i])
    return "".join(ans)


def vigenere_decrypt(ciphertext, key="leg"):
    key = str(key)
    key = key.replace(" ", "")
    p = len(ciphertext)
    k = len(key)

    if len(ciphertext) != len(key):
        q = p//k
        key = key*(q) + key[:p % k]
    ans = []
    for i in range(p):
        if(ciphertext[i].isalpha() and ciphertext[i].isupper()):
            ans.append(chr((ord(ciphertext[i])-ord(key[i])-65+26) % 26 + 65))
        elif(ciphertext[i].isalpha() and ciphertext[i].islower()):
            ans.append(chr((ord(ciphertext[i])-ord(key[i])-97+26) % 26 + 97))
        else:
            ans.append(ciphertext[i])
    return "".join(ans)
