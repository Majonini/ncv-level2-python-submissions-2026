total = 0
n = int(input("Enter Number: "))

for x in range(1,n+1):
    cube = x**3
    print(cube, end=" , ")
total = total + cube
print ("Total:", total)