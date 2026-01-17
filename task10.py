#   While10. n natural soni berilgan (n > 1). 3k <= n shartni qanoatlantiruvchi eng katta butun k sonini
# aniqlovchi programma tuzilsin.
n = int(input("n ni kiriting: "))
k = 0
temp = 1    
while temp * 3 <= n:
    temp *= 3
    k += 1
print("Eng katta k:", k)