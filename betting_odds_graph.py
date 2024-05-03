import matplotlib.pyplot as plt
import pandas as pd
import json
from datetime import timedelta

# Assuming 'data' is your JSON data
with open('output.json', 'r') as json_file:
    # Load the JSON data
    data = json.load(json_file)

# Flatten the data
flattened_data = []
for match in data:
    last_team1_odds = None
    last_team2_odds = None
    last_draw_odds = None
    for odds in match['match_odds']:
        team1_odds = odds['team1'] if odds['team1'] != -1 else last_team1_odds
        team2_odds = odds['team2'] if odds['team2'] != -1 else last_team2_odds
        draw_odds = odds['draw'] if odds['draw'] != -1 else last_draw_odds
        flattened_data.append({
            'match_date': match['match_date'],
            'start_time': match['start_time'],
            'team1_name': match['team1_name'],
            'team2_name': match['team2_name'],
            'odds_date': odds['date'],
            'odds_time': odds['time'],
            'team1_odds': team1_odds,
            'team2_odds': team2_odds,
            'draw_odds': draw_odds,
        })
        if team1_odds is not None:
            last_team1_odds = team1_odds
        if team2_odds is not None:
            last_team2_odds = team2_odds
        if draw_odds is not None:
            last_draw_odds = draw_odds

# Convert to DataFrame
df = pd.DataFrame(flattened_data)

df['match_datetime'] = pd.to_datetime(df['match_date'] + ' ' + df['start_time'])
df['odds_datetime'] = pd.to_datetime(df['odds_date'] + ' ' + df['odds_time'])

# Filter out the odds that are not during the game or just before the game
df = df[(df['odds_datetime'] >= df['match_datetime']) & (df['odds_datetime'] <= df['match_datetime'] + timedelta(minutes=90))]

# Create a separate graph for each match
for (match_date, team1_name, team2_name), match_df in df.groupby(['match_date', 'team1_name', 'team2_name']):
    plt.figure(figsize=(10, 6))
    plt.plot(match_df['odds_datetime'], match_df['team1_odds'], label=team1_name)
    plt.plot(match_df['odds_datetime'], match_df['team2_odds'], label=team2_name)
    plt.plot(match_df['odds_datetime'], match_df['draw_odds'], label='Draw')
    title = f"Odds for match on {match_date} between {team1_name} and {team2_name}"
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Odds')
    plt.legend()
    plt.savefig(title + '.png')  # Save the figure
    plt.show()
