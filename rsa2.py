from math import gcd
p=17 
q=11
n=p*q
fi=(p-1)*(q-1)
d=-1
k=1
e=2
while(gcd(e,fi)!=1):
    e+=1
# e=17
print("Public Key = (n= ",n," ,e= ",e,")")

while True:
    d=(1+(k*fi))/e
    if (d.is_integer()):
        break
    k+=1
enc=list()
def encrypt():
    msg=str(input("Enter the message ").upper())
    print(msg)
    # enc.clear ()
    for i in msg:
        enc.append(str(pow(ord(i),e,n)))
    print(" ".join(enc))

def decrypt():
    dec=list()
    print("private key = ",int(d))
    for i in enc:
        dec.append(chr(pow(int(i),int(d),n)))
    print("".join(dec))
encrypt()
decrypt()
    