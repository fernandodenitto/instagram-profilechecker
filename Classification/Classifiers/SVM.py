# CONTEXT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# IMPORT ALL THE UTILS FOR THE DATASET
from dataset_utils import *

# IMPORT THE SCIKIT FUNCTIONS
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# IMPORT THE ORIGINAL DATASET
df_real = pd.read_csv('../../data/balanced_real_data.csv')
df_fake = pd.read_csv('../../data/balanced_fake_data.csv')
dataset=pd.concat([df_real,df_fake],ignore_index=True)
dataset=fix_private_entries(dataset)


# TAKE THE TRAINSET AND THE TARGET FROM DATASET
trainset=get_trainset(dataset)
targets=get_target_dataset(dataset)


# DELETING THE STATISTICS OF THE USERS CONTENTS
trainset_without_stats=drop_stats(trainset)

# STANDARDIZE DATASET
trainset_without_stats=StandardScale_dataset(trainset_without_stats)


# TRAINING WITHOUT STATISTICS OF THE USERS CONTENTS
x_train, x_test, y_train, y_test = train_test_split(trainset_without_stats, targets, test_size = 0.2, random_state = 12345)
svc = SVC(gamma='scale')
svc.fit(x_train, y_train)
predictions = svc.predict(x_test)


print("\nPERFORMANCE WITHOUT THE STATISTICS OF THE USERS CONTENTS: ")
print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, predictions))

# CLASSIFICATION OF ONLY PUBLIC PROFILES
dataset_publics=drop_NaN_entries(dataset)
trainset_publics=get_trainset(dataset_publics)
targets_publics=get_target_dataset(dataset_publics)

# STANDARDIZE DATASET
trainset_publics=StandardScale_dataset(trainset_publics)


# TRAINING WITH PUBLIC PROFILES (WITH STATITISTIC ON MEDIAS)
x_train, x_test, y_train, y_test = train_test_split(trainset_publics, targets_publics, test_size = 0.2, random_state = 12345)
svc = SVC(gamma='scale')
svc.fit(x_train, y_train)
predictions = svc.predict(x_test)


print("\nPERFORMANCE WITH THE STATISTICS OF THE USERS CONTENTS: ")
print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, predictions))

# CLASSIFICATION WITH NaN VALUES REPLACED WITH STATISTICS
dataset_median=fill_NaN_median(dataset)
trainset_median=get_trainset(dataset_median)
targets_median=get_target_dataset(dataset_median)

# STANDARDIZE DATASET
trainset_median=StandardScale_dataset(trainset_median)

# TRAINING WITH NaN VALUES REPLACED WITH STATISTICS
x_train, x_test, y_train, y_test = train_test_split(trainset_median, targets_median, test_size = 0.2, random_state = 12345)
svc = SVC(gamma='scale')
svc.fit(x_train, y_train)
predictions = svc.predict(x_test)

print("\nPERFORMANCE WITH NaN VALUES REPLACED WITH THE MEDIAN: ")
print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, predictions))