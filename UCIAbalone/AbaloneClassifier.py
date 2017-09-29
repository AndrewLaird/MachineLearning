import numpy as np
import pandas as pd
from sklearn import model_selection, neighbors, linear_model, preprocessing, feature_selection

dataframe = pd.read_csv("abalone.data")

dataframe = pd.get_dummies(dataframe)

X = dataframe.drop(["age"],1)
y = dataframe["age"]

X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=.2)

model = linear_model.LinearRegression()
#model = neighbors.KNeighborsClassifier()


model = feature_selection.RFECV(model, step=1, cv=10)

model.fit(X_train,y_train)


accuracy = model.score(X_test,y_test)
print(accuracy)

difference = 0

X_test = np.array(X_test)
for index in range(len(X_test)):
    prediction = model.predict(X_test[index].reshape([1,-1]))[0]
    actual = np.array(y_test)[index]
    print("{:.1f}".format(prediction),actual)
    difference += abs(prediction - actual)


print("mean difference is",abs(difference/len(X_test)))

