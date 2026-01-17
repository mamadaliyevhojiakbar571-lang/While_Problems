# While1. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada maksimal darajada B
# kesma joylashtirilgan. A kesmaning bo'sh qismini aniqlovchi programma tuzilsin. Ko'paytirish va bo'lish
# amallarini ishlatmang.
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
while A >= B:
    A = A - B
print("A kesmaning bo'sh qismi:", A)

