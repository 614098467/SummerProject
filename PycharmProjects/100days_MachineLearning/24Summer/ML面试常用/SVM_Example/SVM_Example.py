from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



iris = load_iris()
X,y = iris.data,iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=2)

svm = SVC(kernel='linear')

svm.fit(X_train,y_train)
print(svm.support_vectors_)
y_pred = svm.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print(acc)