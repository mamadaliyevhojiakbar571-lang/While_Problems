# While6. n natural soni berilgan (n > 0). Quyidagi ifodani hisoblovchi programma tuzilsin:
# n!! = n * (n - 2) * (n-4) ...
# Agar n juft bo'lsa oxirgi ko'payuvchi 2, toq bo'lsa 1 bo'ladi.
n = int(input("n ni kiriting: "))
result = 1
while n >= 1:
    result = result * n
    n = n - 2
print("n!! ning qiymati:", result)