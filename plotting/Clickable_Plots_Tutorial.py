#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:39:24 2021

@author: simon
"""
#%% Imports
import matplotlib.pyplot as plt
import numpy as np
import functools # needed to create the on click wrapper


#%% Example 1- Simple
# This definition will be called everytime you click, the last argument is the click "event"
def onclick(fig, axis, event):
    ix, iy= event.xdata, event.ydata # Collect the click co-ordinates
    axis.scatter(ix, iy, color='red', marker='d') #scatter the location of the click
    plt.draw() #makes the scatter show
    return
fig= plt.figure(num= 'Example 1')
ax= fig.add_subplot(111)
x, y= np.random.uniform(-100, 100, size=1000), np.random.uniform(-100, 100, size=1000)
ax.scatter(x, y)
onclick_wrapper=functools.partial(onclick, fig,  ax) # Create the wrapper
cid = fig.canvas.mpl_connect('button_press_event', onclick_wrapper) # Attach it to the click function in the figure

#%% Example 2- What if we have more than one subplot in the figure?

# This definition will be called everytime you click, the last argument is the click "event"
def onclick(fig, axis, event):
    if axis.in_axes(event): # check if the event is in the subplot provided
        ix, iy= event.xdata, event.ydata # Collect the click co-ordinates
        axis.scatter(ix, iy, color='red', marker='d') #scatter the location of the click
        plt.draw() #makes the scatter show
    return
fig2= plt.figure(num= 'Example 2')
ax2= fig2.add_subplot(121)
ax3= fig2.add_subplot(122)
x, y= np.random.uniform(-100, 100, size=1000), np.random.uniform(-100, 100, size=1000)
ax2.scatter(x, y)
onclick_wrapper=functools.partial(onclick, fig2,  ax2) # Create the wrapper
cid = fig2.canvas.mpl_connect('button_press_event', onclick_wrapper) # Attach it to the click function in the figure

#%% Example 3- What if we want to do different things depending on which subplot we click in

# This definition will be called everytime you click, the last argument is the click "event"
def onclick(fig, axis, axis2, event):
    if axis.in_axes(event): # check if the event is in the subplot provided
        ix, iy= event.xdata, event.ydata # Collect the click co-ordinates
        axis.scatter(ix, iy, color='red', marker='d') #scatter on first subplot
        plt.draw() #makes the scatter show
    elif axis2.in_axes(event):
        ix, iy= event.xdata, event.ydata
        axis2.scatter(ix, iy, color='green', marker='h') #scatter on second subplot
        plt.draw()
    return
fig3= plt.figure(num= 'Example 3')
ax4= fig3.add_subplot(121)
ax5= fig3.add_subplot(122)
x, y= np.random.uniform(-100, 100, size=1000), np.random.uniform(-100, 100, size=1000)
ax4.scatter(x, y)
x, y= np.random.uniform(-100, 100, size=1000), np.random.uniform(-100, 100, size=1000)
ax5.scatter(x, y)
onclick_wrapper=functools.partial(onclick, fig3,  ax4, ax5) # Create the wrapper
cid = fig3.canvas.mpl_connect('button_press_event', onclick_wrapper) # Attach it to the click function in the figure

#%% Example 4- If we're doing the same thing on all the subplots you pass into the function

# This definition will be called everytime you click, the last argument is the click "event"
def onclick(fig, axes, event):
    bools= np.array([axis.in_axes(event) for axis in axes]) #Has True for which subplot the click is in
    if any(bools):
        axis= np.array(axes)[bools][0] # Select the axis
        ix, iy= event.xdata, event.ydata # Collect the click co-ordinates
        axis.scatter(ix, iy, color='purple', marker='p')
        plt.draw() #makes the scatter show
    return
fig4= plt.figure(num='Example 4')
gs=fig4.add_gridspec(10, 10,
                     wspace=0, hspace=0)
axes= [fig4.add_subplot(i) for i in gs]
onclick_wrapper=functools.partial(onclick, fig4,  axes) # Create the wrapper
cid = fig4.canvas.mpl_connect('button_press_event', onclick_wrapper) # Attach it to the click function in the figure