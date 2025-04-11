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
    W=[1,+1, 0]    #line  X1 X2 X0   W1.x1 +W2.x2 + W0 = 0
    Enabler= 1

    # X >> W.X >> SUM(W.X) >> E*SUM(W.X) = u >> Fthreshold(u)= Y1 >> Y1

    #========================================================
    def __init__(self,W,Theshold ):    #W- weights   E - enabler  ' not used T- Theshold

        self.W=W   #line
        self.Theshold=Theshold # Theshold

        return
#-------------------------------------------------------
#-------------------------------------------------------
    def predict(self,X1,X2):  # x -INPUT
        npX1=np.array(X1)
        npX2=np.array(X2)
        # weighted input
        npWX =npX1*self.W[0]+ npX2*self.W[1] + self.W[2]  #self.W[2] = bias
        WX = npWX.tolist()
        print("debug.predict: Weighted input WX[i]=")
        print(npWX)
        print("debug.predict: Weighted input WX[i]=")
        print(npWX)

        Y1 = [self.sigmoid(x,self.Theshold) for x in WX]

        return Y1
#-------------------------------------------------------
    def predictverbose(self,X1,X2,W):  # x -INPUT
        npX1=np.array(X1)
        npX2=np.array(X2)
        # weighted input
        npWX =npX1*W[0]+ npX2*W[1]+ W[2]  #self.W[2] = bias
        WX = npWX.tolist()
        print("debug.predict: Weighted input WX[i]=")
        print(npWX)
        Y1 = [self.sigmoid(x,self.Theshold) for x in WX]
        return Y1
#-------------------------------------------------------
    def learn(self, X1,X2 , Y1, W0, Enabler, beta ):  # X -INPUT   Y Output

        print("============================================")
        print("ITTERATION")
        print("=============================================")
        print("Initial Parameters W[W1,W2,W0] Enabler")
        print(W0, " / ",Enabler," / ", beta)

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
            Y=self.predictverbose(X1,X2,W)
            npY=np.array(Y)
            npW=np.array(W)
            ## Update the weights and bias using the following formulas:
            ## w=w+α⋅error⋅x and b=b+α⋅error, where α is the learning rate.

##            ERROR= npY1[i] - npY[i]   ## three error conditions  0 1 -1
            if npY1[i] == npY[i]:
                ERROR=0
            if npY1[i] > npY[i]:
                ERROR=1
            if npY1[i] < npY[i]:
                ERROR=-1
            # 1  -1
            # 1  1
            # -1 1
            # 0 0

            #(1-1)
##            Err=ERROR.item()
            Err=ERROR
            DeltaW=  [X1[i]*beta*Err ,X2[i]*beta*Err , +1*beta*Err]
            W=npW.tolist()
            W=np.add(W,DeltaW)
            print("X1=",X1[i]," X2=",X2[i]," Y1=",Y1[i]," Yp=",Y[i])
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
                Y=threshold
            if (u < threshold):
                Y=-threshold
            if (u == threshold):
                Y=0
##            print("debug.sigmoid: u=",u, "Y=",Y," threshold=",threshold)
            return Y

#----------------------------------------------------------------------------
##===========================================================================
##=  Testing Peceptron
##===========================================================================

if __name__ == '__main__':

    import sys
    sys.path.append('C:/Users/sesa237770/Documents/Mathbox/Python_Samples/07-perceptor')
    from CAX_perceptron_visualization import perceptron_visualization

    mode=1  # 1 ="prediction" 2 ="training"

    mode = int(input("1 = prediction  2 = training : "))

    if mode==1 :
        print("============================================")
        print("perceptron   Prediction")
        print("=============================================")

        W0=[ 0.8 , -0.5,0]
        WT=[ 1.05 , 0.025,0]  # Traind weights
        Threshold=0
        X1=[0.3,-0.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]

        Yt=[1,-1,-1,1] # trained output

        W= WT

        print("X1=",X1)
        print("X2=",X2)
        print("W=",W , "(Chosen Weight vector Wi )")
        print("\n")

        neuron01=perceptron(W,Threshold)
        Y=neuron01.predict(X1,X2)
        print("\nNeuron Output=",Y)
        print("\nTrained Output=",Yt)

    if mode==2 :

        print("============================================")
        print("perceptron   Training")
        print("=============================================")
        W0=[ 0.8 , -0.5,0]   # Random
##        W0=[0.85 , 0.275,0]  # With initial learning
        X1=[0.3,-.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]
        Y1=[1,-1,-1,1]

        W0=[ 0.8 , 1,-1.4]   # Random
##        W0=[0.85 , 0.275,0]  # With initial learning
##        W0=[0.64, 0.6,  0.2 ]
        W0=[2.56, 2.68, 0.2 ]

        X1=[0.2,0.2,0.8,1]
        X2=[0.3,0.8,0.2,0.8]
        Y1=[-1,-1,-1,1]

        Threshold=0
        beta=0.8 # A error gradient type number

        print("X1[i]=",X1)
        print("X2[i]=",X2)
        print("Y1[i]=",Y1)
        print("beta=",beta)

        neuron01=perceptron(W0,Threshold)
        W  = neuron01.learn(X1,X2 ,Y1,W0,Threshold, beta )
        print("W_final[i]=",W )

        print("============================================")
        print("perceptron   Training COMPLETE")
        print("=============================================")

        neuronview=perceptron_visualization('PERCEPTRON','X1','X2')
        neuronview.plot(X1,X2,Y1,W0,W)



