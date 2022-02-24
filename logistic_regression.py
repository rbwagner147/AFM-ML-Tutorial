#Logistic Regression 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import import_data.py
from sklearn import metrics

dataset = pd.read_csv('')
import_data_py(['Material used','AFM y_value'])

xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, test_size = 0.25, random_state = 0)


y= np.arrange

model = LogisticRegression(solver='liblinear', random_state=0)

model.fit(x, y)

model.classes_

pred_data = model.predict_proba(x)

model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)

model.score(x, y)

cnf_matrix = metrics.confusion_matrix(x, y)
cnf_matrix

print(classification_report(y, model.predict_proba(x)))

plt.tight_layout()
plt.title('AFM')
plt.xlabel('Material used')
plt.ylabel('Contact made or not')
plt.legend()
plt.show()


