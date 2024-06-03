import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import radviz

class train_by_set:
    def __init__(self, feature):
        self.feature = feature
        self.df = pd.read_csv('train.csv')
        dataset = pd.DataFrame(pd.DataFrame.to_numpy(self.df), columns=["petallength","petalwidth","class"])
        self.data_setosa = dataset[dataset["class"] == "Iris-setosa"].sort_values(self.feature)
        self.data_versicolor = dataset[dataset["class"] == "Iris-versicolor"].sort_values(self.feature)
        self.data_virginica = dataset[dataset["class"] == "Iris-virginica"].sort_values(self.feature)

    """
    the first element is the minimum
    """
    def get_setosa_range_values(self):
         return self.data_setosa.iloc[0, :][self.feature], self.data_setosa.iloc[-1, :][self.feature]

    def get_versicolor_range_values(self):
         return self.data_versicolor.iloc[0, :][self.feature], self.data_versicolor.iloc[-1, :][self.feature]

    def get_virginica_range_values(self):
         return self.data_virginica.iloc[0, :][self.feature], self.data_virginica.iloc[-1, :][self.feature]

    def get_threshold(self):
        setosa = self.get_setosa_range_values()
        versicolor = self.get_versicolor_range_values()
        virginica = self.get_virginica_range_values()
        flowers_values = []
        flowers_values.append(setosa[1])
        flowers_values.append(versicolor[0])
        flowers_values.append(versicolor[1])
        flowers_values.append(virginica[0])

        thresholds = []
        print (flowers_values)
        for i in range(0, len(flowers_values)-1, 2):
             _max = flowers_values[i]
             _min_2 = flowers_values[i+1]
             thresholds.append(_max + math.sqrt((_max - _min_2)**2) / 2)
        return thresholds


