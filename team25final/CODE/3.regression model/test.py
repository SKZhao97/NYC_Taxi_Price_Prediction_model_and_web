import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import utils as utils
import numpy as np
import glob

def predict(X_test):
	#feature columns [2,3,5,6,11,12,13]
	print('Loading model to predict...')
	# load model to predict
	bst = lgb.Booster(model_file='./model.txt')
	# can only predict with the best iteration (or the saving iteration)
	y_pred = bst.predict(X_test)

	return y_pred

# X_train, Y_train, X_test, Y_test = utils.get_train_test()

subdirname = './data/rush_hour/'
depthfiles = glob.glob(subdirname + '*.csv')
for i in range(len(depthfiles)):
	X_test = pd.read_csv(depthfiles[i])
	Y_test = predict(X_test)
	file_tokens = depthfiles[i].split("/")
	file_name = file_tokens[len(file_tokens) - 1]
	print(depthfiles[i])
	output_name = "./test_result/predictions_" + file_name
	np.savetxt(output_name, Y_test, delimiter=",")
