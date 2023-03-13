a = 0 
b = 0 

while True:
    n = int(input()) 
    if n == 0: 
        break 
    if n > a or n < a: 
        b += 1 
        a = n 
    else:
        b = 0 

print(b)