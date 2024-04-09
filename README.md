# ML-Project2
Microsoft Stock Price Prediction with Machine Learning
from datetime import datetime 
import tensorflow as tf 
from tensorflow import keras 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
import numpy as np 
import seaborn as sns 
microsoft = pd.read_csv('MicrosoftStock.csv') 
print(microsoft.head()) 
microsoft.shape
microsoft.info()
microsoft.describe()
plt.plot(microsoft['date'], 
		microsoft['open'], 
		color="blue", 
		label="open") 
plt.plot(microsoft['date'], 
		microsoft['close'], 
		color="green", 
		label="close") 
plt.title("Microsoft Open-Close Stock") 
plt.legend() 
plt.plot(microsoft['date'], 
		microsoft['volume']) 
plt.show()
sns.heatmap(microsoft.corr(), 
			annot=True, 
			cbar=False) 
plt.show() 
microsoft['date'] = pd.to_datetime(microsoft['date']) 
prediction = microsoft.loc[(microsoft['date'] 
							> datetime(2013, 1, 1)) 
							& (microsoft['date'] 
							< datetime(2018, 1, 1))] 

plt.figure(figsize=(10, 10)) 
plt.plot(microsoft['date'], microsoft['close']) 
plt.xlabel("Date") 
plt.ylabel("Close") 
plt.title("Microsoft Stock Prices") 


