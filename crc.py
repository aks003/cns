
def xor(a, b):
    # print(b)
    result = []
    for i in range(1, len(b)):
        # print(i)
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    # print(result)
    return ''.join(result)
 
 
def mod2div(dividend, divisor):

    pick = len(divisor)
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else:   
            tmp = tmp[1:] + dividend[pick]
        pick += 1
 
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)

 
    checkword = tmp
    return checkword
 

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Encoded Data (Data + Remainder) : ",codeword)
    data_received=input("Enter the data received in binary :")
    if data_received != codeword:
    	print("Error is detected")
    else:
    	print("No error is detected")
# Driver code
data=input("Enter the data in binary :")
key=input("Enter the key in binary :")
ind=key.find("1")
key=key[ind:]
encodeData(data, key)
