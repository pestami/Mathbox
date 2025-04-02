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
    Enabler=0 # Enabler
    Threshold=0 # Threshhold
    bias=0
    # X >> W.X >> SUM(W.X) >> E*SUM(W.X) = u >> Fthreshold(u)= Y1 >> Y1

    #========================================================
    def __init__(self,W,Enabler,Threshold,bias ):    #W- weights   E - enabler  T- Theshold

        self.W=W   #line
        self.Enabler=Enabler # Enabler
        self.Threshold=Threshold # Threshhold
        self.bias=bias
        return
#-------------------------------------------------------
#-------------------------------------------------------
    def predict(self,X1,X2):  # x -INPUT

        npX1=np.array(X1)
        npX2=np.array(X2)

        # weighted input
        npWX =npX1*self.W[0]+ npX2*self.W[1]
        # weighted input x Enabler
        npWX = npWX * self.Enabler

        print("Weighted input WX[i]=")
        print(npWX)

        O = list(map(lambda i: self.sigmoid(i,self.Threshold), npWX))
        O1=list(O)

        print("Predict Y[i]=")
        print(O1)

        return O1
#-------------------------------------------------------
    def predictverbose(self,X1,X2,W,Enabler,Threshold,bias  ):  # x -INPUT

        npX1=np.array(X1)
        npX2=np.array(X2)

        # weighted input
        npWX =npX1*W[0]+ npX2*W[1]
        # weighted input x Enabler
        npWX = npWX * Enabler  # + bias

##        print("Weighted input WX[i]=")
##        print(npWX)
        O = list(map(lambda i: self.sigmoid(i,Threshold), npWX))
        O1=list(O)

##        print("Predict Y[i]=")
##        print(O1)

        return O1
#-------------------------------------------------------
    def learn(self, X1 , Y1,W0,Enabler,Threshold,bias ):  # X -INPUT   Y Output

        print("============================================")
        print("ITTERATION")
        print("=============================================")
        print("Initial Parameters W[W1,W2] Enabler,Threshold")
        print(W0,Enabler,Threshold)

        for i in range(len(X1)):
##        for i in range(2):

            if i==0:
                W=W0
                npX1=np.array(X1)
                npX2=np.array(X2)
                npY1=np.array(Y1)   # Learning Expected Values

            print("---------------------------------------")
            print("Iterration=",i)
##            print("DEBUG Call: predictfull:")
            Y=neuron01.predictverbose(X1,X2,W,Enabler,Threshold,bias)
            npY=np.array(Y)
            npW=np.array(W)

            ERROR= npY1[i] - npY[i]   ## three error conditions  0 1 -1
            Err=ERROR.item()
            DeltaW=  [X1[i]*beta*Err ,X2[i]*beta*Err ]
            W=npW + DeltaW

            print("Error---- Output=",ERROR)
            print("DeltaW--- Output=",DeltaW)
            print("Wnew[i]-- Output=",W)
        print("---------------------------------------")

        return W
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
        Enabler=1
        Threshold=0   ## if u > 0  if u <0 if u = 0   ????
        bias=0
        X1=[0.3,-0.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]

        W= W0

        print("X1=",X1)
        print("X2=",X2)
        print("W=",W , "(Chosen Weight vector Wi )")
        print("\n")

        neuron01=perceptron(W,Enabler,Threshold,bias )
        O1=neuron01.predict(X1,X2)
        print("\nNeuron Output=",O1)

    if mode==2 :

        print("============================================")
        print("perceptron   Training")
        print("=============================================")
        W0=[ 0.8 , -0.5]
        WT=[ 1.05 , 0.025]
        Enabler=1
        Threshold=0   ## if u > 0  if u <0 if u = 0   ????
        bias=0

        W= W0
        X1=[0.3,-0.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]
        Y1=[1,0,0,1]

        print("X1[i]=",X1)
        print("X2[i]=",X2)
        print("Y1[i]=",Y1)

        W0=[ 0.8 , -0.5]
        Enabler=1
        Threshold=0
        beta=0.5   # A error gradient type number

        neuron01=perceptron(W0,Enabler,Threshold,bias)
        W= neuron01.learn(X1 ,Y1,W,Enabler,Threshold,bias )
        print("W_final[i]=",W)

        print("============================================")
        print("perceptron   Training COMPLETE")
        print("=============================================")

        neuronview=perceptron_visualization('PERCEPTRON','X1','X2')
        neuronview.plot(X1,X2,W0,W)


