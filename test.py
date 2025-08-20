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

print("\n\n\n")
print("Final Result: " + result)
print("Length of the string is: " + str(len(result)))
print("Time taken to print the string: " + str(len(result) * 0.01) + " seconds") 