# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus


# load dataset
data = pd.read_csv("data/data.csv")

# data=data.dropna()

# #split dataset in features and target variable
# feature_cols = ['profile_pic','biography','follows_count','followed_by_count','ff_ratio','media_count','is_private','is_verified','is_business_account','is_joined_recently','highlight_reel_count','connected_fb_page','average_likes','max_likes','min_likes','std_likes','var_likes','skw_likes','average_comments','max_comments','min_comments','std_comments','var_comments','skw_comments','mean_time_between_posts','max_time_between_posts','min_time_between_posts','std_time_between_posts','var_time_between_posts','skw_time_between_posts']
# X = data[feature_cols] # Features
# y = data['real_account'] # Target variable

# # Split dataset into training set and test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# # Create Decision Tree classifer object
# clf = DecisionTreeClassifier()

# # Train Decision Tree Classifer
# clf = clf.fit(X_train,y_train)

# #Predict the response for test dataset
# y_pred = clf.predict(X_test)

# # Model Accuracy, how often is the classifier correct?
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# dot_data = StringIO()
# export_graphviz(clf, out_file=dot_data,  
#                 filled=True, rounded=True,
#                 special_characters=True, feature_names = feature_cols,class_names=['0','1'])
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# graph.write_png('diabetes.png')
# Image(graph.create_png())


