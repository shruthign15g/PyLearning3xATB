set1 = set(["Hello World", "Good Morning", "Hello World."])
print(len(set1))

for i in set1:
    print(i)

set1 = set([1,2,3,4,0,9,7,6,8])
print(set1)
print(max(set1))
print(min(set1))
print(sum(set1))
print(sorted(set1))
print(sorted(set1, reverse=True))
set1.add(5)
print(set1)
set1.pop()
print(set1)