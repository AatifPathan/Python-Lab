class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
calc = Calculator()
result1 = calc.add(5)
result2 = calc.add(5, 10)
result3 = calc.add(5, 10, 15)

print("Addition of 5:", result1)
print("Addition of 5 and 10:", result2)
print("Addition of 5, 10, and 15:", result3)
