# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:33:15 2023

@author: rdevinen
"""

import pandas as pd
import pickle
    

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go


#%% plots a web graph of measured data on open streetmap
def plot_openstreet(t = 16):
    with open('map_scatter_plot_testo_full_310.pickle', 'rb') as handle:
        map_scatter_plot_testo_full = pickle.load(handle)

    dff = map_scatter_plot_testo_full[t].copy()

    fig = px.scatter_mapbox(dff,
                            lon = 'longitude',
                            lat = 'latitude',
                        zoom = 16,
                        color = dff["temp_C"],
                        size = dff["size"],
                        width = 1200,
                        labels = {"temp_C": "Temperature °C"},
                        height = 900,
                            color_continuous_scale='Rainbow',
                        title = "Temperature between {} and {}".format(dff.index[2], dff.index[-15]),
                        range_color = [26,36]
                        )

    fig.update_layout(mapbox_style = "open-street-map")
    #fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
    fig.show()

#%%


# function to convert lat and lon to simulation coordinates
def convert_lat_lon_to_image_coords(lat, lon, min_lat = 48.45574, 
                                    min_lon = 7.93867, max_lat = 48.46050,
                                    max_lon = 7.94586):
    lat_range = max_lat - min_lat
    lon_range = max_lon - min_lon
    lat_scale_factor = 800 / lat_range
    lon_scale_factor = 800 / lon_range
    scaled_x = (lat - min_lat) * lat_scale_factor
    scaled_y = (lon - min_lon) * lon_scale_factor
    return scaled_x, scaled_y

# since simulation data dont have even coordinates we need this function
def make_odd(number):
    number = round(number)
    if number % 2 == 0:  # Check if the number is even
        return number + 1  # If even, add 1 to make it odd
    else:
        return number  # If already odd, leave it unchanged

# load measurement data
with open('map_scatter_plot_testo_full_310.pickle', 'rb') as handle:
    map_scatter_plot_testo_full = pickle.load(handle)

def plot_meas(t = 16, vmin=29, vmax=36):
    # use empty canvas to plot measurement data
    new = xr.open_dataset(
        "D:/PALM/campus_24_v1/OUTPUT/campus_24_v1_3d.000.nc", engine="netcdf4")
    
    # D:/PALM/campus_24_v1/OUTPUT/campus_24_v1_3d.000.nc
    # D:/PALM/campus_72_v1/OUTPUT/campus_72_v1_3d.000.nc
    # D:/PALM/campus_gui_24/OUTPUT/campus_gui_24_3d.000.nc
    # C:/Users/rdevinen/Downloads/campus_2_gui_24/OUTPUT/campus_2_gui_24_3d.000.nc

    a1 = new["theta"].isel(time=16, zu_3d=10).fillna(0)
    a1.loc[:] = np.nan
    new_attributes = {'units': '°C', 'long_name': 'Temperature'}
    a1.attrs.update(new_attributes)
    
    dff = map_scatter_plot_testo_full[t].copy()
    dff["x"], dff["y"] = convert_lat_lon_to_image_coords(dff.latitude, dff.longitude)

    
    for index, row in dff.iterrows():
        
        x1 = make_odd(row["x"]) - 6
        x2 = make_odd(row["x"]) + 6

        y1 = make_odd(row["y"]) - 6
        y2 = make_odd(row["y"]) + 6    
        
        
        
        a1.loc[dict(x=slice(y1,y2), y=slice(x1,x2))] = row["temp_C"]

    fig, ax = plt.subplots()
    ax.clear()
    a1.plot(  cmap='rainbow', robust=True, ax = ax, label='Temp', vmin=vmin, vmax=vmax); #new
    


    ax.set_title("Measurement data plotted for " + str(t) + ":00 Uhr" )
    #plt.savefig("plots/plot.pdf", format='pdf')
    #plt.savefig('plots/plot.svg', format='svg')
    plt.savefig('plots/plot_meas_{}.png'.format(t), format='png')
    plt.show()
    return a1



#%%

def plot_simulation(t = 16, vmin=29, vmax=36):

    new = xr.open_dataset(
            "D:/PALM/campus_24_v1/OUTPUT/campus_24_v1_3d.000.nc", engine="netcdf4")
    
    a = new["theta"].isel(time=16, zu_3d=2).fillna(0)
    a.loc[:] = np.nan
    new_attributes = {'units': '°C', 'long_name': 'Temperature'}
    a.attrs.update(new_attributes)
    
    dff = map_scatter_plot_testo_full[t].copy()
    dff["x"], dff["y"] = convert_lat_lon_to_image_coords(dff.latitude, dff.longitude)

    
    new = xr.open_dataset(
        "D:/PALM/campus_24_v1/OUTPUT/campus_24_v1_3d.000.nc", engine="netcdf4")
    
    a1 = new["theta"].isel(time=t, zu_3d=2).fillna(0)
    
    b1 = new["im_t_indoor_mean"].isel(time=t, zw_3d=2).fillna(0)
    
    c1 = (a1+b1)-273 #new
    
    
    for index, row in dff.iterrows():
        
        x = make_odd(row["x"])
        y = make_odd(row["y"])
        
        x1 = make_odd(row["x"]) - 6
        x2 = make_odd(row["x"]) + 6
    
        y1 = make_odd(row["y"]) - 6
        y2 = make_odd(row["y"]) + 6    
        
        
        
        # a.loc[dict(x=slice(y1,y2), y=slice(x1,x2))] = row["temp_C"]
        a.loc[dict(x=slice(y1,y2), y=slice(x1,x2))] = c1.loc[dict(x=slice(y1,y2), y=slice(x1,x2))]
        # a.loc[dict(x=slice(y1,y2), y=slice(x1,x2))] = c1.loc[y,x]
    
    
    fig5, ax5 = plt.subplots()
    a.plot(  cmap='rainbow', robust=True, ax = ax5, label='Inline label', vmin=vmin, vmax=vmax); #new
    ax5.set_title("Simulation data plotted for " + str(t) + ":00 Uhr")
    fig5.savefig('plots/plot_sim_{}.png'.format(t), format='png')
    plt.show()
    return a



#%%

def plot_diff(t = 16, vmin=29, vmax=36):
    diff = plot_simulation(t,vmin, vmax ) - plot_meas(t,vmin, vmax)
    new_attributes = {'units': 'K', 'long_name': 'Temperature difference'}
    diff.attrs.update(new_attributes)
    
    fig6, ax6 = plt.subplots()
    diff.plot(  cmap='rainbow', robust=True, ax = ax6, label='Inline label', vmin=-5, vmax=5)
    ax6.set_title("Simulation - Measured data plotted for " + str(t) + ":00 Uhr")
    plt.savefig('plots/diff_plot_{}.png'.format(t), format='png')

    
#%%
for i in range(25):
    plot_diff(i)
    plt.close("all")
    print(i)



































#%%
    



