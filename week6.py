from sklearn.linear_model import LogisticRegression
import pandas as pd

url = 'http://bit.ly/kaggletrain'
train = pd.read_csv(url)

feature_cols = ['Pclass', 'Parch']
X = train.loc[:, feature_cols]
y = train.Survived

logreg = LogisticRegression()
logreg.fit(X, y)
url_test = 'http://bit.ly/kaggletest'
test = pd.read_csv(url_test)
X_new = test.loc[:, feature_cols]
new_pred_class = logreg.predict(X_new)

kaggle_data = pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).set_index('PassengerId')
kaggle_data.to_csv('sub.csv')

train.to_pickle('train.pkl')
pd.read_pickle('train.pkl')
