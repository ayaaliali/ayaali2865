def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# الحصول على الرقم من المستخدم
num = int(input("Enter a number to calculate its factorial: "))

# التحقق من أن الرقم ليس سالبًا
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
