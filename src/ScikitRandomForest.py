import Algorithmia
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np
np.random.seed(0)


# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    train, test = df[df['is_train']==True], df[df['is_train']==False]
    features = df.columns[:4]
    y = pd.factorize(train['species'])[0]
    clf = RandomForestClassifier(n_jobs=2, random_state=0)
    clf.fit(train[features], y)
    clf.predict(test[features])
    clf.predict_proba(test[features])[0:10]
    preds = iris.target_names[clf.predict(test[features])]
    print(preds[0:5])
    pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])
    print(list(zip(train[features], clf.feature_importances_)))
    
    
    
    
    return "hello {}".format(list(zip(train[features], clf.feature_importances_)))
