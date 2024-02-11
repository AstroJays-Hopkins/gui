import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

pltInterval = 1
plt.rcParams["font.family"] = "monospace" 


#unimportant to understand - simply put it creates the dummy functions that we are graphing
# arange inits t a an array of values between 0.01 and 5.0 iterating by 0.01
t = np.arange(0.01, 5.0, 0.01)
#graphing different sin functions over the established t range
ss1 = np.sin(2 * np.pi * t) 
ss2 = np.sin(3 * np.pi * t)
ss3 = np.sin(4 * np.pi * t)
# ss4 = np.sin(5 * np.pi * t)
ss4 = [0]
yy = [ss1,ss2,ss3,ss4] # format an array of these functions

#DUMMY INPUT ARRAY
inp = [0,0,0,0,0] # [vel, alt, gps_x,gps_y,status]


#Formatting data for graphs
color = ['r', 'g', 'b', 'y'] 
title = ['Flight Path', 'Acceleration Curve', 'Compass Heading', 'Text Readouts:']
x_axis = ['Altitude (meters)',"Velocity (m/s)", '', 'Detector Output']
y_axis = ['Time', 'Time','','']

#init the subplot space (creates a 2 by 2 set of subplots)
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=False, figsize = (9,6))

#SETTINGS
#manage settings figure wide
fig.tight_layout(h_pad=4,w_pad=3) #controls the spacing between the subplots


#manage settings subplot wide
axs[1,0].remove()
axs[1,0] = fig.add_subplot(223,projection='polar')
axs[1,0].set_theta_zero_location("N")
axs[1,0].set_theta_direction(-1)
axs[1,1].set_axis_off()




#init the display data of each of the subplots

for k,(ax,y) in enumerate(zip(axs.flat,yy)):
	ax.set_xlabel(y_axis[k], fontsize=12)
	ax.set_ylabel(x_axis[k], fontsize=12)
	ax.set_title(title[k], fontsize=14)

status_map = ["ThE rOcKeT iS On FIRE", "   ReAdY tO LaUNcH   ", "     NoT pRiMeD      ", "        pRiMeD       ", "       LiFToFf       ", "       aPoGEe        ", "sEcOnD dEpLoY: [PYRO]"]


#helper function to return the current status warning of the rocket as text
def get_status():
	# return status_map[inp[4]]
	return status_map[random.randint(0,6)]

def get_alt():
	alt = random.random()
	alt = round(alt,5)
	alt = str(alt)
	while len(alt) <= 20:
		alt = " " + alt + " "
	if len(alt) == 20:
		alt = alt + " "
	return alt

#helper function that manages plotting a one of the sub plot curves
def curve_sub_plot(ax,i,y,k):
	ax.plot(t[:i], y[:i], color=color[k], linestyle='--') #for a given subplot pull data from the demo functions

#helper function for funcAnimation that will update each of the subplots
def update(i):
	for k,(ax,y) in enumerate(zip(axs.flat,yy)):
		if k != 3:
			curve_sub_plot(ax,i,y,k)
	for text in axs[1,1].texts:
		text.remove()
	axs[1,1].text(.5,.2,get_status(), size=14, rotation=0.,
				ha="center", va="center",
       			bbox=dict(boxstyle="sawtooth",
                ec=(1., 0.5, 0.5), 
                fc=(1., 0.8, 0.8),pad = 1))
	axs[1,1].text(.5,.8,get_alt(), size=14, rotation=0.,
				ha="center", va="center",
       			bbox=dict(boxstyle="sawtooth",
                ec=(1., 0.5, 0.5), 
                fc=(1., 0.8, 0.8),pad = 1))



#main code to actually run the live animation
anim = FuncAnimation(fig, update, interval=pltInterval)
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()