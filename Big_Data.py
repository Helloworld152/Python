import numpy as np
import pandas as pd

# data = np.array([[1.9526, -0.246, -0.8856], [0.5639, 0.2379, 0.9104]])
# print(data)


# data1 = [11, 23, 23]
# index = ['a', 'b', 'c']
# s = pd.Series(data1, index=index)
# print(s)
# print(s['a'], s['b'], s['c'])


# data = {'name':['Joe', 'Cat', 'Mike', 'Kim', 'Amy'],
#         'year':[2012, 2012, 2013, 2014, 2014],
#         'Points':[4, 24, 31, 2, 3]}
# df = pd.DataFrame(data, index = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
# print(df)


# CountryList = ['Iraq', 'China', 'USA', 'China', 'USA', 'Iraq', 'USA', 'USA']
# CityList = ['Baghdad', 'Beijing', 'New York', 'Hong Kong', 'Los Angeles', 'Karbala', 'Chicago', 'Seattle']
# RainNumpyArray = np.array([2.24, 25, 47.2, 87, 15, 3.5, 34, 40])
# df = pd.DataFrame({'City':CityList, 'Country':CountryList, 'RainFall':RainNumpyArray})
#
# print(df.head(8))
# print(df.groupby(['Country'], as_index=False).mean())


# data = np.array([[1, 2, 2, 2, 4, 5, 2],
#                  [3, 3, 3, 3, 3, 6, 6]])
# print(data)
# print(data.shape)
# print(data*2 + 4)
# print(data*data)
# data1 = np.array([0,1,2,3,4,5,6,7,8,9])
# print(data1[5:8])
# print(data1 > 3)
# print(np.sqrt(data1))


data = pd.read_csv("Population_database.csv")
print(data.head(10))
print(data.describe())