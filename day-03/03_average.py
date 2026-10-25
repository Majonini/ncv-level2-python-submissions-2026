#Write a Python program that captures four quiz marks,
#calculates their average, and displays the result
#to two decimal places.
mark1 = float(input("Enter quiz mark 1: "))
mark2 = float(input("Enter quiz mark 2: "))
mark3 = float(input("Enter quiz mark 3: "))
mark4 = float(input("Enter quiz mark 4: "))

average = (mark1 + mark2 + mark3 + mark4) / 4

print(f"Average mark: {average:.2f}")
