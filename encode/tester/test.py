def mymap(func, *seqs):
    print(seqs)


dic = {"a", "b", "c"}
map(lambda x: print(x), dic)

mymap(None, 1, 2, 3)
