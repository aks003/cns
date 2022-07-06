def encrypt(text,key):
    result=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+=chr((ord(char)-65+key)%26+65)
        else:
            result+=chr((ord(char)-97+key)%26+97)
    return result
text=input("Enter the text : ")
key=int(input("Enter the key : "))
print("Encrypted text : ",encrypt(text,key))