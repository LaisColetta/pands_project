# Program that analyses Iris data set based on the tasks in the project. Analysis outside the scope of the mandatory tasks for this project are inside the jupyter notebook in this folder.
# Author: Lais Coletta


import numpy as np
#importing seaborn which is a library builded on matlotlib that helps to build plots with a nicer / more complex layouts
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#creating the variable 'df' for the data frame 'Iris_csv' and read the csv file using the read () function:
df = pd.read_csv('iris_csv.csv')

#First task: "Output a summary of each variable to a single text file"
#use function 'with open' as shown in lecture 'pands 7.1 files' to create and write on the file. wt is to open the txt file in a writing mode
with open ("summary.txt", 'wt') as f:
    #write a title and add space between data
    f.write ("Summary of each variable in Iris Data set \n\n")
    #write describe function which is a summary function in pandas
    f.write (str(df.describe()))
    #use the function value_counts to an overview of the data distribution between species
    f.write ("\n\n Data distribution \n\n")
    f.write (str(df.species.value_counts()))

#Second task: Saves a histogram of each variable to png files
#create a histogram that compares the attributes counts x sizes separated by species
plt.hist([df['sepal_length'], df['sepal_width'], df['petal_length'], df['petal_width']])
labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
plt.legend(labels)
plt.title('Comparison of features size')
plt.xlabel('Attributes in cm')
plt.ylabel('Count')
plt.savefig('Comparison of features size')

#create subplots for each attribute
#plt.subplots() is a function that returns a tuple containing a figure and axes objects, 'unpacking' this tuple into the variables fig and ax. (source: https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python )
#(2,2) in this function returns 4 graphs, 2 each cell
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
ax[0, 0].hist(df['sepal_length'])
ax[0, 0].set_title('Sepal Length')

ax[0, 1].hist(df['sepal_width'])
ax[0, 1].set_title('Sepal Width')

ax[1, 0].hist(df['petal_length'])
ax[1, 0].set_title('Petal Length')

ax[1, 1].hist(df['petal_width'])
ax[1, 1].set_title('Petal Width')
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
#create variable that loads iris data set from the online repository (requires internet)
iris = sns.load_dataset('iris')
#make the 'species' column categorical to fix the order
#'A categorical variable (sometimes called a nominal variable) is one that has two or more categories'. reference: https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.Categorical.html
iris['species'] = pd.Categorical(iris['species'])
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
#for loop through every column (0 to 4)
for col, ax in zip(iris.columns[:4], axs.flat):
    # seaborn histogram function. Hue determines which data we are selecting to be colored.
    sns.histplot(data=iris, x=col, hue='species', common_norm=False, legend=ax==axs[0,0], ax=ax)
#tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
plt.tight_layout()
plt.savefig('Histogram of each variable by species')

#Third task: Outputs a scatter plot of each pair of variables.
#create scatter plots of each pair of variables comparing sepal lenght and width
#to add space between title and graphe use variable y
plt.title('Comparison between species based on sepal length and width', y=1.06)
#s variable is to change dots size
sns.scatterplot(df['sepal_length'],df['sepal_width'],hue =df['species'],s=40)
ax = plt.subplot(111)
#shrinking plot width by 20% to fit legend box outside the axis of the figure (source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
#put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#save plot in png
plt.savefig('Scatter plot comparing sepal width vs leght')

#comparing petal lenght and width
plt.title('Comparison between species based on petal lenght and width', y=1.06)
sns.scatterplot(df['petal_length'], df['petal_width'], hue = df['species'], s= 40)
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('Scatter plot comparing petal width and lenght')