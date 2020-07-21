# -*- coding: utf-8 -*-
"""Day 9-14 Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19UrNgdlqkkz4enBOoZg643XZjSXdSVXZ

#Install

*note:
day 8 was GitHub Tutorials,
this was week 7/13-17
"""

pip install sklearn

pip install quandl

pip install pandas

import pandas as pd 
import quandl
import math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import numpy as np
import datetime 
import matplotlib.pyplot as plt
from matplotlib import style
import random
import pickle
from collections import Counter

"""# Linear Regression 1-12

## 1-2 Regression Intro
"""

import pandas as pd 
import quandl

df = quandl.get("EOD/DIS", authtoken="Dbe_ku9TBLRgTk-zbxFa")
#print(df.head())
df = df[['Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume']]

df['HL_PCT']=(df['Adj_High']-df['Adj_Close'])/df['Adj_Close'] * 100.0
df['PCT_Change']=(df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] * 100.0

df = df[['Adj_Close', 'HL_PCT', 'PCT_Change', 'Adj_Volume']]
print(df.head())

"""## 3 Regression Features and Labels"""

import math
forecast_col= 'Adj_Close'
df.fillna(-99999, inplace=True) #replaces na and blanks 
forecast_out = int(math.ceil(0.01*len(df))) #to get 10 days in the future

df ['label'] = df[forecast_col].shift(-forecast_out)



df.dropna(inplace=True)

print(df.head())

"""##4 Regression Training and Testing"""

from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size=0.2)

#clf= svm.SVR(kernel='poly') #score vector regression
clf=LinearRegression()  #(n_jobs=10)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test)  #confidence level
print(accuracy)

"""##5 Regression forecasting and predicting"""

df = quandl.get("EOD/DIS", authtoken="Dbe_ku9TBLRgTk-zbxFa")
#print(df.head())
df = df[['Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume']]

df['HL_PCT']=(df['Adj_High']-df['Adj_Close'])/df['Adj_Close'] * 100.0
df['PCT_Change']=(df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] * 100.0

df = df[['Adj_Close', 'HL_PCT', 'PCT_Change', 'Adj_Volume']]

df ['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = X[:-forecast_out:]
X_lately = X[-forecast_out:]
X = preprocessing.scale(X)

df.dropna(inplace=True)

y = np.array(df['label'])
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size=0.2)

clf=LinearRegression(n_jobs=10)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test) 

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out) #gives you the next 30 days for prices

import datetime 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df['Forecast']=np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day=86400
next_unix = last_unix + one_day

for i in forecast_set:
  next_date = datetime.datetime.fromtimestamp(next_unix)
  next_unix += one_day
  df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj_Close'].plot()
df['Forecast']

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

"""##6 Pickling and Scaling"""

import pickle

clf=LinearRegression(n_jobs=10)
clf.fit(X_train, y_train)
with open ('linearregression.pickle', 'wb') as f:
  pickle.dump(clf, f)
  pickle_in = open('linearregression.pickle', 'rb')
clf=pickle.load(pickle_in)


accuracy = clf.score(X_test,y_test) 

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)


style.use('ggplot')

df['Forecast']=np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day=86400
next_unix = last_unix + one_day

for i in forecast_set:
  next_date = datetime.datetime.fromtimestamp(next_unix)
  next_unix += one_day
  df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj_Close'].plot()
df['Forecast']

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

"""##7 Regression How it Works (notes, no code)

Best fit line 

*   y=mx+b

##8-9 How to program the Best Fit Slope - Finding m & b
"""

from statistics import mean
import numpy as np

xs= np.array([1,2,3,4,5,6], dtype=np.float64)
ys= np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope(xs,ys):
  m = ( ((mean(xs)*mean(ys))-mean(xs*ys)) /
       ((mean(xs)**2) - mean(xs**2)))
  return m 
m=best_fit_slope(xs,ys)

