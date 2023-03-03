import pandas as pd
import matplotlib.pyplot as plt


# reading the CSV file into a pandas DataFrame
df = pd.read_csv(
    "C:/Users/kusha/OneDrive/Desktop/assignment/england airfrost information2.csv")
print(df)

# defining a function to calculate average air frost for winter, spring and autumn


def calculate_avg_airfrost(df):
    # creating an empty dictionary to store the result
    average = {}
    # using loop to represent the seasons
    for season in ['win', 'spr', 'aut']:
        # calculating the mean air frost for the season
        mean_airfrost = df[season].mean()
        # adding the mean air frost to the dictionary
        average[season] = mean_airfrost
    # returing the dictionary of average air frost
    return average


# calling the fu nction to calculate the average airfrost
average = calculate_avg_airfrost(df)
print("Average airfrost for winter, spring, and autumn:", average)

# creating a line plot in which each seasons is represented with diff. colour
fig, ax = plt.subplots()
key = df.columns[0]

ax.plot(df[key], df['win'], color='blue',
        label=f'Winter (Avg: {average["win"]:.1f}°F)')
ax.plot(df[key], df['spr'], color='yellow',
        label=f'Spring (Avg: {average["spr"]:.1f}°F)')
ax.plot(df[key], df['aut'], color='red',
        label=f'Autumn (Avg: {average["aut"]:.1f}°F)')

# setting the plot title and axis labels
plt.title('seasonal and annual air frost for England')
plt.xlabel('Year ')
plt.ylabel('airfrost (°F)')
plt.ylim(0, 80)
plt.xlim(1960, 2023)

plt.legend()

# show the plot
plt.show()
