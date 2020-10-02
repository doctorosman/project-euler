fibonacci = [1, 2]

while True:
    n = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    
    if n < 4000000:
        fibonacci.append(n)
    else:
        break

total = 0

for i in fibonacci:
    if i % 2 == 0:
        total += i

print(total)