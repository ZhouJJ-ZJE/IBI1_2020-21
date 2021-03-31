import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import file and show every second row between 0 and 10
covid_data = pd.read_csv("full_data.csv")
print(covid_data.loc[0:11:2, :])
# used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
my_columns = [False, False, False, False, True, False]
Afg = []
for i in range(0, 7996):
    if covid_data.loc[i, "location"] == "Afghanistan":
        Afg.append(i)
print(covid_data.loc[Afg, my_columns])
# computed the mean and median of new cases for the entire world
World = []
for i in range(0, 7996):
    if covid_data.loc[i, "location"] == 'World':
        World.append(i)
world_new_cases = covid_data.loc[World, "new_cases"]
world_new_deaths = covid_data.loc[World, "new_deaths"]
world_dates = covid_data.loc[World, "date"]  # for the plot below
print(world_new_cases.describe())
# created a boxplot
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()
# plot both new cases and new deaths worldwide
plt.plot(world_dates, world_new_cases, 'r')
plt.plot(world_dates, world_new_deaths, 'b')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.show()
# question part: How have new cases and total cases developed over time in Spain?
Spain = []
for i in range(0, 7996):
    if covid_data.loc[i, "location"] == 'Spain':
        Spain.append(i)
Spain_new_cases = covid_data.loc[Spain, "new_cases"]
Spain_total_cases = covid_data.loc[Spain, "total_cases"]
plt.plot(world_dates, Spain_new_cases, 'r')
plt.plot(world_dates, Spain_total_cases, 'b')
plt.title("Pandemic in Spain")
plt.show()

