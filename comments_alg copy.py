import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file_name = 'jakes_labelled\man_city_vs_chelsea.csv'
# Load your csv file
df = pd.read_csv(file_name)

columns = df.columns
team1 =  columns[2]
team2 = columns[3]

df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')
print(df)
# Define the start time of the match
match_date = "2023-05-21"
start_time = "11:00:00"
end_time = "13:00:00"
match_start = datetime.strptime(f"{match_date} {start_time}", "%Y-%m-%d %H:%M:%S")
match_end = datetime.strptime(f"{match_date} {end_time}", "%Y-%m-%d %H:%M:%S")

df = df[(df['time'] >= match_start)]
df = df[df['time'] < match_end]

# Make sure your time column is in the correct datetime format
df[team1] = pd.to_numeric(df[team1], errors='coerce').astype('Int64')
df[team2] = pd.to_numeric(df[team2], errors='coerce').astype('Int64')

# Set the time column as the index of the dataframe
df.set_index('time', inplace=True)

df_resampled1 = df[team1].resample('5T').sum().fillna(0)
df_resampled2 = df[team2].resample('5T').sum().fillna(0)

# Plot the data with labels
plt.plot(df_resampled1, label=team1)
plt.plot(df_resampled2, label=team2)

plt.title(team1 + ' vs ' + team2 + ' ' +match_date)
plt.xlabel('Time')
plt.ylabel('Values')

# Display the legend
plt.legend()

plt.show()
