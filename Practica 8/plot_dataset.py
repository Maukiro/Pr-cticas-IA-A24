import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from train import train_by_set

def classify(feature, lines_ths):
	if feature == "petallength":
		print(lines_ths)
		for i in lines_ths:
			plt.axvline(i)
	if feature == "petalwidth":
		print(lines_ths)
		for i in lines_ths:
			plt.axhline(i)

def plot_data(file, feature, lines_ths):
	df = pd.read_csv(file, header=None)
	dataset = pd.DataFrame(pd.DataFrame.to_numpy(df), columns=["petal_length","petal_width","species"])
	
	_data_petal_length = dataset['petal_length'][1:].astype(float)
	_data_petal_width = dataset['petal_width'][1:].astype(float)

	plt.scatter(_data_petal_length, _data_petal_width, c=pd.factorize(dataset['species'][1:])[0])

	classify(feature, lines_ths)

	plt.xlabel('Sepal Length (cm)')
	plt.ylabel('Sepal Width (cm)')
	plt.title('Sepal Length vs Sepal Width')
	plt.legend()
	plt.grid(True)

	plt.show()

if __name__ == '__main__':
	train_by_petalllength = train_by_set("petallength")
	lines_ths = train_by_petalllength.get_threshold()

	plot_data("./train.csv", 'petallength', lines_ths)
	plot_data("./test.csv", 'petallength', lines_ths)

	train_by_petalllength = train_by_set("petalwidth")
	lines_ths = train_by_petalllength.get_threshold()
	
	plot_data("./train.csv", 'petalwidth', lines_ths)
	plot_data("./test.csv", 'petalwidth', lines_ths)
