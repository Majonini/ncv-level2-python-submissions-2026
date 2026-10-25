# marks = [62,75,48,91,70]
# 
# print("First:",marks[0])
# print("Third:",marks[3])
# print("Number of marks:",len(marks))

marks = []
mark = int(input("Enter marks(or -1 to stop)"))
while mark != -1:
    marks.append(mark)

    mark = int(input("Enter marks(or -1 to stop)"))
    
print(f"Our list has {len(marks)}: elements")

def printt_list_size(marks):
    print(f"Our list has {len(marks)}: elements")

def 

sum=0
for x in range(len(marks)):
    print(marks[x])

sum = sum + mark

print(f"the sum of all marks = {sum}")

def get_avg_of_marks():
    total = 0
    for x in range(len(marks)):
        mark = marks[x]
        total = total + mark
        avg = total / len(marks)
    print(f"the average of all marks = {avg}")

def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_marks = marks[i]
        if (current_mark > highest):
            highest = current_mark
    print(f"The highest mark is {highest}")

menu = "Press 1: Capturing marks\n"
menu +="Press 2: Check number of marks\n" 
menu +="Press 3: To calculate average of marks\n" 
menu +="Press 4: To find highest marks\n" 
menu +="Press -1: To exit"

print(menu)
choice = int(input(": Make your Choice"))

entered_marks = []
if choice ==1:
    entered_marks = getMarks()


