def Rail_Fence_encrypt(text="Hello",rails=3):
    rails=int(rails)
    l=len(text)
    mat=[["^" for i in range(l)] for j in range(rails)]
    i,j=0,0
    c=False
    for k in text:
        if(i==0 or i==rails-1):
            c=not c
        mat[i][j]=k
        j=j+1
        if(c):
            i=i+1
        else:
            i=i-1
    ans=""
    for i in mat:
        ans=ans+"".join(i)
    ans=ans.replace("^","")
    return ans

def Rail_Fence_decrypt(cipher, key=3):
    key=int(key)
    ans=""
    l=[['^' for i in range(len(cipher))] for j in range(key)]
    z=0
    m=0
    while(z<key):
        i,j=0,0
        c=False
        for k in range(len(cipher)):
            if(i==0 or i==key-1):
                c=not c
            if(z==i):
                l[i][j]=cipher[m]
                m=m+1
            j=j+1
            if(c):
                i=i+1
            else:
                i=i-1
        z=z+1
    i,j=0,0
    c=False
    for k in cipher:
        if(i==0 or i==key-1):
            c=not c
        ans=ans+l[i][j]
        j=j+1
        if(c):
            i=i+1
        else:
            i=i-1
    return ans
