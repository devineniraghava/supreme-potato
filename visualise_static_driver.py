# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:24:21 2023

@author: rdevinen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:25:15 2023

@author: rdevinen
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

#from plot_functions import plot_openstreet

#%%


ds = xr.open_dataset(
    "C:/Users/rdevinen/Downloads/campus_gui_24_static", engine="netcdf4")

# ds['zt'] = ds['zt'].where(ds['zt'] != 65535, 155)

print(ds.data_vars)

fig1, ax1 = plt.subplots()



ds["zt"].plot(cmap='rainbow', robust=True, ax = ax1, label='Inline label'); #new
ax1.set_title("Static Driver")
plt.show()

# ds.to_netcdf("C:/Users/rdevinen/Downloads/campus_gui_24_static_2")
ds.close()
#%%
ds.close()

#%% Edit static driver
# edit in such a way that it it not detected by palm
import netCDF4 as nc
with nc.Dataset('C:/Users/rdevinen/Downloads/campus_gui_24_static', 'r+') as ncfile:
    # Access the variable you want to modify
    variable = ncfile.variables['zt']

    # Access the fill value
    fill_value = variable._FillValue

    # Retrieve the data as a NumPy array
    data = variable[:]

    # Modify the data as needed
    data[data >= 200] = 152

    # Update the variable with the modified data
    variable[:] = data
















#%%





























