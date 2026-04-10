import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import matplotlib.pyplot as plt

data=pd.read_csv("phishing_data.csv")
X=data.drop("label",axis=1)
y=data["label"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

model=RandomForestClassifier()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
print("Accuracy:",acc)

cm=confusion_matrix(y_test,y_pred)
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.savefig("static/confusion_matrix.png")

with open("model.pkl","wb") as f:
    pickle.dump(model,f)
