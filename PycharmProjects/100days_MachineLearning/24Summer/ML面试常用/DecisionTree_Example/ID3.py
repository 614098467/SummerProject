
import pandas as pd
from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'True'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = DataFrame(data)
df = pd.get_dummies(df,columns = ['Outlook', 'Temperature', 'Humidity', 'Windy'])

X = df.drop(columns='PlayTennis')
y = df['PlayTennis'].apply(lambda x:1 if x == 'Yes' else 0)

X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.3,random_state=1)
tree = DecisionTreeClassifier(criterion='entropy',random_state=42)

tree.fit(X_train,y_train)

y_pred = tree.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print(acc)
plt.figure(figsize=(12, 8))
plot_tree(tree, feature_names=list(X.columns), class_names=['No', 'Yes'], filled=True)
plt.show()
