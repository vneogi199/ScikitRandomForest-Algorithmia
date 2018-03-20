import Algorithmia
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages

client = Algorithmia.client()

def process_input(input):
    # Create numpy array from csv file passed as input in apply()
    if input.startswith('data:'):
        file_url = client.file(input).getFile().name
        try:
            np_array=pd.read_csv(file_url)
            #np_array = np.genfromtxt(file_url, delimiter=',')
            print(np_array)
            return np_array
        except Exception as e:
            print("Could not create numpy array from data", e)
            sys.exit(0)

def apply(input):
    train=process_input('data://vneogi199/training/Algorithmia-phishing.csv')
    test = process_input(input)
    cols =list(train.columns)
    cols=cols[:len(cols)-1]
    colsRes = ['Result']
    trainArr = train.as_matrix(cols) #training array
    trainRes = train.as_matrix(colsRes) # training results
    rf = RandomForestClassifier(n_estimators=100) # initialize
    rf.fit(trainArr, trainRes) # fit the data to the algorithm
    testArr = test.as_matrix(cols)
    result1 = rf.predict(testArr)
    test['predictions'] = result1
    return test['predictions']