print(m)

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs= np.array([1,2,3,4,5,6], dtype=np.float64)
ys= np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
  m = ( ((mean(xs)*mean(ys))-mean(xs*ys)) /
       ((mean(xs)**2) - mean(xs**2)))
  b = mean(ys)-m*mean(xs)
  return m, b 
m,b=best_fit_slope_and_intercept(xs,ys)

#print(m,b)
regression_line= [(m*x)+b for x in xs]


predict_x = 8
predict_y = (m*predict_x)+b


plt.scatter(xs,ys)

plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs, regression_line)

plt.show()

"""##10-11 R Squared"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs= np.array([1,2,3,4,5,6], dtype=np.float64)
ys= np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
  m = ( ((mean(xs)*mean(ys))-mean(xs*ys)) /
       ((mean(xs)**2) - mean(xs**2)))
  b = mean(ys)-m*mean(xs)
  return m, b 

def squared_error(ys_orig, ys_line):
  return sum((ys_line-ys_orig**2))

def coefficient_of_determination(ys_orig,ys_line):
  y_mean_line= [mean(ys_orig) for y in ys_orig]
  squared_error_regr = squared_error(ys_orig, ys_line)
  squared_error_y_mean = squared_error(ys_orig, y_mean_line)
  return 1 - (squared_error_regr / squared_error_y_mean)


m,b=best_fit_slope_and_intercept(xs,ys)

#print(m,b)
regression_line= [(m*x)+b for x in xs]


predict_x = 8
predict_y = (m*predict_x)+b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)

plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs, regression_line)

plt.show()

"""##12 Testing Assumptions"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs= np.array([1,2,3,4,5,6], dtype=np.float64)
#ys= np.array([5,4,6,5,6,7], dtype=np.float64)

def create_dataset(hm, varience, step=2, correlation=False):    #hm is 'how many'
  val=1
  ys=[]
  for i in range(hm):
    y= val + random.randrange(-varience, varience)
    ys.append(y)
    if correlation and correlation == 'pos':
      val+=step
    elif correlation and correlation == 'neg':
      val-=step
  xs = [i for i in range(len(ys))]
  return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def best_fit_slope_and_intercept(xs,ys):
  m = ( ((mean(xs)*mean(ys))-mean(xs*ys)) /
       ((mean(xs)**2) - mean(xs**2)))
  b = mean(ys)-m*mean(xs)
  return m, b 

def squared_error(ys_orig, ys_line):
  return sum((ys_line-ys_orig**2))

def coefficient_of_determination(ys_orig,ys_line):
  y_mean_line= [mean(ys_orig) for y in ys_orig]
  squared_error_regr = squared_error(ys_orig, ys_line)
  squared_error_y_mean = squared_error(ys_orig, y_mean_line)
  return 1 - (squared_error_regr / squared_error_y_mean)


xs,ys = create_dataset(40, 10, 2, correlation='pos')   #if you decrease the varience the r squared increases


m,b=best_fit_slope_and_intercept(xs,ys)

#print(m,b)
regression_line= [(m*x)+b for x in xs]


predict_x = 8
predict_y = (m*predict_x)+b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
#plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()

df = quandl.get("EOD/DIS", authtoken="Dbe_ku9TBLRgTk-zbxFa")

df = df[['Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume']]

df['HL_PCT']=(df['Adj_High']-df['Adj_Close'])/df['Adj_Close'] * 100.0
df['PCT_Change']=(df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] * 100.0

#         price          x           x              x
df = df[['Adj_Close', 'HL_PCT', 'PCT_Change', 'Adj_Volume']]

forecast_col= 'Adj_Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df))) 

df ['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label', 'Adj_Close'],1))
X = X[:-forecast_out]
X_lately = X[-forecast_out:]
X = preprocessing.scale(X)


df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size=0.2)

clf=LinearRegression(n_jobs=10)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test,y_test) 

