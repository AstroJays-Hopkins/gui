import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pltInterval = 1

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

#create polar graph subplot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#plot first set of data
ax.plot(theta, r)

#update method for Animation
def update(i):
    #Plot arbitrarily modified data
	ax.plot(theta, r + i, color='r', linestyle='--')

#ax.set_rmax(2) --> unnecessary, maybe? but in documentation
ax.set_rticks([0.5, 1, 1.5, 2])  # Set the amount of radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
#ax.grid(True) --> also potentially unnecessary

#graph title
ax.set_title("A line plot on a polar axis", va='bottom')

#animation function & updating graph
anim = FuncAnimation(fig, update, interval=pltInterval)
plt.show()