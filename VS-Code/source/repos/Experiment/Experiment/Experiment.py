usr_inp=""
while True:
    usr_inp=input("Enter a number<space>convert-type or exit \n\r")
    usr_inp=usr_inp.lower()
    words=usr_inp.split(" ")
    
    if usr_inp=="exit":
        break
    elif words[1]=="hex":
        print(f'Hexadecimal:{hex(int(words[0]))}')
    elif words[1]=="bin":
        print(f'Binary:{bin(int(words[0]))}')
    elif words[1]=="oct":
        print(f'Octal:{oct(int(words[0]))}')
    else:
        print("sorry, didn't get that!")