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
#======================================================================


# create data
x = [10,20,30,40,50]
y = [30,30,30,30,30]

# plot line
plt.plot(x, y)
plt.show()

# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
x = [1.0,2,3,4,5]
y = [3.0,3,3,3,3]

# plot lines
plt.plot(x, y, label = "line 1", linestyle="-")
plt.plot(y, x, label = "line 2", linestyle="--")
plt.plot(x, np.sin(x), label = "curve 1", linestyle="-.")
plt.plot(x, np.cos(x), label = "curve 2", linestyle=":")
plt.legend()
plt.show()


#======================================================================

np.random.seed(0)
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)

# Create a scatter plot
plt.scatter(x, y, color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Matplotlib')
plt.show()




# Calculate the line of best fit
slope, intercept = np.polyfit(x, y, 1)
line = slope * x + intercept

# Plot the scatter plot and line of best fit
plt.scatter(x, y, color='blue')
plt.plot(x, line, color='red', label='Line of Best Fit')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Line of Best Fit')
plt.legend()
plt.show()