forecast_set = clf.predict(X_lately)
#print(forecast_set, accuracy, forecast_out)

df['Forecast']=np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day=86400
next_unix = last_unix + one_day

for i in forecast_set:
  next_date = datetime.datetime.fromtimestamp(next_unix)
  next_unix += one_day
  df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj_Close'].plot()
df['Forecast']

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

"""# K Nearest Neighbor 13-19

## 13-14 Classification w/ K Nearest Neighbors

data from https://archive.ics.uci.edu/ml/datasets.php
"""

import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd 

df = pd.read_csv('breast-cancer-wisconsin.data')

df.columns = ['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size',
              'bare_nuclei','bland_chrom','norm_nucleoli','mitoses','class']
df.replace('?', -99999, inplace=True)

df.drop(['id'],1,inplace=True)

X= np.array(df.drop(['class'],1))
y= np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([4,2,1,1,1,2,3,2,1])
example_measures = example_measures.reshape(1,-1)

prediction=clf.predict(example_measures)
print(prediction)

"""## 15 Euclidean Distance"""

from math import sqrt

plot1=[1,3]
plot2=[2,5]

euclidean_distance= sqrt( (plot1[0]-plot2[0])**2 +(plot1[1]-plot2[1])**2 )
print(euclidean_distance)

"""##16 Creating Our K Nearest Neighbors Algorithm"""

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset ={'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features=[5,7]

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset [i]] for i in dataset]
plt.scatter(new_features[0],new_features[1], s=100)  #s means size
plt.show()


def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k:
    warnings.warn('K is not equal to value less that total voting groups')

    knnalgos
    return vote_result

"""##17 Writing our own K Nearest Neighbors in Code"""

def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k:
    warnings.warn('K is not equal to value less that total voting groups')
  distances= []
  for group in data:
    for features in data[group]:
      euclidean_distance= np.linalg.norm(np.array(features)-np.array(predict))
      distances.append([euclidean_distance, group])
  votes = [i[1] for i in sorted(distances)[:k]]
  print(Counter(votes).most_common(1))
  vote_result= Counter(votes).most_common(1)[0][0]
  
  return vote_result

result=k_nearest_neighbors(dataset, new_features, k=3)
print(result)

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset [i]] for i in dataset]
plt.scatter(new_features[0],new_features[1], s=100, color=result)  #now it should color match with its neighbors 
plt.show()

"""## 18 Applying our K Nearest Neighbors Algorithm"""

import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k:
    warnings.warn('K is not equal to value less that total voting groups')
  distances= []
  for group in data:
    for features in data[group]:
      euclidean_distance= np.linalg.norm(np.array(features)-np.array(predict))
      distances.append([euclidean_distance, group])
  votes = [i[1] for i in sorted(distances)[:k]]
  #print(Counter(votes).most_common(1))
  vote_result= Counter(votes).most_common(1)[0][0]
  
  return vote_result


df = pd.read_csv('breast-cancer-wisconsin.data')

df.columns = ['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size',
              'bare_nuclei','bland_chrom','norm_nucleoli','mitoses','class']

