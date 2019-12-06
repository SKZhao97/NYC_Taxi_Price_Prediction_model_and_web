import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import utils as utils
import numpy as np

X_train, Y_train, X_test, Y_test = utils.get_train_test()


# create dataset for lightgbm
lgb_train = lgb.Dataset(X_train, Y_train)
lgb_eval = lgb.Dataset(X_test, Y_test)

# experiment parameters:
# num_leaves: 20, 50, 100, 200
# max_depth: 5, 8, 10, 15
# learning_rate: 0.001, 0.01, 0.05, 0.1
# num_bosst_round: 20, 100, 1000, 2000

num_leaves_list = [20,50,100,200]
max_depth_list = [5, 10, 15, 25]
learning_rate_list = [0.001, 0.01, 0.05, 0.1]
num_boost_round_list = [20, 100, 1000, 2000, 4000]

MSRE = []
MCE = []

for i in range(len(max_depth_list)):
    print("Iteration----------------------->", i)
    params = {
        'boosting_type': 'gbdt',
        'objective': 'regression',
        'metric': {'l2', 'l1'},
        'num_leaves': 100,
        'max_depth': max_depth_list[i],
        'learning_rate': 0.05,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.8,
        'bagging_freq': 5,
        'verbose': 0
    }

    print('Starting training...')
    # trainazure
    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=1000,
                    valid_sets=lgb_eval,
                    early_stopping_rounds=1000)

    print('Starting predicting...')
    # predict
    Y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    # eval
    msre = mean_squared_error(Y_test, Y_pred) ** 0.5
    print('The rmse of prediction is:', msre)
    MSRE.append(msre)

    mean_percentage_error = utils.mean_absolute_percentage_error(Y_test, Y_pred)
    print('The mean percentage error is:', mean_percentage_error)
    MCE.append(mean_percentage_error)

res = [MSRE, MCE]
output_name = "./metrix/experiment_num_max_depth.txt"
np.savetxt(output_name, res, delimiter=",")