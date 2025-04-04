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

from CAX_perceptron import perceptron
import sys
sys.path.append('C:/Users/sesa237770/Documents/Mathbox/Python_Samples/07-perceptor')
from CAX_perceptron_visualization import perceptron_visualization

if __name__ == '__main__':


##============================================================================
##============================================================================

    print("============================================")
    print("perceptron Definition")
    print("--------------------------------------------")

    mode=2 # 2 Training 1 Prediction

    W0=[ 0.8 , 0.5, 0.1]
##    WT=[ 1.05 , 0.025]  # Traind weights
    Enabler=1
    Threshold=0   ## if u > 0  if u <0 if u = 0   ????
    bias=0

    Example=1

    Example = int(input("Enter Example to Perform 1...3 : "))

    #EXAMPLE 1
    if Example==1:
        W0=[ 0.8 , 0.5, 0.1]  # Random bias=0.1
        W0=[0.85 , 0.275, 0.1] # With initial learning


        X1=[0.3,-.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]

        X1=[0.3,-.6,-0.10,0.10]
        X2=[0.7,0.3,-0.80,-0.45]

        Y1=[1,-1,-1,1]
        Threshold=0   ## if u > 0  if u <0 if u = 0   ????

    #EXAMPLE 2
    if Example==2:
        W0=[ 0.8 , -0.5, 0.1]   # Random bias=0.1
        X1=[0.2,0.2,0.8,1.0]
        X2=[0.3,0.8,0.2,0.8]
        Y1=[-1,-1,-1,1]
        Threshold=0   ## if u > 0  if u <0 if u = 0   ????

    #EXAMPLE 3
    if Example==3:
        W0=[ 0.8 , -0.5, 0.1]  # Random bias=0.1
        W0=[0.85,  0.275, 0.1  ]
        X1=[0.2,0.2,0.8,1.0,0.2,0.2,0.8,1.0]
        X2=[0.3,0.8,0.2,0.8,0.3,0.8,0.2,0.8]
        Y1=[-1,-1,-1,1,-1,-1,-1,1]

        Threshold=0   ## if u > 0  if u <0 if u = 0   ????

    print("============================================")
    print("perceptron   Training")
    print("--------------------------------------------")
    beta=0.2   # A error gradient type number
    W= W0
    print("X1=",X1)
    print("X2=",X2)
    print("Threshold=",Threshold)
    print("W=",W , "(Chosen Weight vector Wi )")
    print("\n")
##============================================================================
##============================================================================

##============================================================================
##============================================================================
    if mode==2 :
        print("============================================")
        print("perceptron   Training, Example=" , Example)
        print("--------------------------------------------")

        neuron01=perceptron(W0,Threshold)
        W = neuron01.learn(X1,X2 ,Y1,W,Enabler,beta )
        print("W_final[i]=",W)


        print(".............................................")
        print("perceptron   Training COMPLETE")
        print("=============================================")

        neuronview=perceptron_visualization('PERCEPTRON','X1','X2')
        neuronview.plot(X1,X2,Y1,W0,W)
##============================================================================
##============================================================================
    if mode==1 :
        neuron01=perceptron(W,Threshold )
        O1=neuron01.predict(X1,X2)
        print("\nNeuron Output=",O1)
##============================================================================
##============================================================================
