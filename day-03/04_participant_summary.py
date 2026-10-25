'''
Create a Python program that accepts a staff member's full name,
staff number, and level. The program must reject an
empty name or a staff number containing non-numeric
characters. If the input is valid, display a standardised summary.
'''
full_name = input("Enter full name: ").strip()
staff_number = input("Enter staff number: ").strip()
level = input("Enter level: ").strip()

if full_name == "":
    print("Error: Full name cannot be empty.")
elif not staff_number.isdigit():
    print("Error: Staff number must contain digits only.")
else:
    print("\n--- STAFF SUMMARY ---")
    print(f"Full Name    : {full_name.title()}")
    print(f"Staff Number : {staff_number}")
    print(f"Level        : {level.upper()}")
