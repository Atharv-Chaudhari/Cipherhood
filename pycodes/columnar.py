def columnar_encrypt(text="Hello",key="hack"):
    key=str(key)
    temp_key=list(key.strip())
    temp_key.sort()
    temp_key="".join(temp_key)
    d=[]
    for i in range(len(temp_key)):
        d.append(key.index(temp_key[i]))
    ans=""
    c=0
    l=[]
    if(len(text)<=len(key)):
        return text
    for i in range(len(text)//len(key)):
        temp=[]
        for j in range(len(key)):
            temp.append(text[c])
            c=c+1
        l.append(temp)
    if(len(text)%len(key)>0):
        tp=list(text[(len(text)//len(key))*len(key):].strip())
        l.append(tp+[0]*(len(key)-len(tp)))
    for i in range(len(d)):
        tmp=""
        for j in range(len(l)):
            if(l[j][d[i]]):
                tmp=tmp+l[j][d[i]]
        ans=ans+tmp 
    return ans

def columnar_decrypt(text,key="hack"):
    key=str(key)
    temp_key=list(key.strip())
    temp_key.sort()
    temp_key="".join(temp_key)
    d=[]
    for i in range(len(temp_key)):
        d.append(temp_key.index(key[i]))
    ans=""
    c=0
    l=[]
    if(len(text)<=len(key)):
        return text
    tmp=[]
    for i in range(len(text)%len(key)):
        tmp.append(d[i])
    n=len(text)//len(key)
    f=len(text)//len(key)
    for i in range(len(d)):
        temp=[]
        if i in tmp:
             n=(len(text)//len(key))+1
             f=n
        else:
            n=len(text)//len(key)
        for k in range(n):
            temp.append(text[c])
            c=c+1
        l.append(temp)
    li=[]
    for i in d:
        li.append(l[i])
    for i in range(f):
        for j in range(len(li)):
            try:
                ans=ans+li[j][i]
            except:
                continue
    return ans