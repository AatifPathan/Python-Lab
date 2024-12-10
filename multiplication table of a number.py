n = int(input("Enter the number to generate its multiplication table: "))
print("Multiplication table:")
for i in range(1, 13):  
    if i == 6:
        continue
    if i==12:
       break
    print(f"{n} x {i} = {n * i}")

