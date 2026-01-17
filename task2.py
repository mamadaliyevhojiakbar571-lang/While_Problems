# While2. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada B kesmadan nechta
# joylashtirish mumkinligini aniqlovchi programma tuzilsin. Ko'paytirish va bo'lish amallarini ishlatmang.
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
count = 0
while A >= B:
    A = A - B
    count += 1
print("B kesmadan joylashtirilgan soni:", count)