# Import numpy with alias np
import numpy as np 

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country']=='Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country']=='USA']


# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

print(usa_consumption['consumption'].mean())



# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category']=='rice']
print(rice_consumption)

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()


# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg(['mean','median']))
print(rice_consumption['co2_emission'].agg([np.mean,np.median]))


# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0,0.25,0.5,0.75,1]))

# Calculate the quintiles of co2_emission

print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6,0.8, 1]))

# Calculate the deciles of co2_emission

print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1,11)))



# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var,np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Create histogram of co2_emission for food_category 'beef'
plt.hist(food_consumption[food_consumption['food_category']=='beef']['co2_emission'])
# Show plot
plt.show()
plt.clf()
# Create histogram of co2_emission for food_category 'eggs'
plt.hist(food_consumption[food_consumption['food_category']=='eggs']['co2_emission'])
# Show plot
plt.show()


# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)


# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country<lower)|(emissions_by_country>upper)]
print(outliers)