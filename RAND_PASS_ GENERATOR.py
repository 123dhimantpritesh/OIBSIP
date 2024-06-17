import string
import random

l = int(input("Enter Password Length: "))
print ('''choose character set for password from these :
       1. Digits
       2. Letters
       3. Special Characters
       4. Exit ''')
cl=""
while(True):
    choice=int(input("pick a number "))
    if (choice==2):
        cl+=string.ascii_letters
    elif(choice==1):
        cl+=string.digits
    elif(choice==3):
        cl+=string.punctuation
    elif(choice==4):
        break
    else:
        print("please choose a valid option ! ")
Pass= []
for i in range(l):
    randchar=random.choice(cl)
    Pass.append(randchar)
print("The random password is " + "".join(Pass))                         