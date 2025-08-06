# Using merge_ordered()

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values

gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',fill_method='ffill')

# Print gdp_sp500
print(gdp_sp500)

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())


# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation,unemployment,on='date',how='inner')


# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter',x='unemployment_rate',y='cpi')
plt.show()


# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp,pop,on=['date','country'] ,
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp,pop,on=['country','date'],fill_method='ffill')

# Print date_ctry
print(date_ctry)


# Use merge_asof() to merge jpm and wells
jpm_wells =pd.merge_asof(jpm,wells,on='date_time',suffixes=['','_wells'],direction='nearest')

print(jpm_wells)
# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac=pd.merge_asof(jpm_wells,bac,on='date_time',suffixes=['_jpm','_bac'],direction='nearest')
 

print(jpm_wells_bac)
# Compute price diff
price_diffs = jpm_wells_bac.diff()
print(price_diffs)
# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()



social_fin.query('company=="facebook" & financial=="total_revenue"')
social_fin.query('value<0 & financial=="net_income"')
social_fin.query('value<0')
social_fin.query('value>100000 & financial=="gross_profit"')

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date>="1991-01-01"')
print(recent_gdp_pop)
# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year',var_name='month',value_name='unempl_rate')

print(ur_tall)
# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])
print(ur_tall)
# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date',y='unempl_rate')
plt.show()


# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric',var_name='date',value_name='close')
print(bond_perc)
# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric=="close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji,bond_perc_close,on='date',how='inner',suffixes=('_dow','_bond'))
print(dow_bond)

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow','close_bond'], x='date', rot=90)
plt.show()
plt.clf()