import operator
import math
import subprocess
try:
    # from tabulate import tabulate
    subprocess.call(['pip install tabulate'])
except Exception as ex:
    print(ex)
    from tabulate import tabulate
# # ________________________________________________________
numOfcenters = int(input("Enter num of centers : "))
listOfCenters = []

for i in range(numOfcenters):
    listOfCenters.append((float(input("Enter x coordinates for center "+str(i+1)+" : ")),
                          float(input("Enter y coordinates for center "+str(i+1)+" : "))))
print(listOfCenters)
numOfPoints = int(input("Enter num of points : "))
listOfPoint = []
for i in range(numOfPoints):
    listOfPoint.append((float(input("Enter x coordinates for point "+str(i+1)+" : ")),
                        float(input("Enter y coordinates for point "+str(i+1)+" : "))))
# print(listOfPoint)
head = []
for i in range(len(listOfCenters)):
    for k in range(len(listOfPoint)):
        head.append("point "+str(k+1)+"- center "+str(i+1))
print()
print("listOfPoint")
print(tabulate(listOfPoint, headers="XY", tablefmt='fancy_grid'))
diffranceList = []
for point in listOfPoint:
    for center in listOfCenters:
        diffranceList.append(
            tuple(map(operator.pow, tuple(map(operator.sub, point, center)), (2, 2))))
print("squared difference between points and centers each " +
      str(int(numOfPoints/numOfcenters))+" observation for 1 point")
print(tabulate(diffranceList, headers="XY", tablefmt='fancy_grid'))
result = []
for i in diffranceList:
    result.append(math.sqrt(i[0]+i[1]))
# print(result)
print("square root for difference")
print(tabulate([result], headers=head,
               tablefmt='fancy_grid', floatfmt='.4f'))
dic = {}
list2 = []


for i in range(0, len(result), numOfcenters):
    list2.append(result[i:i+numOfcenters])
for i, j in zip(range(numOfPoints), list2):
    dic["point"+str(i+1)] = j
# print(list2)
# print(dic)
dic2 = {}
categ = {}
for pointNum, distanceList in dic.items():
    dic2[str(pointNum)] = str(distanceList.index(min(distanceList))+1)
    if 'center' + str(distanceList.index(min(distanceList))+1) not in categ:
        categ['center' +
              str(distanceList.index(min(distanceList))+1)] = [pointNum]

    else:
        categ['center' +
              str(distanceList.index(min(distanceList))+1)].append(pointNum)

print("Distance between every point and canters")
print(tabulate(dic.items(), headers=[
      "PointNo.", "Distacne-Respectivly"], tablefmt='fancy_grid'))
print("for which center the point below ?")
print(tabulate(dic2.items(), headers=[
      "PointNo.", "it's center"], tablefmt='fancy_grid'))

print("Every center contain what and how-many ?")
num = [len(v) for k, v in categ.items()]
print(tabulate(zip(categ.keys(), categ.values(), num), headers=[
      "centerNo.", "ListOfPoints", "How-many"], tablefmt='fancy_grid'))
final = []
for pair in listOfCenters:
    for center, total in categ.items():
        final.append((pair[0]/len(total), pair[1]/len(total)))
# print(final)
pointDic = {}
f = 1
for i in listOfPoint:
    pointDic['point'+str(f)] = i
    f = f+1
# print(pointDic)
dic77 = {}
for k, v in categ.items():
    xsum = 0
    for i in v:
        xsum = xsum + pointDic[i][0]
    dic77["newX"+k] = xsum/len(v)
    ysum = 0
    for i in v:
        ysum += pointDic[i][1]
    dic77["newY"+k] = ysum/len(v)
print("New Centers : ")
print(tabulate(dic77.items(), headers=[
      "coordinate", "value"], tablefmt='fancy_grid'))


# g = {'center1': [1, 2, 3],
#      'center2': [1, 2, 3],
#      'center3': [1, 2, 3]}
# num = [len(v) for k, v in g.items()]
# # for k, v in g.items():
# #     num.append(len(v))
# print(tabulate(zip(g.items(), num)))
# print(g)
# print((g.__sizeof__()))
# print(len(g.items()))
