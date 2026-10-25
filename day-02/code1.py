# this is a comment
#This is my Code

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
fence_length = 2 * (length + width)
print("Fencing needed:", fence_length)


#This is my Code
rate = 1.50
num_books = int(input("Number of books: "))
weeks_late = int(input("Weeks late: "))
fine = num_books * weeks_late * rate
print("The fine is R", fine)

#Highest common factor (Probm4)
first = int(input("Enter the first Number: "))
second = int(input("Enter the second Number: "))

if first < second:
    factor = first
else:
    factor = second
        
while first % factor !=0 or second % factor !=0:
    factor = factor - 1
        
print("the highest common fator is: ", factor)