def myfun(list):
    for n in list:
        output = ""
        times = n
        while times>0:
            output = output+"*"
            times= times-1
        print(output)
    
print(myfun([2,3,5,3,1]))