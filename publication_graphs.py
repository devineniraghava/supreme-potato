# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:16:35 2024

@author: rdevinen
"""
# https://github.com/frankligy/python_visualization_tutorial
# load package
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
# print(mpl.rcParams.keys) # prints all the defaut setttigns of plots
# full list of parameters is available at https://github.com/frankligy/python_visualization_tutorial/blob/main/rcParams.txt

# any parameters can be changed using the following syntax

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

# Reset all parameters to their defaults
# mpl.rcParams.update(mpl.rcParamsDefault)

#%%
#create a canvas with width and height
fig = plt.figure(figsize=(10,6) , num='Learning Figure')

# create an axes with anchor point, left bottom corner (0.1,0.1), 
# and the size parameters (0.5,0.8)
ax  = plt.axes((0.1,0.1,0.5,0.8))
# print default figsize
mpl.rcParams['figure.figsize']

# get rid of the spines of this figure
# locate ax.spines object and set them invisible.
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

#  play with the x-axis ticks and tick labels
ax.tick_params(axis='x',which='major',direction='out',length=10,width=5,
               color='red',pad=15,labelsize=15,labelcolor='green',
               labelrotation=15)

# In addition to change the format, 
# you can change the tick and tick label themself as well
ax.set_xticks([0.2,1])
ax.set_xticklabels(['pos1','pos2'])

# every 0.5 unit interval will have a major tick
ax.yaxis.set_major_locator(MultipleLocator(0.5))
# every 0.1 unit interval will have a minor tick
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

a=ax.yaxis.get_major_locator()
b=ax.yaxis.get_major_formatter()

ax.grid(True,which='major',axis='both',alpha=0.3)

c = ax.get_xticks()
d = ax.get_xticklabels()

fig.show()

# continue here
# https://towardsdatascience.com/making-publication-quality-figures-in-python-part-i-fig-and-axes-d86c3903ad9b













#%%













#%%