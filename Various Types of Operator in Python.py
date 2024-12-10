a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
x = bool(int(input("Enter 1 or 0 for the first boolean value: ")))
y = bool(int(input("Enter 1 or 0 for the second boolean value: ")))
s = int(a)
e = int(b)

print("\nArithmetic Operators")
print("The sum is", a + b)
print("The difference is", a - b)
print("The multiplication is", a * b)
print("The division is", a / b)
print("The modulus is", a % b)
print("The power is", a ** b)

print("\nAssignment Operators")
c = a + b
print("Equal to:", c)
a += b
print("Plus equal to:", a)
a -= b
print("Difference equal to:", a)
a *= b
print("Multiply equal to:", a)
a /= b
print("Division equal to:", a)
a **= b
print("Power equal to:", a)
a %= b
print("Modulus equal to:", a)

print("\nConditional Operators")
print("a is equal to b:", a == b)
print("a is not equal to b:", a != b)
print("a is greater than b:", a > b)
print("a is less than b:", a < b)
print("a is greater than or equal to b:", a >= b)
print("a is less than or equal to b:", a <= b)

print("\nLogical Operators")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)

print("\nBitwise Operators")
print("AND:", s & e)
print("OR:", s| e)
print("XOR:", s ^ e)
print("NOT:", ~s)
print("Left shift:", s << 1)
print("Right shift:", s >> 1)
