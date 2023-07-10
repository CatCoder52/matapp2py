
#input = np.loadtxt("1.txt", dtype='i', delimiter=',')
from numpy import loadtxt
lines = loadtxt("1.txt", delimiter=",", unpack=False)
lines = lines.replace(","," ")
data = open("1.txt", "r")
dataString = data.read()
print((lines))

#copy the data from the string into a list
dataList = dataString.split("\n")
#print(dataList)

#Cast all the list elements into floats
for i in range(0, len(dataList),1):
    dataList[i] = dataList[i].replace(","," ")
    dataList[i] = float(dataList[i])

