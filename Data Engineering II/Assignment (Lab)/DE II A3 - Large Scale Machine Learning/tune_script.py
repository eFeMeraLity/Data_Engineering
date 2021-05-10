import ray
import time
import numpy as np

from sklearn.datasets import fetch_covtype

from sklearn.ensemble import RandomForestClassifier

from ray.tune.sklearn import TuneGridSearchCV
from sklearn.model_selection import train_test_split

# Load the data
data = fetch_covtype()
x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

default_model = RandomForestClassifier()
default_model.fit(x_train, y_train)
default_pred = default_model.predict(x_test)
default_params = default_model.get_params()
default_accuracy = np.count_nonzero(np.array(default_pred) == np.array(y_test)) / len(default_pred)


parameter_grid = {"n_estimators":[10, 50],
                  "max_depth":[5, 50, 100],
                  "ccp_alpha":[0.001, 0.01]}

tune_search = TuneGridSearchCV(RandomForestClassifier(),
                               param_grid = parameter_grid,
                               scoring = "accuracy")

start = time.time()
tune_search.fit(x_train, y_train)
end = time.time()

best_score = tune_search.best_score_
best_params = tune_search.best_params_

print('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

print(f"Default parameters: {default_params}")
print(f"Default accuracy: {default_accuracy}")

print("Tune GridSearch Fit Time:", end - start)
print(f"GridSearch parameters: {best_params}")
print(f"GridSearch score: {best_score}")