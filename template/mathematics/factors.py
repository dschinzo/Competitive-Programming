n = int(input())
facts = [1, n]
i = 2
while i < n ** 0.5:
    if n % i == 0:
        facts.append(i)
        facts.append(n//i)
    i += 1
if i**2 == n:
    facts.append(i)
facts.sort()
print(facts)