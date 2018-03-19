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

def process_input(input):
    # Create numpy array from csv file passed as input in apply()
    if input.startswith('data:'):
        file_url = client.file(input).getFile().name
        try:
            np_array = np.genfromtxt(file_url, delimiter=',')
            print(np_array)
            return np_array
        except Exception as e:
            print("Could not create numpy array from data", e)
            sys.exit(0)


def apply(input):
    dataset = process_input(data://vneogi199/training/Algorithmia-phishing.csv)
    trained_model = random_forest_classifier(dataset[:,:29], dataset[:,29])
    print("Trained model :: "+ trained_model)
    return "hello {}".format(list(zip(train[features], clf.feature_importances_)))
