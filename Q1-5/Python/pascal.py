n = int(input("Enter the number of rows: "))
tri = []

for i in range(1, n+1):
    if n <= 0:
        print()
        exit(0)

    if i == 1:
        tri.append([1])
        continue
    prev = tri[i - 2]
    next = []
    for k in range(len(prev) + 1):
        if (k == 0) or (k == len(prev)):
            next.append(1)
        else:
            next.append(prev[k-1] + prev[k])
    tri.append(next)
for row in tri:
    for n in row:
        print(n, end='  ')
    print()