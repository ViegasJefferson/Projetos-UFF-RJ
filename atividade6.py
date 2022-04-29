a = input()
b = []
[b.append(x) for x in [[int(n) for _ in range(1, a.count(n) + 1)] for n in a.split()] if not x in b]

print(b)