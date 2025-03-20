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

class perceptron_v01:

    ##  Class variables: This variable is shared between all objects of a class
    ## command history and command latest
    W=[1,+1]    #line
    E=1 # Enabler
    T=1 # Threshhold
    # X >> W.X >> SUM(W.X) >> E*SUM(W.X) = u >> Fthreshold(u)= Y1 >> Y1

    #========================================================
    def __init__(self,W,E,T ):    #W- weights   E - enabler  T- Theshold

        return
#-------------------------------------------------------
#-------------------------------------------------------
    def predict(self,X1,X2):  # x -INPUT

        npX1=np.array(X1)
        npX2=np.array(X2)

        # weighted input
        npWX =npX1*W[0]+ npX2*W[1]
        # weighted input x Enabler
        npWX = npWX * E

        print("Predict: Weighted input: ",npWX)

        O = list(map(lambda i: self.sigmoid(i,T), npWX))
        O1=list(O)

        print("Predict: Output: ",O1)

        return O1
#-------------------------------------------------------
    def learn(self, X , Y):  # X -INPUT   Y Output



        return
#-------------------------------------------------------
# Theshold function
    def sigmoid(self, u,threshold):  # u -INPUT   Y Output

            if (u > threshold):
                Y=1
            if (u < threshold):
                Y=0
            if (u == threshold):
                Y=1
##            print(Y)
            return Y

#-----------------------------a-----------------------------------------------


if __name__ == '__main__':


    print("============================================")
    print("perceptron_v01")
    print("=============================================")

    W=[ 0.8 , -0.5]
##    W=[ 1.05 , 0.025] # Traind weights

    E=1
    T=0

    neuron01=perceptron_v01(W,E,T)

    X1=[0.3,-0.6,-0.10,0.10]
    X2=[0.7,0.3,-0.80,-0.45]

    print("X1=",X1)
    print("X2=",X2)
    print("W=",W)

    print("\n")

    O1=neuron01.predict(X1,X2)
    print("\nNeuron Output=",O1)

