# import random
# import string

# lm=list(i for i in string.ascii_uppercase)
# slm=lm.copy()
# random.shuffle(slm)
# sm=list(i for i in string.ascii_lowercase)
# ssm=sm.copy()
# random.shuffle(ssm)
# otpe=dict(zip(lm,slm))
# otpd=dict(zip(sm,ssm))
# otpie={v: k for k, v in otpe.items()}
# otpids={v: k for k, v in otpd.items()}

def otp_encrypt(text="Hello",key="XMCKL"):
    ans=""
    for i in range(len(text)):
        if(text[i].isalpha() and text[i].isupper()):
            ans=ans+chr((((ord(text[i])-65)+(ord(key[i].upper())-65))%26)+65)
        elif(text[i].isalpha() and text[i].islower()):
            ans=ans+chr(((((ord(text[i])-97)+(ord(key[i].lower())-97)))%26)+97)
        else:
            ans=ans+text[i]
    return ans

def otp_decrypt(text="Eqnvz",key="XMCKL"):
    ans=""
    for i in range(len(text)):
        if(text[i].isalpha() and text[i].isupper()):
            ans=ans+chr(((((ord(text[i])-65)-(ord(key[i].upper())-65)))%26)+65)
        elif(text[i].isalpha() and text[i].islower()):
            ans=ans+chr(((((ord(text[i])-97)-(ord(key[i].lower())-97)))%26)+97)
        else:
            ans=ans+text[i]
    return ans
