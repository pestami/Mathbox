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
    def plot(self,X1,X2,Y1,W0,W):  # x -INPUT

        npY1=np.array(Y1)

        color_map = {0: 'red', 1: 'green'}
        C=[color_map[Y] for Y in Y1]



        plt.figure(num='CLASSIFIERS')
        #plt.scatter(X1, X2, color='blue')
        plt.scatter(X1, X2, color=C)

        plt.xlabel('X1-axis')
        plt.ylabel('X2-axis')
        plt.axvspan(-0.01, 0.01, color='red', alpha=0.5)
        plt.axhspan(-0.01, 0.01, color='red', alpha=0.5)
        plt.axis('equal')
        plt.grid(True)

        intercept = 0
        slope=-W0[0]/W0[1]
        xa=np.linspace(-1, 1, num=20)

        line = slope * xa + intercept
        plt.plot(xa, line, color='grey' , label=self.title, linestyle='dotted')

        intercept = 0
        slope=-W[0]/W[1]
##        xb=np.linspace(-1, 1, num=20)

        lineb = slope * xa + intercept
        plt.plot(xa, lineb, color='green', label=self.title , linestyle='-')

        slopep1, intercept = np.polyfit(X1, X2, 1)
        linep1 = slopep1 * xa + intercept
        plt.plot(xa, linep1, color='red', label=self.title , linestyle='dotted')

##        slopep2, intercept = np.polyfit(X2, X1, 1)
##        linep2 = slopep2 * xa + intercept
##        plt.plot(xa, linep2, color='orange', label=self.title , linestyle='dotted')

##        plt.xlim(min(X1)- 0.05*min(X1), max(X1)+ 0.05*max(X1))  # sets the x-axis limits to (2, 8)
##        plt.ylim(min(X2)- 0.05*min(X2), max(X2)+ 0.05*max(X2))  # sets the y-axis limits to (-1.5, 1.5)

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
    W=[1.05 , 0.25]

    neuron=perceptron_visualization('PERCEPTRON','X1','X2')
    neuron.plot(X01,X02,Y1,W0,W)



