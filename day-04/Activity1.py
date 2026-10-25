
mark = float(input("Enter mark (0 to 100): "))

if mark < 0 or mark > 100 and mark is not =="":
    classification = "Invalid mark"
elif mark >= 0 and mark < 40:
    classification = f'{mark} Not achieved'
elif mark >= 40 and mark < 50:
    classification = "Not yet competent"
elif mark >= 50 and mark < 70:
    classification = "Competent"
elif mark >= 70 and mark < 80:
    classification = "Highly competent"
else:
    classification = "Outstanding"

print("Mark: ", mark)
print("Classification: ", classification)
