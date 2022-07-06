a=str(input("Enter the text ").upper())
b=str(input("Enter the key  ").upper())
k=0
print (a)
enc=""
dec=""
for i in range(len(a)):
    enc+=chr((ord(a[i])+ord(b[i%len(b)]))%26+ord('A'))
for i in range(len(enc)):
    dec+=chr((ord(enc[i])-ord(b[i%len(b)])+26)%26+ord('A'))
print(enc)
print(dec)