P = 23
G = 9
print('The Value of P is ',P)
print('The Value of G is ',G)
a = int(input('Enter the private key for A: '))
x = int(pow(G,a,P))
b = int(input('Enter the Private Key for B: '))
y = int(pow(G,b,P))
print("The exchanged X is",x,"Y is",y)
ka = int(pow(y,a,P))
kb = int(pow(x,b,P))
print('Secret key for the A is :',(ka))
print('Secret Key for the B is :',(kb))
