import Algorithmia
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def random_forest_classifier(features, target):
    """
    To train the random forest classifier with features and target data
    :param features:
    :param target:
    :return: trained random forest classifier
    """
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

def apply(input):
    # dataset = pd.read_csv('data://vneogi199/training/Algorithmia-phishing.csv')
    dataset = pd.read_csv('data://.my/training/Algorithmia-phishing.csv')
    trained_model = random_forest_classifier(dataset[:,:29], dataset[:,29])
    print("Trained model :: "+ trained_model)
    return "hello {}".format(list(zip(train[features], clf.feature_importances_)))
