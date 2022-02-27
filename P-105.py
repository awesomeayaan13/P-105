import csv
import pandas as pd
import plotly.express as px
import math
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data.pop(0)

def mean(data):
    total_marks=0
    total_entries=len(data)
    for marks in data:
        total_marks+=float(marks[1])
    mean=total_marks/total_entries
    
    return mean

squared_list=[]
for number in data:
    a=int(number) - mean(data)
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum=sum+i

result = sum/ (len(data)-1)
std_deviation=math.sqrt(result)
print(std_deviation)