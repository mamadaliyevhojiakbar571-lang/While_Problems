# While7. n natural soni berilgan (n > 0). Kvadrati n dan katta bo'ladigan eng kichik butun k sonini (k2 > n)
# aniqlovchi programma tuzilsin. Ildizdan chiqaruvchi funksiyadan foydalanmang.
n = int(input("n ni kiriting: "))
k = 1
while k * k <= n:
    k += 1
print("Kvadrati n dan katta bo'ladigan eng kichik butun k soni:", k)