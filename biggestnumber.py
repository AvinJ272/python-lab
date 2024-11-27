pi = 3.1416

num1 = int(input("enter the first number"))
num2 =int(input("enter the second number"))
num3 = int(input("enter the third number"))

if num1 >= num2 and num1>=num2:
    n = num3
elif num2 >= num1 and num2 >= num3:
    n = num2
else:
    n = num3

print(f"the largest number is :{n}")

nn =n**2
nnn = nn**3

result = n+nn+nnn
# print(f"n + nn + nnn = {n} + {nn} + {nnn}"  = {result}")
print(f"n + nn + nnn = {n} + {nn} + {nnn} = {result}")


radius =n

area = pi* radius **2
perimeter=2* pi * radius

print(f"\nFor a circle with radius {radius}:")
print(f"area = {area:2f}")
print(f"perimeter (circumference)={perimeter:.2f}")