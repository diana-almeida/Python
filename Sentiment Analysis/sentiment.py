
from textblob import TextBlob
import pandas as pd

#write path of the file where you have the information
path='TEST.csv'

#make csv readable
data = pd.read_csv(path)

# convert pandas to string
data1=str(data)

#print the polarity
print(TextBlob(data1).sentiment.polarity)

#print if negative, positive or neutral
if TextBlob(data1).sentiment.polarity > 0:
    print('positive')
elif TextBlob(data1).sentiment.polarity == 0:
    print('neutral')
else:
    print('negative')
