import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import utils as utils

def predict(X_test):
	#feature columns [2,3,5,6,11,12,13]
	print('Loading model to predict...')
	# load model to predict
	bst = lgb.Booster(model_file='./model.txt')
	# can only predict with the best iteration (or the saving iteration)
	y_pred = bst.predict(X_test)

	return y_pred[0]

X_train, Y_train, X_test, Y_test = utils.get_train_test()

res = predict(X_test)

print("Prediction amount of fare is  ----------------> " + str(res))
