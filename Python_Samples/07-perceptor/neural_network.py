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
# from array import array






#===============================================================================
# PANDAS required ?
#===============================================================================

if __name__ == '__main__':

    W=[0.5,-0.3]
    X1=[2,3,4,1]
    X2=[4,7,9,2]


 

  
# # Create a scatter plot
# plt.scatter(X1, X2, color='blue')
# plt.xlabel('X1-axis')
# plt.ylabel('X2-axis')
# plt.title('McCulloch-Pitts.Perceptron')
# plt.show()




# Calculate the line of best fit
slope, intercept = np.polyfit(X1, X2, 1)

xline=np.array('i',X1)   # i -integer

line = slope * xline + intercept

# Plot the scatter plot and line of best fit
plt.scatter(X1, X2, color='blue')

#plt.plot(x, line, color='red', label='Line of Best Fit')
plt.xlabel('X1-axis')
plt.ylabel('X2-axis')
plt.title('McCulloch-Pitts.Perceptron')
plt.legend()
plt.show()