n = int(input("Enter a number: "))
i = 1
while n > 0:
    i *= n
    n -= 1
print(f"The factorial is {i}")
