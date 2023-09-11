# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np


class random_data:
    '''Creat package for data generation
    Create a function called create_data() in datagen.py that takes two arguments: num_rows and num_cols.
    The function should return a pandas DataFrame with num_rows rows and num_cols columns of random numbers.
    The random numbers should be between 0 and 1.
    The column names should be the letters A, B, C, etc.
    The row names should be the numbers 1, 2, 3, etc.
    The function should also print out the shape of the DataFrame it returns.
    Create a file called test.py that imports the create_data() function from datagen.py.
    In test.py, call the create_data() function with the arguments 10 and 1000.'''


    def __init__(self, num_rows=100, num_cols=500):
        self.num_rows = num_rows
        self.num_cols = num_cols

    def create_data(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols

        
        #Creat random data with label in last column and return dataframe
        df = pd.DataFrame(np.random.rand(num_rows, num_cols))
        #random label
        df['labels'] = np.random.randint(0, 2, num_rows)
        #set column name
        
        
        return df
    
    
class analyse_:
    '''Create function to analyse data with PCA model'''
    
    def __init__(self):
        import pandas as pd
        import numpy as np
        from sklearn.decomposition import PCA
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import classification_report
        from sklearn.metrics import roc_curve
        from sklearn.metrics import roc_auc_score
        from matplotlib import pyplot
        from sklearn.metrics import precision_recall_curve
        from sklearn.metrics import f1_score
        from sklearn.metrics import auc
        from sklearn.metrics import average_precision_score


    
    def classification_report(self, df=None):
        
        self.df = df
        
        import pandas as pd
        import numpy as np
        from sklearn.decomposition import PCA
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import classification_report
        from sklearn.metrics import roc_curve
        from sklearn.metrics import roc_auc_score
        from matplotlib import pyplot
        from sklearn.metrics import precision_recall_curve
        from sklearn.metrics import f1_score
        from sklearn.metrics import auc
        from sklearn.metrics import average_precision_score
        #separate labels and data
        labels = df['labels']
        data = df.drop('labels', axis=1)
        
        #split data
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, random_state=2)
        
        #logistic regression
        model = LogisticRegression(solver='lbfgs')
        model.fit(X_train, y_train)
        yhat = model.predict(X_test)
        
        #report
        report = classification_report(y_test, yhat)
        
        return print(report)
    
    
    

    
    
    
    



