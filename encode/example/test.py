def ans(n, a, b, f):
    print("%s says %d" % (n, f(a, b)))


def ah(a, b):
    return a + b


ans("jfox", 1, 5, ah)
