# While3. N va K butun musbat sonlari berilgan. Faqat ayirish va qo'shish amallarini ishlatib N sonini K
# soniga bo'lgandagi qoldiq va butun qismini aniqlovchi programma tuzilsin.
N = int(input("N ni kiriting: "))
K = int(input("K ni kiriting: "))
count = 0
while N >= K:
    N = N - K
    count += 1
print("N ni K ga bo'lgandagi butun qismi:", count)
print("N ni K ga bo'lgandagi qoldiq:", N)