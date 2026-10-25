# marks = [62,75,48,91,70]
# 
# print("First:",marks[0])
# print("Third:",marks[3])
# print("Number of marks:",len(marks))

marks = []
#i = 0
# marks[i] = marks
mark = int(input("Enter marks(or -1 to stop)"))
while mark != -1:
    marks.append(mark)
#     marks[i] = marks
#     i += 1
    mark = int(input("Enter marks(or -1 to stop)"))
    
print(f"Our list has {len(marks)}: elements")
sum=0
for x in range(len(marks)):
    print(marks[x])

sum = sum + mark

print(f"the sum of all marks = {sum}")

total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark
    avg = total / len(marks)
print(f"the average of all marks = {avg}")

