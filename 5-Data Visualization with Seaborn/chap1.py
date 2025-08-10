# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())


# Create a DataFrame from csv file
df=pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders',data=df)
sns.countplot(x=df['Spiders'])
sns.countplot(df['Spiders'])
# Display the plot
plt.show()

# Create a scatter plot of absences vs. final grade
# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",hue_order=['Rural','Urban'])


# Show plot
plt.show()

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school',data=student_data)
print(student_data[student_data['school']=='MS']['school'].count())


# Display plot
plt.show()
plt.clf()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school',data=student_data,hue='location',palette=palette_colors)



# Display plot
plt.show()