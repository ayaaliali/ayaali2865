# الحصول على الرقم الثنائي من المستخدم
binary_str = input("Enter a binary number: ")

try:
    # التحويل من ثنائي إلى عشري
    decimal_number = int(binary_str, 2)
    print(f"The decimal equivalent of binary {binary_str} is {decimal_number}")
except ValueError:
    # التعامل مع الأخطاء إذا لم يكن الإدخال رقمًا ثنائيًا صحيحًا
    print("The input is not a valid binary number.")
