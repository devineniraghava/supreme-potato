#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:25:15 2023

@author: rdevinen
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates
import pandas as pd

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
from datetime import datetime, timedelta
import pickle
#%% Plot the Whole Simulation at a specific time

path1 = "D:/PALM/campus_24_v1/OUTPUT/campus_24_v1_3d.000.nc" #campus_24_v1_3d.000
path2 =  "D:/PALM/campus_72_v1/OUTPUT/campus_72_v1_3d.000.nc" # campus_72_v1_3d.000
path3 = "D:/PALM/campus_2_gui_24/OUTPUT/campus_2_gui_24_3d.000.nc" # campus_gui_24_3d.000
path4 = "D:/PALM/campus_3_gui_24/OUTPUT/campus_3_gui_24_3d.000.nc" # campus_3_gui_24.000
t = 16



#%%% 1) Plot campus_24_v1_3d.000


new1 = xr.open_dataset(path1, engine="netcdf4")


fig1, ax1 = plt.subplots()


a1 = new1["theta"].isel(time=t, zu_3d=2,x=slice(None, None),  y=slice(None, None)).fillna(0)

b1 = new1["im_t_indoor_mean"].isel(time=t, zw_3d=2,x=slice(None, None), y=slice(None, None) ).fillna(0)

c1 = (a1+b1)-273 #new



c1.plot(  cmap='rainbow', robust=True, ax = ax1, label='Inline label'); #new
ax1.set_title("24 Hours Simulation " + str(t) + ":00 Uhr" + "Temperature °C at 2 meters height")
# fig1.savefig("New Simulation " + str(t) + ":00 Uhr.png")
plt.show()

#%%% 2) Plot campus_72_v1_3d.000


new2 = xr.open_dataset(path2, engine="netcdf4")


fig2, ax2 = plt.subplots()


a2 = new2["theta"].isel(time=t, zu_3d=2,x=slice(None, None),  y=slice(None, None)).fillna(0)

b2 = new2["im_t_indoor_mean"].isel(time=t, zw_3d=2,x=slice(None, None), y=slice(None, None) ).fillna(0)

c2 = (a2+b2)-273 #new



c2.plot(  cmap='rainbow', robust=True, ax = ax2, label='Inline label'); #new
ax2.set_title("72 Hours Simulation " + str(t) + ":00 Uhr" + "Temperature °C at 2 meters height")
# fig1.savefig("New Simulation " + str(t) + ":00 Uhr.png")
plt.show()

#%%% 3) Plot campus_gui_24_3d.000


new3 = xr.open_dataset(path4, engine="netcdf4")


fig3, ax3 = plt.subplots()


a3 = new3["theta"].isel(time=t, zu_3d=10,x=slice(None, 395),  y=slice(5, None)).fillna(0)

b3 = new3["im_t_indoor_mean"].isel(time=t, zw_3d=10,x=slice(None, 395), y=slice(5, None) ).fillna(0)

c3 = (a3+b3)-273 #new



c3.plot(  cmap='rainbow', robust=True, ax = ax3, label='Inline label'); #new
ax3.set_title("GUI Input at " + str(t) + ":00 Uhr" + "Temperature °C at 10 meters height")
# fig1.savefig("New Simulation " + str(t) + ":00 Uhr.png")
plt.show()

#%% Building Temperatures



#%%% 1) campus_24_v1_3d.000

fig4, ax4 = plt.subplots()

a1 = new1["theta"].isel(x = 216, y = 122, zu_3d=2).fillna(0)

b1 = new1["im_t_indoor_mean"].isel(x = 216, y = 122, zw_3d=2).fillna(0)

c1 = (a1+b1)-273.15 #new

ax4.plot(c1.variable)
ax4.set_title("24 Hours Simulation Indoor Temperature for C Building at" + str(t) + ":00 Uhr" )

ax4.set_ylabel('Temperature °C')
ax4.set_xlabel('Time [Hours]')

plt.show()

#%%% 2) campus_72_v1_3d.000

fig5, ax5 = plt.subplots()

