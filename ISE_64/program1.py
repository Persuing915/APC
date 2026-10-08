n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)

average = sum(marks) / n
maximum = max(marks)
minimum = min(marks)

above_average = 0

for m in marks:
    if m > average:
        above_average += 1

print("Maximum Marks:", maximum)
print("Minimum Marks:", minimum)
print("Average Marks:", average)
print("Students above Average:", above_average)