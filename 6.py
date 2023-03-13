a = 1
count = 1
n = int(input())

for i in range(n, 0, -1):   
    a *= i
    count += a
    
count = count / a
print(count)