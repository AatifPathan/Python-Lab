a = int(input("Enter the total number of subjects: "))
b = int(input("Enter the total marks of all the subjects: "))
c = int(input("Enter the maximum marks of a subject: "))
avg = b / a
per = (b /c) * 100
print("The Average is",avg)
if per >= 90:
    print("The Grade is A")
elif per >= 80 and per < 90:
    print("The Grade is B")
elif per >= 70 and per < 80:
    print("The Grade is C")
elif per >= 60 and per < 70:
    print("The Grade is D")
else:
    print("Fail")
