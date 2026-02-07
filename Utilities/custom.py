import numpy as np
import pandas as pd


abundances=['Fe/H', 'Na/Fe', 'O/Fe']
def data_loader(target, xysplit=False, return_test_data=False, full_data_filename='../Datasets/NGC_combi.csv', target_folder='../Datasets'):
	df_full=pd.read_csv(full_data_filename)
	df_full.set_index('Star ID')
	test_indeces=pd.read_csv("{target_folder}/{target.replace('/', '_')}_TEST_IDs.csv")
	df=df_full.drop(np.array(test_indeces['Star ID']))
	train, test=df, df_full.loc[test_indeces]
	X_train=train.drop(abundances, axis=1)
	X_test=test.drop(abundances, axiis=1)
	y_train=train[target]
	y_test=test.loc[target]
	if return_test_data==True:
		if xysplit==True:
			return X_train, X_test, y_train, y_test
		else:
			return train, test
	else:
		if xysplit==True:
			return X_train, y_train
		else:
			return train
