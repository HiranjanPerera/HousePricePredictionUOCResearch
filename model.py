from pprint import pprint
import pandas as pd
#import self as self
from sklearn import metrics, preprocessing
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.linear_model import Ridge, RidgeClassifier, Lasso, LassoCV, LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedKFold, GridSearchCV, RandomizedSearchCV,RepeatedStratifiedKFold
import random
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, IsolationForest
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
pd.options.mode.chained_assignment = None
from scipy.stats import chi2_contingency, spearmanr
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics



# Model Fitting

# Hyper parameter Tuning
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# Testing
from sklearn.metrics import classification_report, roc_curve, plot_roc_curve

# Decision Tree
from sklearn import tree

# RFECV
from sklearn.feature_selection import RFECV


pd.options.mode.chained_assignment = None
#data = pd.read_csv("Cleaned_training.csv")
data =  pd.read_csv("data.csv")
data.drop(['Time_to_Townnan','Distance_to_MainRDnan','Ava_Electricity_yes','Ava_Water_yes','Age_Ordinal','Distance_to_MainRD','Parking_space','Spl_Arch_Design_Ordinal','Complete_stage_Incomplete','Ava_Supermarket_yes','Furniture_yes','Garden_size_Ordinal'], axis=1, inplace=True)
## Capture the dependent feature
y=data[['Price']]
## drop dependent feature from dataset
X=data.drop(['Price'],axis=1)
## Always remember there way always be a chance of data leakage so we need to split the data first and then apply feature
## Engineering
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.svm import SVR
SVM_regression1 = SVR(C= 4, gamma=10, kernel='linear')
SVRModel = SVM_regression1.fit(X_train,y_train)


             
import pickle
pickle.dump(SVRModel,open('SVRModel.pkl','wb'))

