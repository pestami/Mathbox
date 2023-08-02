#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     18.07.2023
# Copyright:   (c) SESA237770 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


## For most practical purposes, you can think of the conditional block that you open
## with if __name__ == "__main__"
## as a way to store code that should only run when your file is executed as a script.

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import numpy as np

# @ jumbo mirror = 1000 x 500
Xmax=450  # mirror X size
Ymax=500  # mirror Y size
Lmax=500  # mirror Y size

# Parabola; y = a(b+x)**2 + c
# a= Y/(X**2)
# b = Xmax/2

a=round(Ymax/Xmax/Xmax,5)   # a= +/- 0.05
c =0
b=Xmax/2

Yfocus=round(c+ 1/a/4,1)
Xfocus=b

print('====Calculating Parabola constraints======')
print('\n Equation=' +"a(X + b)^2 + c")
print('a=' + str(a))
print('b=' + str(b))
print('c=' + str(c))

print(' Equation= ' + str(a)+"(X + "+ str(b)+")^2"+ str(c))
print(' Y Focus = ' + str(Yfocus))

print('\n==========================================')

x = np.linspace(0, Xmax, 10)
##y = np.sin(x)
y = a*(x-b)**2 + c

x2=np.linspace(0.9*Xmax/2,  1.1*Xmax/2, 10)
y2 = Yfocus + 0*x


print('\n===========================================')
# import scipy.integrate.quad
from scipy import integrate
arcLength = lambda x: np.sqrt(1+  (2*a*x-2*a*b)**2)


# using scipy.integrate.quad() method
geek = integrate.quad(arcLength, 0, Xmax)

##print(geek)

print('\n===Calculating arc Length of Parabola=====')
Larc=round(geek[0],0)
print('arc Length=' + str(Larc) +" mm")
print('==========================================')
print('=========Arc Coordinates ===========')

print(x)
print(y)
## xy = np.meshgrid(x,y)

xy =np.array([[X1, Y1] for X1 ,Y1 in zip(x,y)])
print(xy)

print('==========================================')


fig, ax = plt.subplots()
ax.plot(x, y,'r')
ax.plot(x2, y2, 'g')

ax.annotate('Focus Y= '+ str(Yfocus), xy=(Xfocus, Yfocus), xytext=(100, 400), arrowprops=dict(facecolor='black', shrink=0.05),      )

ax.annotate('Arc Length =' + str(Larc) +" mm",
            xy=(.025, .975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

ax.set_xlim([0, 500])
ax.set_ylim([0, 500])

print('==========================================')

print('==========================================')

##ax.plot(100,100)
##plt.show()
##plt.show(block=True)