a2 = new2["theta"].isel(x = 216, y = 122, zu_3d=2).fillna(0)

b2 = new2["im_t_indoor_mean"].isel(x = 216, y = 122, zw_3d=2).fillna(0)

c2 = (a2+b2)-273.15 #new

ax5.plot(c2.variable)
ax5.set_title("72 Hours Simulation Indoor Temperature for C Building at" + str(t) + ":00 Uhr" )
ax5.set_ylabel('Temperature °C')
ax5.set_xlabel('Time [Hours]')

plt.show()

#%%% 3) campus_gui_24_3d.000

fig6, ax6 = plt.subplots()

a3 = new3["theta"].isel(x = 216, y = 122, zu_3d=10).fillna(0)

b3 = new3["im_t_indoor_mean"].isel(x = 216, y = 122, zw_3d=10).fillna(0)

c3 = (a3+b3)-273.15 #new

ax6.plot(c3.variable)
ax6.set_title("GUI Simulation Indoor Temperature for C Building at" + str(t) + ":00 Uhr" )
ax6.set_ylabel('Temperature °C')
ax6.set_xlabel('Time [Hours]')
plt.show()



#%% Measured Data C Buildng
def mask(df):
    df = df[(df['datetime'] >= "2022-08-02 00:00:00") & (df['datetime'] <= "2022-08-03 00:00:00")]
    return df

def plt_df(df):
    
    plt.plot(df["datetime"], df["°C"], label = df["room"].iat[0])
    # make the x ticks as time
    plt.gcf().autofmt_xdate()
    myFmt = mdates.DateFormatter('%H:%M')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.xlabel("02-08-2023")
    plt.ylabel("Temperature °C")
    plt.ylim(20, 30)
    plt.title("Measured Room Temperature vs PALM")
    plt.legend()
    
    plt.show()

b_df_0 = pd.read_excel("C:/Users/rdevinen/Music/GitHub/campus_messung/6_Buildings_Comparison/0_rawdata/010822-030822/B1.xlsx") 

["Geb. B1:Gebäude B1'Lüftung'RLT Anlage Innenräume'AB-Temp. RLT Innenräume.Aktueller Wert", 
 "Geb. B1:Gebäude B1'Lüftung'RLT Anlage EDV Räume'AB-Temp. RLT EDV Räume.Aktueller Wert",
 "Geb_C:Gebäude B1'Lüftung'Lüftung Physik Hörsaal'Hörsaal 038'Raumtemperatur.Aktueller Wert",
 "Geb_C:Gebäude B1'Lüftung'Lüftung Chemie Hörsaal'Hörsaal 005'Raumtemperatur.Aktueller Wert",
 "Geb_C:Gebäude B1'Lüftung'Lüftung Hörsaal 012'Raumtemperatur.Aktueller Wert"]


###############################################################################

b_df_3 = b_df_0.iloc[:, [6,7]]
b_df_3['Datum/Uhrzeit5'] = pd.to_datetime(b_df_3['Datum/Uhrzeit5'], format = 
                                          "%d.%m.%Y %H:%M:%S")
b_df_3.columns = ["datetime", "°C"]
b_df_3 = mask(b_df_3)
b_df_3["room"] = "C_Physik Hörsaal"

###############################################################################

b_df_4 = b_df_0.iloc[:, [9,10]]
b_df_4['Datum/Uhrzeit8'] = pd.to_datetime(b_df_4['Datum/Uhrzeit8'], format = 
                                          "%d.%m.%Y %H:%M:%S")
b_df_4.columns = ["datetime", "°C"]
b_df_4 = mask(b_df_4)
b_df_4["room"] = "C_Chemie Hörsaal"

###############################################################################

b_df_5 = b_df_0.iloc[:, [12,13]]
b_df_5['Datum/Uhrzeit11'] = pd.to_datetime(b_df_5['Datum/Uhrzeit11'], format = 
                                         "%d.%m.%Y %H:%M:%S")
b_df_5.columns = ["datetime", "°C"]
b_df_5 = mask(b_df_5)
b_df_5["room"] = "C"

