#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:27:24 2019

@author: awanika
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv('/home/awanika/Downloads/iris.csv')

print(iris.shape)

print(iris.columns)

iris['species'].value_counts()
print("Iris is a balanced dataset as the number of data points for every class is same.")

#correlation
x = iris.corr()
print(x)

#kde plots
a = iris['sepal_length']
b = iris['sepal_width']
c = iris['petal_length']
d = iris['petal_width']
e = iris['species']

a.plot.kde()
b.plot.kde()
c.plot.kde()
d.plot.kde()

#SCATTERPLOT
#unicolor 
iris.plot(kind='scatter', x='sepal_length', y='sepal_width') ;
plt.show()

#color-coding
sns.set_style('whitegrid');
sns.FacetGrid(iris, hue='species', size=4).map(plt.scatter, 'sepal_length', 'sepal_width').add_legend();
plt.show();

print('blue dots are easily separable that corresponds to setosa')


#PAIR-PLOT
sns.set_style('whitegrid');
sns.pairplot(iris, hue='species', size=3);
plt.show()

print("petal_length ans petal_width give more clearity in the plots.")
print("setose is easily separable while virginica and versicolor have some overlap")

#1-D scatter plot
iris_setosa = iris.loc[iris['species'] == 'setosa'];
iris_virginica = iris.loc[iris['species'] == 'virginica'];
iris_versicolor = iris.loc[iris['species'] == 'versicolor'];


#distplots
sns.FacetGrid(iris, hue='species', size=5).map(sns.distplot, 'petal_length').add_legend();
plt.show();

sns.FacetGrid(iris, hue='species', size=5).map(sns.distplot, 'petal_width').add_legend();
plt.show();

sns.FacetGrid(iris, hue='species', size=5).map(sns.distplot, 'sepal_length').add_legend();
plt.show();

sns.FacetGrid(iris, hue='species', size=5).map(sns.distplot, 'petal_width').add_legend();
plt.show();


print("Setosa is easily separable as compared to others and sepal_ length is not a good feature")


#plotting pdf and cdf


#mean variance and stddev wrt petal_length and petal_width
print("Mean")
print(np.mean(iris_setosa['petal_length']))
print(np.mean(iris_virginica['petal_length']))
print(np.mean(iris_versicolor['petal_length']))

print(np.std(iris_setosa['petal_length']))
print(np.std(iris_virginica['petal_length']))
print(np.std(iris_versicolor['petal_length']))


print("from mean we see that setosa has less petal_length")

#median
print(np.median(iris_setosa['petal_length']))
print(np.median(iris_virginica['petal_length']))
print(np.median(iris_versicolor['petal_length']))

#boxplots
sns.boxplot(x='species',y='petal_length', data=iris)
plt.show()

#violin plots
sns.violinplot(x='species', y='petal_length', data=iris, size=8)
plt.show()














