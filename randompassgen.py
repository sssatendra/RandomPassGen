import random  #importing random module


# defining all lower case ,upper case letters, numbers and symbols
lower="abcdefghijcklmnopqrstwxyz"
upper=lower.upper()
numbers="0123456789"
symbols="{}[]*:;,/,_-"


#concatenate the entire keywords into one variable 
all=lower+upper+numbers+symbols

#Accepting an input for the lenth of the password
while True:

    try:
        Lenght=int(input("enter the Lenght of the password: "))
    except:
        print("Lenght must be an integer")
    else:
        break

#picking up random keyswords from the string of the defined lenght
password="".join(random.sample(all,Lenght))

print(password)