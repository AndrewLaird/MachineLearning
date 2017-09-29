import numpy as np
import pandas as pd

from sklearn import linear_model, model_selection, neighbors,feature_selection

dataframe = pd.read_csv("winequality-red.csv")

X = dataframe.drop(["quality"],1)
y = dataframe["quality"]

X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=.2)

classifier = linear_model.LinearRegression()
#classifier = neighbors.KNeighborsClassifier()
classifier  = feature_selection.RFECV(classifier, step=1, cv=10)


classifier.fit(X_train,y_train)
print(classifier.score(X_test,y_test))
difference = 0
print(X_test.__class__.__name__)

X_test = np.array(X_test)
for index in range(len(X_test)):
    prediction = classifier.predict(X_test[index].reshape([1,-1]))[0]
    actual = np.array(y_test)[index]
    print("{:.1f}".format(prediction),actual)
    difference += abs(prediction - actual)


print("mean difference is",abs(difference/len(X_test)))

