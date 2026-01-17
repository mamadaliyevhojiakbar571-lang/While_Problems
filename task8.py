# While8. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lmagan eng katta butun k sonini
# (k2 <= n) aniglovchi programma tuzilsin. Ildizdan chigaruvchi funksiyadan foydalanmang.
n = int(input("n ni kiriting: "))
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print("Kvadrati n dan katta bo'lmagan eng katta butun k soni:", k)