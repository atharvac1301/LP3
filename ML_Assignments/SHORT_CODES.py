import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv()

df.isnull().sum()

df = df.drop(columns=[])

df.dropna(inplace=True)


z_scores = stats.zscore(df['fare_amount'])
z_threshold = 3

df_filtered = df[abs(z_scores) <= z_threshold]
outliers = df[abs(z_scores) > z_threshold]


corr_matrix = sns.heatmap(df_filtered.corr(), annot=True)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay


cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=['Not Spam', 'Spam']).plot()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

from keras.models import Sequential
from keras.layers import Dense


dict = {}
df[column].map(dict)

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = Sequential([
    Dense(8, activation='relu'),
    Dense(8, activation='relu'),
    Dense(8, activation='relu'),
    Dense(8, activation='relu'),
    Dense(8, activation='sigmoid'),
    
    
])

model.compile(optim, loss, metrics=['accuracy'])
history = model.fit(X_train, y_train, batch_size, epochs)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['accuracy'], label='Accuracy')

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()


import numpy
import matplotlib.pyplot as plt

def function(x):
    return (x+3)**2

def derivative(x):
    return 2*(x+3)

def grad_descent(starting_x, lr, num_iter):
    x = starting_x
    x_history = [x]
    
    for i in range(num_iter):
        x = x - lr * derivative(x)
        x_history.append(x)
        print(f"Iterations: {i}, Value: {x}")
    
    return x, x_history



plt.plot(x_history, function(np.array(x_history)), marker='o')


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


dict = {}
df[column] = df[column].map(dict)


sse = []

for k in range(1, 11):
    model = KMeans(n_clusters=k)
    model.fit(df)
    sse.append(model.inertia_)    # Important step

plt.plot(range(1, 11), sse, marker='o')

K = 3
model = KMeans(n_clusters=K)
df['Cluster'] = model.fit_predict(df)   # new column for cluster no.

