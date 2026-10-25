
count = 0
total = 0

while True:
    mark = int(input("Enter a mark (enter -1 to stop): "))

    if mark == -1:
        break

    if mark >= 0 and mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print("Invalid mark! Enter a mark from 0 to 100.")

print("\n--- RESULTS ---")
print("Number of valid marks:", count)
print("Total of valid marks:", total)

if count > 0:
    average = total / count
    print(f"Average mark: {average:.2f}")
else:
    print("No valid marks were entered.")
