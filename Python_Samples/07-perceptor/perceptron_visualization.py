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
import numpy as np
import matplotlib.pyplot as plt

class perceptron_visualization:
    title=''   #line
    lablex='' # Enabler
    labley='' # Threshhold

#========================================================
    def __init__(self,title,lablex,labely ):    #W- weights   E - enabler  T- Theshold
            self.title=title   #line
            self.lablex=lablex # Enabler
            self.labley=labely # Threshhold
            return
#-------------------------------------------------------
#-------------------------------------------------------
    def plot(self,X1,X2,W):  # x -INPUT

        plt.figure(num='CLASSIFIERS')
        plt.scatter(X1, X2, color='blue')
        plt.xlabel('X1-axis')
        plt.ylabel('X2-axis')
        plt.axvspan(-0.01, 0.01, color='red', alpha=0.5)
        plt.axhspan(-0.01, 0.01, color='red', alpha=0.5)
        plt.axis('equal')
        plt.grid(True)

        intercept = 0
        W=[ 0.8 , -0.5]
        slope=-W[0]/W[1]
        xa=np.linspace(-1, 1, num=20)

        line = slope * xa + intercept
        plt.plot(xa, line, color='black', label=self.title , linestyle='dotted')

        plt.show()


        return
#-------------------------------------------------------

#----------------------------------------------------------------------------
##===========================================================================
##=  Testing Peceptron_Vizalization
##===========================================================================

if __name__ == '__main__':
    print("============================================")
    print("perceptron   Vizalization")
    print("=============================================")

    X01=[0.3,-0.6,-0.10,0.10]
    X02=[0.7,0.3,-0.80,-0.45]
    Y1=[1,0,0,1]

    W0=[ 0.8 , -0.5]
    neuron=perceptron_visualization('PERCEPTRON','X1','X2')
    neuron.plot(X01,X02,W0)



