# Pandas Project  
**Author:** Lais Coletta  

## Overview

This project explores the **Iris flower dataset**, a well-known dataset introduced by British statistician and biologist Ronald Fisher in 1936. The dataset contains 150 samples from three species of Iris flowers: **Iris setosa**, **Iris virginica**, and **Iris versicolor**. For each flower, four features were measured: the length and width of the sepal and petal (in centimeters). Fisher used this dataset to develop a linear discriminant model for distinguishing between the species based on these features.

The Iris dataset is widely used in Data Science and Machine Learning, often as an introductory dataset for classification problems. It consists of 150 records and five attributes: **Sepal length**, **Sepal width**, **Petal length**, **Petal width**, and **Species**.

For further reading:  
[Wikipedia - Iris Flower Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set#:~:text=The%20Iris%20flower%20data%20set,example%20of%20linear%20discriminant%20analysis.)

![Iris Flower](https://upload.wikimedia.org/wikipedia/commons/0/0e/Iris_versicolor_3.jpg)

## Project Development

The project was built based on Google research and knowledge gained in the course, particularly during Week 08 when we focused on plotting techniques. All references used in this project are included as comments in the `analysis.py` file and/or directly referenced within the Jupyter notebook `analysis.ipynb`. Any sections of the project copied from external sources are marked in *italic* with corresponding references.

### Tools and Resources Used
- **Pandas**: For data manipulation and analysis.
- **Matplotlib** & **Seaborn**: For data visualization and plotting.
- **Jupyter Notebook**: For organizing and presenting the analysis.
  
Tutorials:
- [Pandas - Keith Galli](https://www.youtube.com/watch?v=vmEHCJofslg&ab_channel=KeithGalli)
- [Jupyter Notebook - Corey Schafer](https://www.youtube.com/watch?v=HW29067qVWk&ab_channel=CoreySchafer)
- [Python Data Analysis with Iris Dataset | Data Science, Plotting & Graphing](https://www.youtube.com/watch?v=qgdhvPsbRHw)

### Key Insights
The Iris dataset's popularity in machine learning arises from its small size, ease of use, and its suitability for testing classification and pattern recognition methods. One of the key reasons it's so well-suited for classification tasks is that one of the species (Iris setosa) is linearly separable from the other two species in the dataset.

## How to Run the Code

### Clone the repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/LaisColetta/pandas_project.git
```
### Install the necessary libraries
Make sure all required libraries are installed by running the following:

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook
To open the project, start Jupyter Notebook:
```bash
jupyter notebook
```
This will open the Jupyter dashboard in your browser. Navigate to the analysis.ipynb file and open it.

### Run the cells
Inside the notebook, run the cells sequentially to perform the analysis. The output will include visualizations, statistical analysis, and model performance metrics.

## User Manual
This project does not include a user interface, as it is implemented in Jupyter Notebook, but you can follow these instructions to analyze the dataset and run the code:

- Open the `analysis.ipynb` notebook in Jupyter.
- The first few cells provide an overview of the dataset and its variables.
- Follow the steps in the cells to explore the correlation between the input variables (sepal and petal dimensions) and the output (species).
- Review the plots and the statistical analysis results in the subsequent cells.
- Interpret the conclusions and insights at the end of the notebook.




