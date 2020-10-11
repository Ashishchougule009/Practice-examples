
import cProfile

def mystr(str,n):
    result = ""
    if len(str)> 2:
        for i in range(n):
            result= result+str[:2]
        return result
    else:
        for i in range(n):
            result = result+str
        return result

print(mystr("asgssg",2))

print(mystr("s",3))

cProfile.run("mystr('ijjd',2)")