s1=float(input("Enter the Maths mark"))
s2=float(input("Enter the AI mark"))
s3=float(input("Enter the DAA mark"))
s4=float(input("Enter the CN mark"))
s5=float(input("Enter the DBMS mark"))
print("Maths mark is",s1)
print("AI mark is",s2)
print("DAA mark is",s3)
print("CN mark is",s4)
print("DBMS mark is",s5)
print(" MARKSHEET")
Total=s1+s2+s3+s4+s5
average=Total/5
if s1>=50 and s2>=50 and s3>=50 and s4>=50 and s5>=50:
    Result="PASS"
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"
else:
    Result="FAIL"
    Grade="No Grade"
print("Result:",Total)
print("Grade:",grade)
