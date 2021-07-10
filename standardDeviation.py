import math
import pandas
import csv

data = pandas.read_csv("C:/Users/Rishi/Downloads/Project 105/st.csv")

Number1 = data["Numbers"].tolist()
n = len(Number1)
sum = 0
for i in Number1:
    sum = sum + i

mean = sum/n
squarelist = []
for i in Number1:
    temp = i - mean
    temp = temp**2
    squarelist.append(temp)

sumsquare = 0
for i in squarelist:
    sumsquare = sumsquare + i

result = sumsquare/n
standarddeviation = math.sqrt(result)

print(standarddeviation)