# David Huang Take Home 3 | Data Science Bootcamp

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set up notebook to show all outputs in a cell, not only last one


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

#1
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['day_name'] = df['hour_beginning'].dt.day_name()
# print(df.day_name)
# print(df.loc[df.day_name.isin(week_days)])
df = df.sort_values(by='hour_beginning')
week_analysis = df.loc[df.day_name.isin(week_days)]


plt.figure(figsize=(12, 6))
plt.plot(week_analysis.day_name, week_analysis.Pedestrians, color='blue')
plt.title('Pedestrian Counts Over Days of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()

#2
df['year'] = df['hour_beginning'].dt.year
year_analysis = df.loc[df.year == 2019]
year_analysis = year_analysis.sort_values(by='weather_summary')

correlation_matrix = year_analysis[['Pedestrians', 'temperature', 'precipitation']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Pedestrians and Weather Summary (2019)')
plt.tight_layout()
plt.show()

#3
df['hour'] = df['hour_beginning'].dt.hour
def daylight_cate(hour):
    daylight = ""
    if(hour >= 0 and hour <= 11):
        daylight = "Morning"
    elif(hour >= 12 and hour <= 17):
        daylight = "Afternoon"
    elif(hour >= 18 and hour <= 21):
        daylight = "Evening"
    else:
        daylight = "Night"
    return daylight

df['daylight'] = df['hour'].apply(daylight_cate)
#print(df['daylight'])

# Aggregating pedestrian counts by hour and plotting a bar graph
daylight_count = df.groupby(df['daylight'])['Pedestrians'].sum()
plt.figure(figsize=(12, 6))
daylight_count.plot(kind='bar', color='orange')
plt.title('Total Pedestrian Counts by Daylight')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Count')
plt.grid(axis='y')  #grid created alone y axis
plt.tight_layout()
plt.show()
