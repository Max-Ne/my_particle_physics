# pretty basic

import random
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.patches import Circle


random.seed(1)
N=10000
below=0

xdata = []
ydata = []

plt.show()

fig, axes = plt.subplots(figsize=(6,6))
axes.set_xlim(0,1)
axes.set_ylim(0,1)

line, = axes.plot(xdata, ydata, 'r.')

# draw the circle
circle = Circle((0,0),1,facecolor='none')
axes.add_patch(circle)

# every iteration for one additional point
for i in range(N):

  xdata.append(random.uniform(0,1))
  ydata.append(random.uniform(0,1))

  if ((np.sqrt(xdata[-1]**2 + ydata[-1]**2)) < 1.): below+=1

  line.set_xdata(xdata)
  line.set_ydata(ydata)
  
  plt.draw()
  plt.pause(1e-17)

  # quarter circle: 1/4 pi * r * r
  if (i%100 == 0): print 4*float(below)/(i+1)

print 4*float(below)/(i+1)
plt.show()
