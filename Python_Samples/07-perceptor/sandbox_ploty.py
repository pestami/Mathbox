#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     18.03.2025
# Copyright:   (c) SESA237770 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def main():
##    pass

import plotly.express as px
import pandas as pd
import numpy as np


if __name__ == '__main__':
##    main()



##    # Create sample data
##    np.random.seed(42)
##    df = pd.DataFrame({
##        'x': np.random.normal(0, 1, 100),
##        'y': np.random.normal(0, 1, 100),
##        'category': ['A'] * 50 + ['B'] * 50
##    })
##    ## ['A'] * 50  = ['A' , 'A'.......
##
##    print(df)
##    # Create basic scatter plot
##    fig = px.scatter(df, x='x', y='y')

##    fig.show()




##    # initialize data of lists.
##    data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
##            'Age': [20, 21, 19, 18]}
##
##    # Create DataFrame
##    df = pd.DataFrame(data)
##
##    print(df)

    #CREATE DATAFRAME FROM SERIS OF LISTS
    # initialize list of lists
    data = [[5, 10], [0, 15], [8, 14]]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['X1', 'X2'])
    print(df)


    fig = px.scatter(df, x='X1', y='X2')

    fig.show()


