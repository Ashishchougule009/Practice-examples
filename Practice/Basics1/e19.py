import cProfile

def fun():
    print(1+2)
cProfile.run('fun()')