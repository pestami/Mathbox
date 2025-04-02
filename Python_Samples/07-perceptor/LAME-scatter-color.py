#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     01.04.2025
# Copyright:   (c) SESA237770 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# Create a scatter plot with colored points
plt.scatter(x, y, c=z, cmap='viridis')

# Add title and labels
plt.title('Scatter Plot with Colored Points')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
np.random.seed(0)
x = np.random.rand(10)
y = np.random.rand(10)
categories = np.random.choice(['A', 'B', 'C'], 10)

# Create a dictionary to map categories to colors
color_map = {'A': 'red', 'B': 'green', 'C': 'blue'}

# Create a scatter plot with colored points
c=[color_map[category] for category in categories]

#c=[1, 2, 3,1], cmap='viridis'

plt.scatter(x, y, c,cmap='viridis' )

# Add title and labels
plt.title('Scatter Plot with Colored Points')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
