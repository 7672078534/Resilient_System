
#importing libraries:
import numpy 
import pandas 
import matplotlib.pyplot
import seaborn
import warnings
warnings.filterwarnings('ignore')
#importing dataset:
Dataset=pandas.read_csv(r"C:\Users\venka\Downloads\cybersecurity_attacks.csv")
Dataset.head()
# DATA PREPROCESSING:
Dataset.info()
Dataset.shape
Dataset.describe()
Dataset.nunique()
Dataset['Log Source'].unique()
# DATA CLEANING:
Dataset.isnull().sum()
Dataset.duplicated().sum()
Dataset.fillna(numpy.mean,inplace=True)
Dataset.isnull().sum()
Dataset['Log Source'].value_counts()
# EDA(EXPLORATORY DATA ANALYSIS)
matplotlib.pyplot.figure(figsize=(15,6))
seaborn.countplot(x='Log Source',data=Dataset,palette='Set1')
matplotlib.pyplot.xticks(rotation = 0)
matplotlib.pyplot.show()
# Result:
matplotlib.pyplot.figure(figsize=(15,6))
seaborn.countplot(x='Protocol',data=Dataset,palette='Set1')
matplotlib.pyplot.xticks(rotation = 0)
matplotlib.pyplot.show()
# Result:
matplotlib.pyplot.figure(figsize=(15,6))
seaborn.countplot(x='Packet Type',data=Dataset,palette='Set1')
matplotlib.pyplot.xticks(rotation = 0)
matplotlib.pyplot.show()
# Result:
matplotlib.pyplot.figure(figsize=(15,6))
seaborn.countplot(x='Attack Type',data=Dataset,palette='Set1')
matplotlib.pyplot.xticks(rotation = 0)
matplotlib.pyplot.show()
matplotlib.pyplot.figure(figsize=(15,6))
seaborn.countplot(x='Traffic Type',data=Dataset,palette='Set1')
matplotlib.pyplot.xticks(rotation = 0)
matplotlib.pyplot.show()
# Gender gap in internet usage by area
matplotlib.pyplot.figure(figsize=(10, 5))
seaborn.barplot(data=Dataset, x='Packet Length', y='Packet Type', ci=None, palette='viridis')
matplotlib.pyplot.title('Bar plot between the packet type and length')
matplotlib.pyplot.xlabel('packet length')
matplotlib.pyplot.ylabel('packet type')
matplotlib.pyplot.show()
matplotlib.pyplot.show()
