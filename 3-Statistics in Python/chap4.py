# CORRELATION

# Create a scatterplot of happiness_score vs. life_exp and show
import seaborn  as sns
sns.scatterplot(world_happiness['happiness_score'],world_happiness['life_exp'])
# Show plot
plt.show()

sns.scatterplot(x='happiness_score',y='life_exp',data=world_happiness)
# Show plot
plt.show()

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='happiness_score',y='life_exp',data=world_happiness,ci=None)
# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

# Correlation between gdp_per_cap and life_exp
cor = world_happiness['life_exp'].corr(world_happiness['gdp_per_cap'])

print(cor)

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap',y='life_exp',data=world_happiness)
# Show plot
plt.show()


# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(y='happiness_score',x='gdp_per_cap',data=world_happiness)
plt.show()
plt.clf()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(y='happiness_score',x='log_gdp_per_cap',data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)


# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='happiness_score',y='grams_sugar_per_day',data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)