import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

np.random.seed(53)
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1
)

X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

classifiers = [
    ("Linear SVC", SVC(kernel="linear")),
    ("Radial SVC", SVC(kernel="rbf")),
    (
        "Multinomial Logistic Regression",
        LogisticRegression(multi_class="multinomial", solver="saga", penalty="l1"),
    ),
    ("Random Forest", RandomForestClassifier(n_estimators=200)),
]

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 8))
ax = ax.flat
cm = "BrBG"
cm_bright = plt.cm.tab20c
step = 0.02
ax[0].set_xticks(())
ax[0].set_yticks(())
for ix, (title, clf) in enumerate(classifiers):
    clf.fit(X_train, y_train)

    a = ax[ix]
    a.set_title(title)

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    Z = Z.reshape(xx.shape)
    a.contourf(xx, yy, Z, cmap=cm, alpha=0.8)

    a.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    a.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )

from pyrolite.util.plot import save_figure

save_figure(
    fig,
    name="ClassifierComparison",
    save_at="../../presentation/figures/",
    save_fmts=["png", "pdf"],
)
