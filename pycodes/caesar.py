def caesar_encrypt(x="Hello",key=4):
    key=int(key)
    y=""
    for i in x:
        if(i.isupper()):
            y=y+chr((ord(i)+key-65)%26+65)
        elif(i.islower()):
            y=y+chr((ord(i)+key-97)%26+97)
        else:
            y=y+i
    return y

def caesar_decrypt(x,key=4):
    key=int(key)
    y=""
    for i in x:
        if(i.isupper()):
            y=y+chr((ord(i)+26-key-65)%26+65)
        elif(i.islower()):
            y=y+chr((ord(i)+26-key-97)%26+97)
        else:
            y=y+i
    return y