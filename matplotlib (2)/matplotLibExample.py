import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
#print(x1)


# create a plot figure
fig = plt.figure()

# subplot
#plt.subplot(2, 1, 1)
plt.plot(x1, np.sin(x1), 'o', color='orange') # plot(x-axis, y-axis, '-'/'.'/'ro')
#plt.xlabel('Time Series')
#plt.ylabel('-1 to +1')
plt.title('Sin wave and Cos wave structure for values '
          'in between 0 to 10')
#plt.subplot(2, 1, 2)
plt.plot(x1, np.cos(x1), '--')
# define axis of the graph
#plt.axis([1, 8, -1, 1])
plt.grid(True)
plt.show()

randValue = np.random.randn(10)
print(randValue)
plt.hist(randValue)
plt.show()

# toyota cars
years =[2019, 2020, 2021, 2022, 2023, 2024]
numberofcars = [10, 12, 4, 15, 20, 5]
error_min = [1, 0,1,2,1,0]
new_coming = [2,1,0,1,0,1]
error = [error_min, new_coming]
plt.bar(years, numberofcars, yerr=error)
plt.errorbar
plt.show()

# ABC car house
years =[2019, 2020, 2021, 2022, 2023, 2024]
toyota = [2,5,7,4,3,9]
nissan = [1,10,6,2,5,1]
ford = [0,2,7,8,7,12]

plt.bar(years, toyota, color = 'b')
plt.bar(years, nissan, color = 'r', bottom=toyota)
plt.bar(years, ford, color='y', bottom=nissan)
plt.show()

plt.figure(figsize=(10,10))
cars = [15,25,14,30]
labels = ['Toyota', 'Nissan', 'Ford', 'Honda']
plt.pie(cars, labels=labels)
plt.show()

from statistics import mean
age = [12,14,15,19]
print(mean(age)) # average

# read the file and load in pandas
import pandas as pd

df = pd.read_csv('insurance.csv') # to read the csv file in row and column structure
print(df.columns)
print(df['age'])

grouped_avg = df.groupby('age')['bmi'].mean()
x =grouped_avg.index
y = grouped_avg.values
plt.figure()
plt.plot(x, y, '-')
plt.show()
'''
ax =  fig.add_axes([0, 12, 0, 1.25])
ax.plot(x1, np.sin(x1), '-')
ax.plot(x1, np.cos(x1), '--')

ax.set_xlabel('X series data')
ax.set_ylabel('-1.0 to +1.0')
plt.show()
fig.savefig('sincos.png')

fig = plt.figure()


axes = fig.add_axes([0.2, 0.1, 0.6, 0.6])

axes.plot(x1, np.sin(x1), 'r')
axes.plot(x1, np.cos(x1), 'b')

axes.set_xlabel('x2')
axes.set_ylabel('y2')
axes.set_title('title')
plt.show()
fig.savefig('sincos2.png')
'''


#ax = plt.subplots(2)


# Call plot() method on the appropriate object
#ax[0].plot(x1, np.sin(x1), 'b-')
#ax[1].plot(x1, np.cos(x1), 'b-')
#plt.show()