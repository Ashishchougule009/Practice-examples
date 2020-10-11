def myfun(list,n):
    if n in list:
        return True
        
    else:
        return False

list = [1,5,3,8]
print(myfun(list,3))
print(myfun(list,-1))