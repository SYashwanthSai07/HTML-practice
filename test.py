import time
string = "Yashwant to be a software engineer"
alphabet = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
for i in range(len(string)):
    for j in alphabet:
        to_print = result + j
        print(to_print); time.sleep(0.01)
        if j == string[i]:
            result += string[i]
            break