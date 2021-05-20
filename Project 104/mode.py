import csv
from collections import Counter
with open("file.csv",newline="") as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
newdata =[]
for i in range (len(data)):
    num=data[i][2]
    newdata.append(float(num))

count=Counter(newdata)
moderange = {
    "50-60":0,
    "60-70":0,
    "70-80":0   
}

for height,occurence in count.items():
    if 50<float(height)<60:
        moderange["50-60"]+=occurence
    elif 60<float(height)<70:
        moderange["60-70"]+=occurence
    elif 70<float(height)<80:
        moderange["70-80"]+=occurence

modedata,modeoccurence=0,0
for range,occurence in moderange.items():
    if occurence > modeoccurence:
        modedata,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((modedata[0]+modedata[1])/2)

print("mode of height = "+ str(mode))