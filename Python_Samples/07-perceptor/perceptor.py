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



class perceptron:

    ##  Class variables: This variable is shared between all objects of a class
    ## command history and command latest
    W=[1,+1]    #line
    E=0 # Enabler
    T=0 # Threshhold
    # X >> W.X >> SUM(W.X) >> E*SUM(W.X) = u >> Fthreshold(u)= Y1 >> Y1

    #========================================================
    def __init__(self,W,E,T ):    #W- weights   E - enabler  T- Theshold

            self.W=W   #line
            self.E=E # Enabler
            self.T=T # Threshhold

            return
#-------------------------------------------------------
#-------------------------------------------------------
    def predict(self,X1,X2):  # x -INPUT

        npX1=np.array(X1)
        npX2=np.array(X2)

        # weighted input
        npWX =npX1*self.W[0]+ npX2*self.W[1]
        # weighted input x Enabler
        npWX = npWX * self.E

        print("Predict: Weighted input: ",npWX)

        O = list(map(lambda i: self.sigmoid(i,self.T), npWX))
        O1=list(O)

        print("Predict: Output: ",O1)

        return O1
#-------------------------------------------------------
    def learn(self, X , Y):  # X -INPUT   Y Output



        return
#-------------------------------------------------------
# Theshold function
# threshold function set at the origin produces an output y,
    def sigmoid(self, u,threshold):  # u -scalar INPUT   y scalar Output

            if (u > threshold):
                Y=1
            if (u < threshold):
                Y=0
            if (u == threshold):
                Y=1
##            print(Y)
            return Y

#----------------------------------------------------------------------------
##===========================================================================
##=  Testing Peceptron
##===========================================================================

if __name__ == '__main__':

    import sys
    sys.path.append('C:/Users/sesa237770/Documents/Mathbox/Python_Samples/07-perceptor')
    from perceptron_visualization import perceptron_visualization

    mode=2  # 1 ="prediction" 2 ="training"

    if mode==1 :
        print("============================================")
        print("perceptron   Prediction")
        print("=============================================")

        W0=[ 0.8 , -0.5]
        WT=[ 1.05 , 0.025]  # Traind weights
        E=1
        T=0   ## if u > 0  if u <0 if u = 0   ????
        X1=[0.3,-0.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]

        W= W0

        print("X1=",X1)
        print("X2=",X2)
        print("W=",W , "(Chosen Weight vector Wi )")
        print("\n")

        neuron01=perceptron(W,E,T)
        O1=neuron01.predict(X1,X2)
        print("\nNeuron Output=",O1)

    if mode==2 :

        print("============================================")
        print("perceptron   Training")
        print("=============================================")


        W0=[ 0.8 , -0.5]
        WT=[ 1.05 , 0.025]

        W= W0
        X1=[0.3,-0.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]
        Y1=[1,0,0,1]

        neuronview=perceptron_visualization('PERCEPTRON','X1','X2')
        neuronview.plot(X1,X2,W)


        print("X1=",X1)
        print("X2=",X2)
        print("Y1=",Y1)
        W0=[ 0.8 , -0.5]
        E=1
        T=0
        beta=0.1   # A error gradient type number

        neuron01=perceptron(W0,E,T)
        Y=neuron01.predict(X1,X2)

        print("\nNeuron Output=",Y)

        npX1=np.array(X1)
        npX2=np.array(X2)
        npY1=np.array(Y1)
        npY=np.array(Y)
        npW=np.array(W0)

## three error conditions  0 1 -1
        ERROR= npY1 - npY
        E=beta*ERROR
        DeltaW= W0 + E[0]*beta

        print("\nError=",ERROR)



