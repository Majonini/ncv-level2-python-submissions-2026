
menu = "Press 1: Capturing marks\n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: To calculate average of marks\n"
menu += "Press 4: To find highest marks\n"
menu += "Press -1: To exit"


# Array (list) to store marks
marks = []


# Function to capture marks
def capture_marks():
    mark = float(input("Enter mark (-1 to stop capturing): "))

    while mark != -1:
        if 0 <= mark <= 100:
            marks.append(mark)
            print("Mark captured successfully.")
        else:
            print("Invalid mark. Enter a mark from 0 to 100.")

        mark = float(input("Enter mark (-1 to stop capturing): "))


# Function to count marks
def count_marks():
    print("Number of marks:", len(marks))


# Function to calculate average
def calculate_average():
    if len(marks) > 0:
        average = sum(marks) / len(marks)
        print(f"Average mark: {average:.2f}")
    else:
        print("No marks captured.")


# Function to find highest mark
def highest_mark():
    if len(marks) > 0:
        print("Highest mark:", max(marks))
    else:
        print("No marks captured.")


# Main program
choice = 0

while choice != -1:
    print("\n", menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        capture_marks()
    elif choice == 2:
        count_marks()
    elif choice == 3:
        calculate_average()
    elif choice == 4:
        highest_mark()
    elif choice == -1:
        print("Program terminated.")
    else:
        print("Invalid menu choice. Try again.")
