# While5. 2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan (n > 0). n = 2k
# . k ni aniqlovchi
# programma tuzilsin.
n = int(input("n ni kiriting: "))
k = 0
temp = 1
while temp < n:
    temp = temp * 2
    k += 1  
print("k ning qiymati:", k)