n = int(input())

maxint = n
count = 1

while n != 0: 
    n = int(input())
    if n == maxint: 
        count += 1
    elif n > maxint: 
        maxint = n 
        count = 1
        
print(count) 