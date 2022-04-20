# Program that analyses the Iris date set
# Author; Lais Coletta


import numpy as np
#importing seaborn which is a library builded on matlotlib that helps to build plots with a nicer / more complex layouts
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#creating the variable 'df' for the data frame 'Iris_csv' and read the csv file using the read () function:
df = pd.read_csv('iris_csv.csv')

#Histograms
#histogram that compares the attributes counts x sizes separated by species
plt.hist([df['sepal_length'], df['sepal_width'], df['petal_length'], df['petal_width']])
labels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
plt.legend(labels)
plt.title('Comparison of features sizes')
plt.xlabel("Attributes in mm")
plt.ylabel("Count")
plt.savefig('Comparison of features sizes')

#create subplots for each attribute
#plt.subplots() is a function that returns a tuple containing a figure and axes objects, 'unpacking' this tuple into the variables fig and ax. (source: https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python )
#(2,2) in this function returns 4 graphs, 2 each row
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
ax[0, 0].hist(df['sepal_length'])
ax[0, 0].set_title('sepal_length')

ax[0, 1].hist(df['sepal_width'])
ax[0, 1].set_title('sepal_width')

ax[1, 0].hist(df['petal_length'])
ax[1, 0].set_title('petal_length')

ax[1, 1].hist(df['petal_width'])
ax[1, 1].set_title('petal_width')
#setting the spacing between subplots (reference: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.savefig('Histogram of each variable')

#create a more detailed version of the previous histogram subplots. Highlighting the species inside each attribute by color
#reference: https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris
#spicy.stats is a sub-package used for probability and statistical operations
from scipy.stats import norm
# create variable that loads iris data set from the online repository (requires internet)
iris = sns.load_dataset('iris')
#make the 'species' column categorical to fix the order
#'A categorical variable (sometimes called a nominal variable) is one that has two or more categories'. source: https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.Categorical.html
iris['species'] = pd.Categorical(iris['species'])

fig, axs = plt.subplots(2, 2, figsize=(12, 6))
#for loop through every column (0 to 4)
for col, ax in zip(iris.columns[:4], axs.flat):
    # seaborn histogram function. Hue determines which data we are selecting to be colored.
    sns.histplot(data=iris, x=col, hue='species', common_norm=False, legend=ax==axs[0,0], ax=ax)
#tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
plt.tight_layout()
plt.savefig('Histogram of each variable by species')

#scatter plots
#create scatter plots of each pair of variables
Iris = sns.load_dataset('iris')

#comparing sepal lenght and width
plt.title('Comparison between species based on sepal length and width', y=1.06)
sns.scatterplot(df['sepal_length'],df['sepal_width'],hue =df['species'],s=50)
ax = plt.subplot(111)
# Shrinking plot width by 20% to fit legend box outside the axis of the figure (source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('Scatter plot comparing sepal width vs leght')

#comparing petal lenght and width
plt.title('Comparison between species based on petal lenght and width', y=1.06)
sns.scatterplot(df['petal_length'], df['petal_width'], hue = df['species'], s= 50)
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('Scatter plot comparing petal width and lenght')

