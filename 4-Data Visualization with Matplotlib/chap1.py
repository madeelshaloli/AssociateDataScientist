# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot  as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

# Sample data for Seattle
seattle_weather = {
    "MONTH": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    "MLY-PRCP-NORMAL": [5.2, 3.8, 3.6, 2.5, 1.8, 1.4, 0.8, 1.0, 1.5, 3.3, 5.0, 5.6],
    "MLY-TAVG-NORMAL": [40.6, 42.7, 46.4, 50.5, 56.1, 61.7, 65.5, 65.4, 60.2, 52.0, 45.1, 40.2]
}

# Sample data for Austin
austin_weather = {
    "MONTH": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    "MLY-PRCP-NORMAL": [2.2, 2.3, 2.5, 2.6, 4.4, 3.7, 2.1, 2.5, 2.7, 3.9, 2.6, 2.4],
    "MLY-TAVG-NORMAL": [52.0, 55.5, 61.1, 68.0, 75.0, 80.4, 84.3, 84.0, 78.3, 68.0, 58.1, 52.2]
}


# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"] )

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()


# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b',marker='o',linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r',marker='v',linestyle='--')

# Call show to display the resulting plot
plt.show()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel('Time(months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation(inches')

# Add the title
ax.set_title('Weather patterns in Austin and seattle ')

# Display the figure
plt.show()


# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])
plt.show()


# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()