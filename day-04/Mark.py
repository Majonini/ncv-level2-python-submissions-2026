Mark = int(input("Please Enter a Mark: "))
if Mark >=0 and Mark <=100:
    if Mark >= 50 and Mark <75:
        print("You PASS")
    elif Mark >= 75:
        print("You got Distinction")
    elif Mark < 50:
        print("You FAIL")
else:
    print("The Mark must be between 0 and 100")