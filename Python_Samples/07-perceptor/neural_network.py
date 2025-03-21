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

import matplotlib.pyplot as plt
import numpy as np

#===============================================================================
# PANDAS required ?
#===============================================================================

if __name__ == '__main__':

##    for itterations in range(4):  # 0 to 4
##        print(itterations)

#------------------------------------------------------------------------------
# From  BOOK: neural networks for applied sciences and engineering , CH 2.5.3
# Recomended BOOK: pattern recognition (4th, 2008)
# "This book is the outgrowth of our teaching advanced undergraduate and graduate
# courses over the past 20 years."

    W=[0.8,-0.5]  # initial Weights
    X1=[+0.30,-0.60,-0.10,+0.10]
    X2=[+0.70,+0.30,-0.80,-0.45]

    WT=[ 1.05 , 0.025] # Trained Weights

    Y1=[1,1,0,0]   # Traind Output
#------------------------------------------------------------------------------
    YC=[]

    for val in  Y1:
        if (val==0):
            YC.append("red")
        if (val==1):
             YC.append("green")

    #===============================================================================

    # # Prepare the PLOT
    plt.scatter(X1, X2, color='blue')
    plt.xlabel('X1-axis')
    plt.ylabel('X2-axis')
    SW = list(map(str, W))

    plt.title('McCulloch-Pitts.Perceptron W='+ ' '.join(SW))
    plt.axis((-1, +1, -1, +1))
    plt.axis('equal')
    # plt.axis.set_aspect('equal')
    # plt.axisgrid(True, which='both')
    plt.grid(True)


    #===============================================================================
    # Calculate the line of best fit
    #-------------------------------------------------------------------------------
    slope, intercept = np.polyfit(X1, X2, 1)
    xa=np.array(X1)   # i -integer
    xa=np.linspace(-1, 1, num=20)
    line = slope * xa + intercept

    # Plot the scatter plot and line of best fit
    plt.plot(xa, line, color='red', label='Math: Best Line Fit')

    #===============================================================================
    #===============================================================================
    # Plot weights (Decision line)
    #-------------------------------------------------------------------------------
    intercept = 0
    slope=-W[0]/W[1]
    xa=np.linspace(-1, 1, num=20)

    line = slope * xa + intercept
    plt.plot(xa, line, color='black', label='Initial(untrained) Decision Boundary',linestyle='dotted')
    plt.legend()

    #===============================================================================
    # Plot input X1 X2
    #-------------------------------------------------------------------------------
    plt.scatter(X1, X2, c=YC, label='Neuron inputs X1 X2')

    plt.legend()

    #===============================================================================
    plt.show()