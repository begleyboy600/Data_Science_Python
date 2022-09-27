# NUMPY ARRAYS

# Numpy Arrays - Indexes
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3= np.array([9, 10, 11])

print(arr2[0][1])
print(arr2[0, 1])
print(arr1[1:3])

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr4[0:2, 1])

arr = np.concatenate((arr1, arr3))
print(arr)

# Creating & Shaping Numpy Objects
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = b.reshape(4, 3)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)    # axis=0 stacks vertically

arr = np.vstack((arr1, arr2))   # Stack vertically
arr = np.hstack((arr1, arr2))   # Stack horizontally
a = np.zeros((2, 5), dtype=np.float32)


###Numpy Arithmetic
a = np.array([3, 4, 5, 6])
b = 2 * a
b = a + 10
b = pow(a,0.5)
c = np.array([10, 11, 12, 13])
d = a+c


# Numpy Statistics – works on lists and numpy arrays
# Centrality & Dispersion - mean, median, std
a = np.array([3, 4, 5, 6])
b = np.mean(a)
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.mean(c, axis=0)
np.median(a), np.std(a), np.var(a)
e = np.array([1, 2, 3, float('nan')])
f = np.nanmean(e)

# Numpy - Correlation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 6, 7])
arr3 = np.array([7, 9, 14])
c = np.corrcoef((arr1, arr2))
d = np.corrcoef((arr1, arr2))[0, 1]
e = np.corrcoef((arr1, arr2, arr3))


# PANDAS DATAFRAMES AND SERIES

# Creating DataFrames
import pandas as pd
data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
purchases = pd.DataFrame(data)
# Change index names
# purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])


# Read in from csv and json files (Json considered as a dictionary)
# import os
# os.getcwd()
# os.chdir("C:\\Users\Playertek\Documents\DkIT\Data Science\Course2022\Week3-4DataMining")
netflix = pd.read_csv(r"C:\Users\mypc\Documents\College Work\Year 3\data science\NetflixData.csv")
#df = pd.read_json('purchases.json')

# Pandas – Getting information 1
netflix.info()
netflix.head()      # Shows first five rows
netflix.describe()
netflix.describe(include='all')


netflix['Status']
temp = netflix['Status'][0]


# Pandas – Getting information 1
x = pd.DataFrame([[1, 2, 3], [4, 5, 6]], ['row1', 'row2'], ['col1', 'col2', 'col3'])    # dataframe creation
x['col1']   # Column selection
# x['row1'] #Does not work for row selection
temp = x.col1     # columns selection
x.col1.row1     # Row selection after column selection

x['col4'] = x['col3'] + x['col2']       # Column Addition
x.columns = ['age1', 'age2', 'age3', 'age2_3']      # Column name changes
del x['col2']   # delete column
# x.drop('age2', axis=1, inplace=True)
x.index = ['r1', 'r2']     # rename rows(index)


temp = x.loc['row1']    # Works on rows
temp[0] = 3

x.iloc[1]   # select row
x.iloc[1, 2]    # select item
x.iloc[:, 1]    # select column
x = pd.DataFrame([[1, 2, 3], [4, 5, 6]], ['row1', 'row2'], ['col1', 'col2', 'col3'])    # dataframecreation

x.append(pd.DataFrame([[1, 2, 3]], columns=['col1', 'col2', 'col3']))   # Add rows



# Pandas - Selection
new = netflix['Seasons']
new1 = netflix[netflix.Seasons > 1]   # Drop certain rows based on column

new2 = netflix.drop(netflix[netflix.Seasons <= 1].index)    # drop certain rows based on column using index of roads
new3 = netflix[netflix.IMDB_Rating > 80]

new4 = netflix[['Title', 'IMDB_Rating']]


# Pandas – Statistical Functions
# count() Number of non-null observations
# sum() Sum of values
# mean() Mean of Values
# median() Median of Values
# mode() Mode of values
# std() Standard Deviation of the Values

new1['IMDB_Rating'].mean()
new3['IMDB_Rating'].count()
new1.mean()     # Will apply to any columns where makes sense to apply.
