l = [2, 3, 4, 5, 6, 7, 8]
r = filter(lambda x: x % 2 != 0, l)
print(list(r))

t = ['a', 'b', 'c', 'd']
t.remove('b')
del t[0:2]
print(t)
