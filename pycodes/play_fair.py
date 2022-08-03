def find_me(l,a):
    x,y,z=0,0,0
    for i in l:
        try:
            y=i.index(a)
            x=z
            z=z+1
            break
        except:
            z=z+1
            continue
    return (x,y)
    
def cleaner(s):
    i = 0
    s=list(s.strip())
    while i < len(s):
        if (ord(s[i]) < ord('A') or ord(s[i]) > ord('Z') and ord(s[i]) < ord('a') or ord(s[i]) > ord('z')):
            del s[i]
            i -= 1
        i += 1
    return "".join(s).upper().replace("J","I")

def lets_pair(a):
    groups=[]
    for i in range(0,len(a),2):
        temp=[]
        temp2=[]
        try:
            if(a[i]!=a[i+1]):
                temp.append(a[i])
                temp.append(a[i+1])
            else:
                temp.append(a[i])
                temp.append("X")
                if(i+2<len(a)):
                    temp2.append(a[i+1])
                    temp2.append(a[i+2])
                else:
                    temp2.append(a[i+1])
                    temp2.append("Z")
        except:
            temp.append(a[i])
            temp.append("Z")
        groups.append(temp)
        if(len(temp2)>0):
            groups.append(temp2)

    return groups
        
def box_it(b):
    b=b.upper()
    l=[["o" for i in range(5)] for j in range(5)]
    b=list(b.strip())
    temp=[]
    for i in b:
        if i not in temp:
            temp.append(i)
    
    b="".join(temp)
    
    z=len(b)
    c=0
    x=0
    temp=[chr(i) for i in range(65,91)]
    temp.remove("J")
    
    for i in b:
        if i in temp:
            temp.remove(i)
            
    if "J" in b:
        b=b.replace("J","I")
        
    for i in range(5):
        for j in range(5):
            if(c<z):
                l[i][j]=b[c]
            else:
                l[i][j]=temp[x]
                x=x+1
            c=c+1
    return l

def play_fair_encrypt(x="Hello",y="key"):
    enc=""
    l=[]
    x=cleaner(x)
    z=lets_pair(x)
    box=box_it(y)
    for i in z:
        pi,pj=find_me(box,i[0])
        qi,qj=find_me(box,i[1])
        if pj==qj:
            l.append(box[(pi+1)%5][pj]+box[(qi+1)%5][qj])
            enc=enc+l[-1]
        elif pi==qi:
            l.append(box[pi][(pj+1)%5]+box[qi][(qj+1)%5])
            enc=enc+l[-1]
        else:
            l.append(box[pi][qj]+box[qi][pj])
            enc=enc+l[-1]
    return enc
    
def play_fair_decrypt(x,y="key"):
    denc=""
    l=[]
    x=cleaner(x)
    z=lets_pair(x)
    box=box_it(y)
    for i in z:
        pi,pj=find_me(box,i[0])
        qi,qj=find_me(box,i[1])
        if pj==qj:
            l.append(box[(pi-1)%5][pj]+box[(qi-1)%5][qj])
            denc=denc+l[-1]
        elif pi==qi:
            l.append(box[pi][(pj-1)%5]+box[qi][(qj-1)%5])
            denc=denc+l[-1]
        else:
            l.append(box[pi][qj]+box[qi][pj])
            denc=denc+l[-1]
    return denc