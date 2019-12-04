import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import glob
	
def save_data(file_name, i):
	cols = [2,3,5,6,10,11,12,13]
	Y_cols = [10]
	data = pd.read_csv(file_name, usecols=cols)
	# Y_data = pd.read_csv('./taxi_01.csv', usecols=Y_cols)
	print(data.columns)
	# Y_data = data['total_amount']
	# X_data = data.drop(['total_amount'], axis=1)
	output_file = "./output_data/" + "data_"+ str(i) + ".csv"
	data.to_csv (output_file, index = None, header=True)
	# Y_data.to_csv ('./labels_data.csv', index = None, header=True)

def process_data(file_name):
	print(file_name)
	pd_data = pd.read_csv(file_name)
	return pd_data

def cobmine_data():
	subdirname = './test/'
	depthfiles = glob.glob(subdirname + '*.csv');
	frames = [process_data(f) for f in depthfiles]
	result = pd.concat(frames)
	result.to_csv("./year_data.csv", index=None, header=True)
    
# depthfiles = glob.glob(subdirname + '*.csv');

# for i in range(len(depthfiles)):
# 	save_data(depthfiles[i], i)

cobmine_data()