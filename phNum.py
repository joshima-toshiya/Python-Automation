
def isPhoneNumber(text):
    if (len(text)!=12):
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if (text[3]!='-'):
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if (text[7]!='-'):
        return False
    for i in range(8,11):
        if not text[i].isdecimal():
            return False
    return True


print("[!]Phone Number extractor")
message=input("Enter the text: ")

for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print("[*]Phone Number found:" + chunk)
print("*DONE!*")
    

