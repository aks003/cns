def xor(div,dis):
    res=[]
    for i in range(1,len(div)):
        if div[i]==dis[i]:
            res.append('0')
        else:
            res.append('1')
    return ''.join(res)

def mod2div(div,dis):
    p=len(dis)
    tmp=div[:p]
    while p<len(div):
        if tmp[0]=='1':
            tmp=xor(tmp,dis)+div[p]
        else:
            tmp=tmp[1:]+div[p]
        p+=1
    if tmp[0]=='1':
        tmp=xor(tmp,dis)
    return tmp

def encrypt(data,dis):
    data_a=data+'0'*(len(dis)-1)
    rem=mod2div(data_a,dis)
    enc=data+rem
    print("Checksum is",rem)
    print("Encrypted data is",enc)
    data_rec=input("Enter the data receieved ")
    if int(mod2div(data_rec,dis))==0:
        print("No error")
    else:
        print("error")

data=input("Enter the data in binary :")
key=input("Enter the key in binary :")
k=key.find('1')
key=key[k:]
encrypt(data, key)
