
count = 0
total = 0

while True:
    mark = float(input("Enter mark (-1 to stop): "))

    if mark == -1:
        break

    if 0 <= mark <= 100:
        total += mark
        count += 1
    else:
        print("Invalid mark. Enter a mark between 0 and 100.")

print("\n--- RESULTS ---")
print("Number of valid marks:", count)
print("Total of valid marks:", total)

if count > 0:
    average = total / count
    print(f"Average mark: {average:.2f}")
else:
    print("No valid marks were entered.")
