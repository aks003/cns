key=str(input("Enter the key ").upper()).replace(" ", "")
mat=[[i for i in range(5)]for x in range(5) ]
# print (mat)
res=list()
for c in key:
    if c not in res:
        if c=='J':
            res.append('I')
        else:
            res.append(c)
for i in range(65,91):
    c=chr(i)
    if c not in res:
        if c=="J" :
            pass
        else:
            res.append(c)
print(res)
for i in range(5):
    for j in range(5):
        mat[i][j]=res[5*i+j]

def loc(c):
    if c == 'J':
        c='I'
    for i,x in enumerate(mat):
        if c in x:
            return [i,x.index(c)] 

def encrypt():
    msg=str(input("Enter the message ").upper()).replace(" ", "")
    for i in range(0,len(msg),2):
        if msg[i]==msg[i+1]:
            msg=msg[:i+1]+"X"+msg[i+1:]
    if len(msg)%2 !=0:
        msg+="X"
    for i in range(0,len(msg),2):
        l1=loc(msg[i])
        l2=loc(msg[i+1])
        if l1[0]==l2[0]:
            print(mat[l1[0]][(l1[1]+1)%5]+mat[l2[0]][(l2[1]+1)%5],end=" ")
        elif l1[1]==l2[1]:
            print(mat[(l1[0]+1)%5][l1[1]]+mat[(l2[0]+1)%5][l2[1]],end=" ")
        else:
            print(mat[l1[0]][l2[1]]+mat[l2[0]][l1[1]],end=" ")

def decrypt():
    msg=str(input("Enter the encrypted message ").upper()).replace(" ", "")
    for i in range(0,len(msg),2):
        l1=loc(msg[i])
        l2=loc(msg[i+1])
        if l1[0]==l2[0]:
            print(mat[l1[0]][(l1[1]-1)%5]+mat[l2[0]][(l2[1]-1)%5],end=" ")
        elif l1[1]==l2[1]:
            print(mat[(l1[0]-1)%5][l1[1]]+mat[(l2[0]-1)%5][l2[1]],end=" ")
        else:
            print(mat[l1[0]][l2[1]]+mat[l2[0]][l1[1]],end=" ")
# print(mat)
encrypt()
print()
decrypt()
print()