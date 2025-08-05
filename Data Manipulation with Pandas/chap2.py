#Aggregating DataFrames



import pandas as pd

# Assuming your data is already in a DataFrame called homelessness
homelessness = pd.DataFrame({
    'region': ['East South Central', 'Pacific', 'Mountain', 'West South Central', 'Pacific', 'Mountain', 'New England', 'South Atlantic', 'South Atlantic', 'South Atlantic', 'South Atlantic', 'Pacific', 'Mountain', 'East North Central', 'East North Central', 'West North Central', 'West North Central', 'East South Central', 'West South Central', 'New England', 'South Atlantic', 'New England', 'East North Central', 'West North Central', 'East South Central', 'West North Central', 'Mountain', 'West North Central', 'Mountain', 'New England', 'Mid-Atlantic', 'Mountain', 'Mid-Atlantic', 'South Atlantic', 'West North Central', 'East North Central', 'West South Central', 'Pacific', 'Mid-Atlantic', 'New England', 'South Atlantic', 'West North Central', 'East South Central', 'West South Central', 'Mountain', 'New England', 'South Atlantic', 'Pacific', 'South Atlantic', 'East North Central', 'Mountain'],
    'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
    'individuals': [2570.0, 1434.0, 7259.0, 2280.0, 109008.0, 7607.0, 2280.0, 708.0, 3770.0, 21443.0, 6943.0, 4131.0, 1297.0, 6752.0, 3776.0, 1711.0, 1443.0, 2735.0, 2540.0, 1450.0, 4914.0, 6811.0, 5209.0, 3993.0, 1024.0, 3776.0, 983.0, 1745.0, 7058.0, 835.0, 6048.0, 1949.0, 39827.0, 6451.0, 467.0, 6929.0, 2823.0, 11139.0, 8163.0, 747.0, 3082.0, 836.0, 6139.0, 19199.0, 1904.0, 780.0, 3928.0, 16424.0, 1021.0, 2740.0, 434.0],
    'family_members': [864.0, 582.0, 2606.0, 432.0, 20964.0, 3250.0, 1696.0, 374.0, 3134.0, 9587.0, 2556.0, 2399.0, 715.0, 3891.0, 1482.0, 1038.0, 773.0, 953.0, 519.0, 1066.0, 2230.0, 13257.0, 3142.0, 3250.0, 328.0, 2107.0, 422.0, 676.0, 486.0, 615.0, 3350.0, 602.0, 52070.0, 2817.0, 75.0, 3320.0, 1048.0, 3337.0, 5349.0, 354.0, 851.0, 323.0, 1744.0, 6111.0, 972.0, 511.0, 2047.0, 5880.0, 222.0, 2167.0, 205.0],
    'state_pop': [4887681, 735139, 7158024, 3009733, 39461588, 5691287, 3571520, 965479, 701547, 21244317, 10511131, 1420593, 1750536, 12723071, 6695497, 3148618, 2911359, 4461153, 4659690, 1339057, 6035802, 6882635, 9984072, 5606249, 2981020, 6121623, 1060665, 1925614, 3027341, 1353465, 8886025, 2092741, 19530351, 10381615, 758080, 11676341, 3940235, 4181886, 12800922, 1058287, 5084156, 878698, 6771631, 28628666, 3153550, 624358, 8501286, 7523869, 1804291, 5807406, 577601]
})


# Data as a dictionary
data = {
    'store': [1, 2, 4, 6, 10, 13, 14, 19, 20, 27, 31, 39],
    'type': ['A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    'department': [1] * 12,
    'date': ['2010-02-05'] * 12,
    'weekly_sales': [24924.50, 35034.06, 38724.42, 25619.00, 40212.84, 46761.90, 32842.31, 21500.58, 46021.21, 32313.79, 18187.71, 21244.50],
    'is_holiday': [False] * 12,
    'temperature_c': [5.728, 4.550, 6.533, 4.683, 12.411, -0.261, -2.606, -6.133, -3.378, -2.672, 3.917, 6.833],
    'fuel_price_usd_per_l': [0.679, 0.679, 0.686, 0.679, 0.782, 0.704, 0.735, 0.780, 0.735, 0.780, 0.679, 0.679],
    'unemployment': [8.106, 8.324, 8.623, 7.259, 9.765, 8.316, 8.992, 8.350, 8.187, 8.237, 8.324, 8.554]
}

# Convert to DataFrame
store_types = pd.DataFrame(data)




def pct40(column):
    return column.quantile(0.5)
print(pct40(homelessness['individuals']))

print(homelessness['individuals'].cumsum())
print(homelessness['individuals'].cummax())
print(homelessness['individuals'].cummin())
print(homelessness['individuals'].cumprod())

# Print the head of the sales DataFrame
print(sales.head)

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

# Print the maximum of the date column
print (sales['date'].max())

# Print the minimum of the date column
print (sales['date'].min())

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))
print(iqr(sales['temperature_c']))

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
print(iqr(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']]))


# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')


# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()


# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=False, normalize=True)
print(dept_props_sorted)


# Calc total weeklny sales
sales_all =sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B  = sales[sales["type"] == "B"]["weekly_sales"].sum()


# Subset for type C stores, calc total weekly sales
sales_C  = sales[sales["type"] == "C"]["weekly_sales"].sum()

print(sales_C)
# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print(sales_by_type)
# Get proportion for each type
sales_propn_by_type = sales_by_type/ sum(sales_by_type)
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type','is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Import numpy with the alias np
import numpy as np
# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([min,max,np.mean,np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats  = sales.groupby('type')[['unemployment','fuel_price_usd_per_l']].agg([min,max,np.mean,np.median])


# Print unemp_fuel_stats
print(unemp_fuel_stats)

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales',index='type')
# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales',index='type',aggfunc=[np.mean,np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Import NumPy as np
import numpy as np
import numpy as np 
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales',index='type',aggfunc=[np.mean,np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales',index='type',columns='is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales',index='department',columns='type',fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0,margins=True))