df.replace('?', -99999, inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()

random.shuffle(full_data)
#print(full_data[:5])

test_size= 0.2
train_set= {2:[], 4:[]} 
test_set= {2:[], 4:[]} 
train_data= full_data[:-int(test_size*len(full_data))]
test_data= full_data[-int(test_size*len(full_data)):]

for i in train_data:
  train_set[i[-1]].append(i[:1])

for i in test_data:
  test_set[i[-1]].append(i[:1])

correct=0
total=0

for group in test_set:
  for data in test_set[group]:
    vote= k_nearest_neighbors(train_set, data, k=25)
    if group == vote:
      correct += 1 
    total +=1

print('Accuracy:', correct/total)

"""## 19 Final thoughts on K Nearest Neighbors"""

def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k:
    warnings.warn('K is not equal to value less that total voting groups')
  distances= []
  for group in data:
    for features in data[group]:
      euclidean_distance= np.linalg.norm(np.array(features)-np.array(predict))
      distances.append([euclidean_distance, group])
  votes = [i[1] for i in sorted(distances)[:k]]
  vote_result= Counter(votes).most_common(1)[0][0]
  confidence= Counter(votes).most_common(1)[0][0] / k
  #print(vote_result, confidence)
  return vote_result, confidence


df = pd.read_csv('breast-cancer-wisconsin.data')
df.columns = ['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size',
              'bare_nuclei','bland_chrom','norm_nucleoli','mitoses','class']
df.replace('?', -99999, inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()

random.shuffle(full_data)

test_size= 0.4
train_set= {2:[], 4:[]} 
test_set= {2:[], 4:[]} 
train_data= full_data[:-int(test_size*len(full_data))]
test_data= full_data[-int(test_size*len(full_data)):]

for i in train_data:
  train_set[i[-1]].append(i[:1])

for i in test_data:
  test_set[i[-1]].append(i[:1])

correct=0
total=0

for group in test_set:
  for data in test_set[group]:
    vote,confidence= k_nearest_neighbors(train_set, data, k=5)
    if group == vote:
      correct += 1 
    else: 
      print(confidence)
    total +=1
print('Accuracy:', correct/total)

accuracies = []

for i in range(25):

  df = pd.read_csv('breast-cancer-wisconsin.data')
  df.columns = ['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size',
              'bare_nuclei','bland_chrom','norm_nucleoli','mitoses','class']
  df.replace('?', -99999, inplace=True)
  df.drop(['id'],1,inplace=True)
  full_data = df.astype(float).values.tolist()

  random.shuffle(full_data)

  test_size= 0.4
  train_set= {2:[], 4:[]} 
  test_set= {2:[], 4:[]} 
  train_data= full_data[:-int(test_size*len(full_data))]
  test_data= full_data[-int(test_size*len(full_data)):]

  for i in train_data:
    train_set[i[-1]].append(i[:1])

  for i in test_data:
    test_set[i[-1]].append(i[:1])

  correct=0
  total=0

  for group in test_set:
    for data in test_set[group]:
      vote,confidence= k_nearest_neighbors(train_set, data, k=5)
      if group == vote:
        correct += 1 
      total +=1
  #print('Accuracy:', correct/total)
  accuracies.append(correct/total)

print(sum(accuracies)/len(accuracies))

"""# SVM 20-

##20 Support Vector Machine Intro and Application (SVM)

*   finding the best seperating hyperplane to classify new data points
*   Binary classifier(the catagories can't be mixed together)
"""

import numpy as np
from sklearn import preprocessing, model_selection, neighbors, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.columns = ['id','clump_thickness','unif_cell_size','unif_cell_shape','marg_adhesion','single_epith_cell_size',
              'bare_nuclei','bland_chrom','norm_nucleoli','mitoses','class']
df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = svm.SVC()
clf = neighbors.KNeighborsClassifier()


clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)

example_measures = np.array([[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print(prediction)

"""## 21-22 Understanding Vectors/Support Vector Assertion (notes, no code)
## 23-24 SVM Fundamentals and Optimization

A= [1,3]  B= [2,4]
*   direction A = [x,y]
*   magnitude- length ||A|| = sqrt(x^2 + y^2)
*   dot product = A.B = 1x2 + 3x4 (scalar value)
*   hyperplane = (w*x) + b   
*   b = bias

optimization

*   minimize ||w||
*   maximize b 
*   to find the smallest magnitude(w) and largest b

constraint 

*   yi(xi*w + b) >= 1
*   w = vector
*   in python : class(KnownFeatures.w+b) >= 1 

convex problem (bowl shape)

##25 Creating an SVM from scratch
"""

import matplotlib.pyplot as plt
from matplotlib import style