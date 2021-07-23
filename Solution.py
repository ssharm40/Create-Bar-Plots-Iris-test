import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
#Write your code here

#task1
def test_barplot_of_iris_sepal_length():
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    ax.set(title="Mean Sepal Length of Iris Species",xlabel='Species',ylabel='Sepal Length (cm)', xlim=(0,3), ylim=(0,7))
    species=['setosa','versicolor','viriginica']
    index=[0.2, 1.2, 2.2]
    sepal_len=[5.01,5.94,6.59]
    ax.bar(index,sepal_len, width=0.5, color='red', edgecolor='black')
    plt.xticks([0.45,1.45,2.45])
    ax.set_xticklabels(['setosa','versicolor','viriginica'])
    plt.savefig("bar_iris_sepal.png")
    plt.show()
    
test_barplot_of_iris_sepal_length()


#task2
def test_barplot_of_iris_measurements():
    fig = plt.figure(figsize = (8,6))
    ax = fig.add_subplot(111)
    sepal_len = [5.01, 5.94, 6.59]
    sepal_wd = [3.42, 2.77, 2.97]
    petal_len = [1.46, 4.26, 5.55]
    petal_wd = [0.24, 1.33, 2.03]
    species = ['setosa', 'versicolor', 'viriginica']
    species_index1 = [0.7, 1.7, 2.7]
    species_index2 = [0.9, 1.9, 2.9]
    species_index3 = [1.1, 2.1, 3.1]
    species_index4 = [1.3, 2.3, 3.3]
    ax.set(title = "Mean Measurements of Iris Species",xlabel = "Specices",ylabel = "Iris Measurements (cm)",xlim = (0.5,3.7),ylim = (0,10))
    ax.bar(species_index1, sepal_len, color='c', width=0.2, edgecolor='black', label='Sepal Length')
    ax.bar(species_index2, sepal_wd, color='m', width=0.2, edgecolor='black', label='Sepal Width')
    ax.bar(species_index3, petal_len, color='y', width=0.2, edgecolor='black', label='Petal Length')
    ax.bar(species_index4, petal_wd, color='orange', width=0.2, edgecolor='black', label='Petal Width')
    ax.set_xticks([1.1,2.1,3.1])
    ax.set_xticklabels(['setosa', 'versicolor','viriginica'])
    ax.legend()
    plt.savefig("bar_iris_measure.png")
    
test_barplot_of_iris_measurements()



#Task3
def test_hbarplot_of_iris_petal_length():
    fig = plt.figure(figsize = (12,5))
    ax = fig.add_subplot(111)
    species = ['setosa', 'versicolor', 'viriginica']
    index = [0.2, 1.2, 2.2]
    petal_len = [1.46, 4.26, 5.55]
    ax.set(title = "Mean Petal Length of Iris Species",ylabel = "Species",xlabel = "Petal Length (cm)")
    ax.barh(index, petal_len, color='c', height = 0.5, edgecolor='black', label='Sepal Length')
    ax.set_yticks([0.45, 1.45,2.45])
    ax.set_yticklabels(['setosa', 'versicolor','viriginica'])
    
    plt.savefig("bar_iris_petal.png")


test_hbarplot_of_iris_petal_length()
