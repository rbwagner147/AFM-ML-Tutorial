#Logistic Regression 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import import_data.py
from sklearn import metrics

dataset = pd.read_csv('')
dataset.head()
import_data_py(['Material used','AFM y_value'])

x_train, x_test, y_train, y_test = train_test_split(dataset[['z distance']], y, test_size = 1, random_state = 0)


y= np.arrange

model = LogisticRegression(solver='liblinear', random_state=0)

model.fit(x_train, y_train)

model.classes_

pred_data = model.predict(x_test)



model.score(x_test, y_test)

cnf_m = confusion_matrix(y, pred_data)
report = classification_report(y, pred_data)

print(classification_report(y, model.predict_proba(x_train)))

plt.tight_layout()
plt.title('AFM')
plt.xlabel('Material used')
plt.ylabel('Contact made or not')
plt.legend()
plt.show()


