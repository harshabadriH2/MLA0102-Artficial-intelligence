from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [
    [22, 0],
    [25, 0],
    [47, 1],
    [52, 1],
    [46, 1],
    [56, 1],
    [55, 0],
    [60, 0]
]

y = [0, 0, 1, 1, 1, 1, 0, 0]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
