from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler

X, y = make_classification(
    n_classes=2,
    class_sep=2,
    weights=[0.1, 0.9],
    n_informative=3,
    n_redundant=1,
    flip_y=0,
    n_features=20,
    n_clusters_per_class=1,
    n_samples=1000,
    random_state=10,
)
print(f"Original dataset shape %s" % Counter(y))
print(f"X shape {X.shape}")
# Original dataset shape Counter({{1: 900, 0: 100}})
ros = RandomOverSampler(random_state=42)
X_res, y_res = ros.fit_resample(X, y)
print("Resampled dataset shape %s" % Counter(y_res))
print(f"Resampled X {X_res.shape}")
# Resampled dataset shape Counter({{0: 900, 1: 900}})