###############################################################################

b_df_6 = b_df_5.copy()
b_df_6["°C"] = (b_df_6["°C"] + b_df_5["°C"])/2
b_df_6["room"] = "C Building Measured"





#%% create a df
# creating a df in a format that fits the plotting function
date_today = datetime(2022, 8, 2, 0, 0)
days = pd.date_range(date_today, date_today + timedelta(hours = 24), freq='H')

np.random.seed(seed=1111)
data = np.random.randint(1, high=30, size=len(days))
df = pd.DataFrame({'datetime': days, '°C': data})
df["room"] = "test"
# df = df.set_index('datetime')
print(df)

#%%
df_24 = df.copy() ; df_24["°C"] = c1.values; df_24["room"] = "C Building PALM version 1"

df_72 = df.copy() ; df_72["°C"] = c2.values[:25]; df_72["room"] = "C Building PALM version 2"

df_gui = df.copy() ; df_gui["°C"] = c3.values; df_gui["room"] = "C Building PALM version GUI"


with open("b_building_sim.pkl", 'rb') as file:
    loaded_df = pickle.load(file)

loaded_df = loaded_df.loc[:, ["s_B_theta_air"]]

loaded_df = loaded_df.reset_index()
loaded_df.columns = ["datetime", "°C"]
loaded_df['datetime'] = loaded_df['datetime'] - pd.Timedelta(days = 365)
loaded_df["room"] = "C Building_5R1C"
c_5r1c = mask(loaded_df)

# b_df_3['Datum/Uhrzeit5'] = pd.to_datetime(b_df_3['Datum/Uhrzeit5'], format = 
                                          # "%d.%m.%Y %H:%M:%S")





fig7, ax7 = plt.subplots()

plt_df(df_24)
plt_df(df_72)
plt_df(df_gui)

plt_df(b_df_6)
# plt_df(c_5r1c)


ax7.grid(True,which='major',axis='both',alpha=0.3)

















#%%

# =============================================================================
# t = 24
# 
# for t in range(25):
#     
# 
# 
#     fig1, ax1 = plt.subplots()
#     
#     
#     a1 = new["theta"].isel(time=t, zu_3d=10).fillna(0)
#     
#     b1 = new["im_t_indoor_mean"].isel(time=t, zw_3d=10).fillna(0)
#     
#     c1 = (a1+b1)-273.15 #new
#     
#     
#     
#     c1.plot(  cmap='rainbow', robust=True, ax = ax1, label='Inline label', vmin=24, vmax=36); #new
#     ax1.set_title("24 Hours Simulation " + str(t) + ":00 Uhr" + " Temperature °C at 2 meters height")
#     fig1.savefig(f"1_plots/New Simulation _{t}.png")
#     
#     plt.show()
# plt.close("all")  
# =============================================================================
#%% Save as a GIF

# =============================================================================
# frames = []
# for t in range(8,25):
#     image = imageio.v2.imread(f'1_plots/New Simulation _{t}.png')
#     frames.append(image)
# =============================================================================

#%%
# =============================================================================
# imageio.mimsave('1_plots/animation.gif', # output gif
#                 frames,          # array of input frames
#                 duration = 1000)         # optional: frames per second
# 
# =============================================================================

###############################################################################
# Indoor data
# fig, ax = plt.subplots()

# b1 = new["im_t_indoor_mean"].sel(x = 381, y = 697, zw_3d=5, method='nearest') - 273.15

# ax.plot(new["im_t_indoor_mean"].time/3600000000000, b1.values)
# plt.ylim(20, 32)
# plt.show()
###############################################################################

# =============================================================================
# 
# fig2, ax2 = plt.subplots()
# 
# 
# 
# a1.plot(  cmap='rainbow', robust=True, ax = ax2, label='Inline label'); #new
# ax2.set_title("New Simulation " + str(t) + ":00 Uhr" + " Temperature °C at 2 meters height")
# # fig1.savefig("New Simulation " + str(t) + ":00 Uhr.png")
# =============================================================================


    
    
#%%




