# Program that analyses the Iris date set
# Author; Lais Coletta

import numpy as np
#importing seaborn which is a library builded on matlotlib that helps to build plots with a nicer / more complex layouts
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_csv.csv')

#The first plot is a histogram that compares the attributes sizes
plt.hist([df['sepal_length'], df['sepal_width'], df['petal_length'], df['petal_width']])
labels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
plt.legend(labels)
plt.title('Comparison of features sizes')
plt.xlabel("Features in mm")
plt.ylabel("Count")
plt.show
plt.savefig('Comparison of features sizes')

#Creating subplots for each attribute
#plt.subplots() is a function that returns a tuple containing a figure and axes objects, 'unpacking' this tuple into the variables fig and ax. (source: https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python )
# (2,2) - returns 4 graphs, 2 each row
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
ax[0, 0].hist(df['sepal_length'])
ax[0, 0].set_title('sepal_length')

ax[0, 1].hist(df['sepal_width'])
ax[0, 1].set_title('sepal_width')

ax[1, 0].hist(df['petal_length'])
ax[1, 0].set_title('petal_length')

ax[1, 1].hist(df['petal_width'])
ax[1, 1].set_title('petal_width')

# setting the spacing between subplots (reference: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()
plt.savefig('Histogram of each variable')

#Creating subplots for each species
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
ax[0, 0].hist(df['Iris_'])
ax[0, 0].set_title('sepal_length')

ax[0, 1].hist(df['sepal_width'])
ax[0, 1].set_title('sepal_width')

ax[1, 0].hist(df['petal_length'])
ax[1, 0].set_title('petal_length')

ax[1, 1].hist(df['petal_width'])
ax[1, 1].set_title('petal_width')
