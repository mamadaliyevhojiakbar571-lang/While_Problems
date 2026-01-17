# While9. n natural soni berilgan (n > 1). 3k > n shartni qanoatlantiruvchi eng kichik butun k sonini
# aniqlovchi programma tuzilsin.
n = int(input("n ni kiriting: "))
k = 1
temp = 3  

while temp <= n:
    temp *= 3
    k += 1

print("Eng kichik k:", k)