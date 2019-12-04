import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import utils as utils



# data = pd.read_csv('./data.csv')
# # Y_data = pd.read_csv('./taxi_01.csv', usecols=Y_cols)
# print(data.columns)
# train, test = train_test_split(data, test_size=0.2)

# Y_train = train['total_amount']
# X_train = train.drop(['total_amount'], axis=1)

# Y_test = test['total_amount']
# X_test = test.drop(['total_amount'], axis=1)
# print(X_train.head())

# X_train = normalization(X_train)
# X_test = normalization(X_test)

X_train, Y_train, X_test, Y_test = utils.get_train_test()


# create dataset for lightgbm
lgb_train = lgb.Dataset(X_train, Y_train)
lgb_eval = lgb.Dataset(X_test, Y_test)

# specify your configurations as a dict
params = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': {'l2', 'l1'},
    'num_leaves': 100,
    'max_depth': 15,
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
                num_boost_round=100,
                valid_sets=lgb_eval,
                early_stopping_rounds=100)

print('Saving model...')
# save model to file
gbm.save_model('model.txt')
# print(X_train)
print('Starting predicting...')
# predict
Y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
# eval
print('The rmse of prediction is:', mean_squared_error(Y_test, Y_pred) ** 0.5)

mean_percentage_error = utils.mean_absolute_percentage_error(Y_test, Y_pred)
print('The mean percentage error is:' + str(mean_percentage_error))
print("prediction ---->")
print(Y_pred[0:10])
print("actual ------>")
print(Y_test.head(10))