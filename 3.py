count = 0
num = 0

while True:
    
    n = int(input())

    if n == 0:
        print(num / count)
    else:
        count += 1
        num += n