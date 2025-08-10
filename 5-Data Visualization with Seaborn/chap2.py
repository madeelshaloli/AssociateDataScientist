import matplotlib.pyplot as plt
import seaborn as sns

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data,kind='scatter')

# Show plot
plt.show()

sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",col='study_time')

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Create a scatter plot of G1 vs. G3


sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],row='famsup',row_order=['yes','no'])
# Show plot
plt.show()

# Create scatter plot of horsepower vs. mpg

sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",hue='cylinders')


# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg

sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style='origin',hue='origin')


# Show plot
plt.show()


# Create line plot

sns.relplot(x='model_year',y='mpg',data=mpg,kind='line')

# Show plot
plt.show()


# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci='sd')

# Show plot
plt.show()

# Create line plot of model year vs. horsepower

sns.relplot(x='model_year',y='horsepower',data=mpg,kind='line',ci=None)


# Show plot
plt.show()


# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", style='origin',hue='origin',
            ci=None)

# Show plot
plt.show()