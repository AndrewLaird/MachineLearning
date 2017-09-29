import pandas as pd
import numpy as np
from sklearn import neighbors, model_selection

dataframe = pd.read_csv("breast-cancer-wisconsin.data")

dataframe.drop(["id"],1,inplace=True)
dataframe.replace("?",-999,inplace=True)

X = dataframe.drop(['classification'],1)
y = dataframe['classification']

X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y, test_size=.2)

optimizer = neighbors.KNeighborsClassifier()
optimizer.fit(X_train,y_train)

accuracy = optimizer.score(X_test,y_test)
print(accuracy)
print(optimizer.score(X_train,y_train))

test_prediction = np.array([1,1,1,1,1,1,3,1,1]).reshape([1,-1])
print(optimizer.predict(test_prediction))