from sklearn.metrics import accuracy_score, classification_report

def evaluar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print("Accuracy:", acc)

    print("\nReporte de clasificación:\n")
    print(classification_report(y_test, y_pred))

    return acc, y_pred