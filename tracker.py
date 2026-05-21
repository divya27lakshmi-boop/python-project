students = []
attendance = []

n = int(input("Enter number of students: "))


for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    students.append(name)

    status = input("Enter attendance (P for Present / A for Absent): ").upper()
    attendance.append(status)

print("\n===== Attendance Report =====")

for i in range(n):
    if attendance[i] == "P":
        print(students[i], "- Present")
    else:
        print(students[i], "- Absent")
