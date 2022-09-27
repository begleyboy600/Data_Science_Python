import numpy as np
import pandas as pd
from scipy import stats
from tabulate import tabulate

print("-- PART 5 --")
# PART 1
print("-- Q1 --")
# Q1
nump1 = np.array([2.3, 3.8, 4.6, 5.8, 6.2])
print(nump1)

print("-- Q2 --")
# Q2
nump2 = np.array([6.3, 8.8, 7.6, 8.8, 10.2])
print(nump2)

print("-- Q3 --")
# Q3
nump1_plus_ten = nump1 + 10
print(nump1_plus_ten)

print("-- Q4 --")
# Q4
nump1_multiply_six = nump1 * 6
print(nump1_multiply_six)

print("-- Q5 --")
# Q5
nump3 = np.concatenate([nump1, nump2])
print(nump3)

print("-- Q6 --")
# Q6
mean_of_nump1 = np.mean(nump1)
median_of_nump1 = np.median(nump1)
mode_of_nump1 = stats.mode(nump1)
std_of_nump1 = np.std(nump1)
print("nump1:")
print("mean:", mean_of_nump1, "\n median: ", median_of_nump1, "\n mode: ", mode_of_nump1, "\n std: ", std_of_nump1)

mean_of_nump2 = np.mean(nump2)
median_of_nump2 = np.median(nump2)
mode_of_nump2 = stats.mode(nump2)
std_of_nump2 = np.std(nump2)
print("nump2:")
print("mean:", mean_of_nump2, "\n median: ", median_of_nump2, "\n mode: ", mode_of_nump2, "\n std: ", std_of_nump2)

print("-- Q7 --")
# Q7
correlation = np.corrcoef((nump1, nump2))[0, 1]
print("correlation: ", correlation)     # strongly positive correlation between the 2 arrays

print("-- Q8 --")
# Q8
nump4 = np.random.randint(0, 51, (6, 8))
print(nump4)

print("-- PART 6 --")
# PART 6
print("-- PART A --")
# PART A
print("-- Q1 --")
# Q1
list = [7, 11, 13, 17]
pd_series = pd.Series(list)
print(pd_series)

print("-- Q2 --")
# Q2
pd_series2 = pd.Series(100.0, index=range(1, 6))
print(pd_series2)

print("-- Q3 --")
# Q3
pd_series3 = pd.Series(np.random.randint((100), size=(20)))
# print(pd_series3.head())
print(pd_series3.describe())

print("-- Q4 --")
# Q4
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures.head())

print("-- Q5 --")
# Q5
dictionary_temperatures = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
temperatures_series = pd.Series(dictionary_temperatures)
print(temperatures_series.head())

print("-- PART B --")
# PART B
print("-- Q1 --")
# Q1
temps = {
    'Maxine': [98.6, 96.9, 97.7],
    'James': [98.9, 100.3, 101.1],
    'Amanda': [98.5, 98.3, 98.7]
}
temperatures_df = pd.DataFrame(temps)
print(temperatures_df.head())

print("-- Q2 --")
# Q2
new_temperatures_df = temperatures_df.rename(index={0: 'Morning', 1: 'Afternoon', 2: 'Evening'})
print(new_temperatures_df)

print("-- Q3 --")
# Q3
print(new_temperatures_df[['Maxine']])

print("-- Q4 --")
# Q4
print(new_temperatures_df.loc[['Morning', 'Evening']])

print("-- Q5 --")
# Q5
print(new_temperatures_df[['Maxine', 'Amanda']])

print("-- Q6 --")
# Q6
print(new_temperatures_df[['Maxine', 'Amanda']].loc[['Morning', 'Afternoon']])

print("-- Q7 --")
# Q7
print(new_temperatures_df.describe(include='all'))

print("-- Q8 --")
# Q8
transposed_dataframe = new_temperatures_df.transpose()
print(transposed_dataframe)

print("-- Q9 --")
# Q9
alphabetic_temperature_dataframe = new_temperatures_df.reindex(sorted(new_temperatures_df.columns), axis=1)
print(alphabetic_temperature_dataframe)

print("-- Q10 --")
# Q10
# method 1
print("temperature value in 2nd row in the 3rd column: ", new_temperatures_df.iloc[1, 2])

# method 2
print("temperature value in 2nd row in the 3rd column: ", new_temperatures_df.iat[1, 2])



