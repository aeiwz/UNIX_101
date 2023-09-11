__
#Creat package for data generation
# Create a function called create_data() in datagen.py that takes two arguments: num_rows and num_cols.
# The function should return a pandas DataFrame with num_rows rows and num_cols columns of random numbers.
# The random numbers should be between 0 and 1.
# The column names should be the letters A, B, C, etc.
# The row names should be the numbers 1, 2, 3, etc.
# The function should also print out the shape of the DataFrame it returns.
# Create a file called test.py that imports the create_data() function from datagen.py.
# In test.py, call the create_data() function with the arguments 10 and 1000.

import pandas as pd
import numpy as np


def __init__(level=NOTSET):
    pass

def create_data(num_rows, num_cols):
    df = pd.DataFrame(np.random.rand(num_rows, num_cols))
    df.columns = [chr(65+i) for i in range(num_cols)]
    df.index = [i for i in range(num_rows)]
    print(df.shape)
    return df



