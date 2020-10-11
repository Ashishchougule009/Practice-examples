import multiprocessing
print(multiprocessing.cpu_count())

n= "2828.000023"
print(float(n))
print(int(float(n)))

from os import listdir
from os.path import isfile, join

filelist = [f for f in listdir("D:\\Python\\Githubuploads\\Geocoder\\uploads") if isfile(join("D:\\Python\\Githubuploads\\Geocoder\\uploads",f))]

print(filelist)