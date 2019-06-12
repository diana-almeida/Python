
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import xlwt
from xlwt import Workbook
import numpy as np
import re
import nltk
import seaborn as sns

# Workbook is created
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

#write path of the file where you have the information
path='C:/Users/admin/Desktop/TEST.csv'
data_source_url = path
test = pd.read_csv(data_source_url)
teststring=str(test)
#dividir por palabra
testlist=teststring.split()

i=0
for one in testlist:
    TextBlob(testlist[i]).sentiment.polarity
    if TextBlob(testlist[i]).sentiment.polarity > 0:
        x='positive'
    elif TextBlob(testlist[i]).sentiment.polarity == 0:
        x='neutral'
    else:
        x='negative'
    #print(x)
    sheet1.write(i, 0, x)
    sheet1.write(i, 1, testlist[i])
    i=i+1
wb.save('EXAMPLE.xls')

#convert excel to csv
data_xls = pd.read_excel('EXAMPLE.xls', 'Sheet 1', index_col=None)
data_xls.to_csv('EXAMPLE_csv.csv', encoding='utf-8')

#create pie chart
plot_size = plt.rcParams["figure.figsize"]
print(plot_size[0])
print(plot_size[1])

plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size

excel2 = pd.read_csv('C:/Users/admin/Desktop/EXAMPLE_csv.csv')
excel2.neutral.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=["red", "yellow", "green"])
#sns.barplot(x='neutral', y='neutral' , data=excel2)
plt.show()
