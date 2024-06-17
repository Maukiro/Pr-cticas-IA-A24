import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import LogisticRegression

def evaluate_model(model, X, y):
    # Hold-out validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    holdout_accuracy = accuracy_score(y_test, y_pred)

    # 10-fold Cross Validation
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X, y, cv=kf)
    cv_accuracy = np.mean(cv_scores)

    return holdout_accuracy, cv_accuracy

def get_results_models():
    results = {
        "Dataset": [],
        "Model": [],
        "Hold-out Accuracy": [],
        "10-fold CV Accuracy": []
    }
    for name, dataset in datasets.items():
        X, y = dataset.data, dataset.target
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Evaluate MLP
        holdout_acc_mlp, cv_acc_mlp = evaluate_model(mlp, X, y)
        results["Dataset"].append(name)
        results["Model"].append("MLP")
        results["Hold-out Accuracy"].append(holdout_acc_mlp)
        results["10-fold CV Accuracy"].append(cv_acc_mlp)

        # Evaluate RBF
        holdout_acc_rbf, cv_acc_rbf = evaluate_model(rbf, X, y)
        results["Dataset"].append(name)
        results["Model"].append("RBF")
        results["Hold-out Accuracy"].append(holdout_acc_rbf)
        results["10-fold CV Accuracy"].append(cv_acc_rbf)
    return results

if __name__ == '__main__':

    datasets = {
        "Iris": load_iris(),
        "Wine": load_wine(),
        "Breast Cancer": load_breast_cancer()
    }

    mlp = MLPClassifier(max_iter=1000, random_state=42)
    rbf = make_pipeline(RBFSampler(gamma=1, random_state=42), LogisticRegression(max_iter=1000))
    results = get_results_models()
    results_df = pd.DataFrame(results)
    print(results_df)

