import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('subway_2.csv', encoding='cp949').rename(columns={'노선명': 'Line', '승차총승객수': 'OnBoard', '하차총승객수': 'OffBoard'})
df['Line'] = df['Line'].str.extract('(\d+)').astype(int)
df.groupby('Line')[['OnBoard', 'OffBoard']].mean().plot(kind='bar', title="Average OnBoard & OffBoard by Line")
plt.xlabel("Line")
plt.ylabel("Average Count")
plt.show()
X, y = df[['OnBoard', 'OffBoard']], df['Line']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
input_val = pd.DataFrame({'OnBoard': [30000], 'OffBoard': [30000]})
models = {'KNN': KNeighborsClassifier(),'Logistic Regression': LogisticRegression(max_iter=2000),'Decision Tree': DecisionTreeClassifier()}
accuracies, predictions = {}, {}
print("\nModel Accuracy and Predictions:")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prediction = model.predict(input_val)[0]
    accuracies[name] = acc
    predictions[name] = prediction
    print(f"{name} => Accuracy: {acc:.4f}, Prediction: {prediction}")
best_model = max(accuracies, key=accuracies.get)
print(f"\nBest Model: {best_model} with Accuracy: {accuracies[best_model]:.4f}")
