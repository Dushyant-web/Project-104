import csv
with open("file.csv",newline="") as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
newdata =[]
for i in range (len(data)):
    num=data[i][2]
    newdata.append(float(num))

n =len(newdata)
total=0
for x in newdata:
    total=total+x
mean=total/n
print("mean of weight = "+ str (mean))