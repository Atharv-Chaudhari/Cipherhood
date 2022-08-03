def affine_encrypt(text="Hello",a=17,b=20):
    a=int(a)
    b=int(b)
    ans=""
    for i in text:
        if(i.isupper()):
            temp=chr((a*(ord(i)-65)+b)%26+65)
            ans=ans+temp
        elif(i.islower()):
            temp=chr((a*(ord(i)-97)+b)%26+97)
            ans=ans+temp
        else:
            ans=ans+i
    return ans

def affine_decrypt(txt,a=17,b=20):
    a=int(a)
    b=int(b)
    ans=""
    for i in txt:
        if(i.isupper()):
            temp=chr((pow(a,-1,26)*(ord(i)-65-b))%26+65)
            ans=ans+temp
        elif(i.islower()):
            temp=chr((pow(a,-1,26)*(ord(i)-97-b))%26+97)
            ans=ans+temp
        else:
            ans=ans+i
    return ans
