# While4. n butun soni berilgan (n > 0). Agar n soni 3 ning darajasi bo'lsa "3 - ning darajasi",
# ", aks xolda "3
# - ning darajasi emas" degan natija chiqaruvchi programma tuzilsin. Qoldiqli bo'lish va bo'lish amallarini
# ishlatmang.
n = int(input("n ni kiriting: "))
temp = n

while temp >= 3:
    temp /= 3

if temp == 1:
    print("3 - ning darajasi")
else:
    print("3 - ning darajasi emas")