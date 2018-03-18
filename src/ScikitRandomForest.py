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
    df.head()
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df.head()
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    df.head()
    train, test = df[df['is_train']==True], df[df['is_train']==False]
    features = df.columns[:4]
    features
    
    
    
    
    return "hello {}".format(input)
