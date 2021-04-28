a = ['a', 'b', 'c']
b = {'a', 'c', 'd'}
print(set(a))
print(set(a).union(b))
a.pop()
print(a)
print(set(a).union(b))


# while len(set(a).union(b)) > 3 :
#     print(a)
#     a.pop()