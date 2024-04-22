import tarfile
import json
import os
import bz2
import datetime

teams = [
    "Arsenal",
    # "Aston Villa",
    # "Bournemouth",
    # "Brentford",
    # "Brighton",
    "Chelsea",
    # "Crystal Palace",
    # "Everton",
    # "Fulham",
    # "Leeds",
    # "Leicester",
    "Liverpool",
    "Man City",
    "Man Utd",
    # "Newcastle",
    # "Nottm Forest",
    # "Southampton",
    "Tottenham",
    # "West Ham",
    # "Wolves"
]


def extract_data(file_name):
    data = []
    with tarfile.open(file_name, 'r') as mytar:
        # Loop through each file
        for member in mytar.getmembers():
            # Check if the file is a .bz2 file
            if member.isfile() and member.name.endswith('.bz2'):
                # Open each file
                try:
                    with mytar.extractfile(member) as myfile:
                        with bz2.open(myfile, 'rt') as f:  # Open the file in text mode
                            match_date = ""
                            team1_id = ""
                            team2_id = ""
                            draw_id = ""
                            team1_name = ""
                            team2_name = ""
                            # draw_name = ""
                            match_odds = []
                            for line in f:  # Read the file line by line
                                try:
                                    json_content = json.loads(line)  # Parse each line as a separate JSON object
                                    if 'marketDefinition' in json_content["mc"][0]:
                                            market_definition = json_content["mc"][0]["marketDefinition"]
                                            market_time = market_definition['marketTime']
                                            date = datetime.datetime.strptime(market_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                                            match_date = date.isoformat(),
                                            team1_id = market_definition["runners"][0]["id"]
                                            team2_id = market_definition["runners"][1]["id"]
                                            draw_id = market_definition["runners"][2]["id"]
                                            team1_name = market_definition["runners"][0]["name"]
                                            team2_name = market_definition["runners"][1]["name"]
                                            if team1_name not in teams or team2_name not in teams:
                                                raise Exception("Team not in the list")
                                            # draw_name = market_definition["runners"][2]["name"]
                                    elif 'rc' in json_content["mc"][0]:
                                        time = datetime.datetime.utcfromtimestamp(int(json_content['pt']) / 1000)
                                        date = time.strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD
                                        time_of_day = time.strftime("%H:%M:%S.%f")[:-3] 
                                        odd1 = -1
                                        odd2 = -1
                                        oddD = -1
                                        for rc_item in json_content["mc"][0]["rc"]:
                                            if rc_item["id"] == team1_id:
                                                odd1 = rc_item["ltp"]
                                            elif rc_item["id"] == team2_id:
                                                odd2 = rc_item["ltp"]
                                            elif rc_item["id"] == draw_id:
                                                oddD = rc_item["ltp"]
                                        match_odds.append({"date": date,
                                                           "time": time_of_day,
                                                           "team1": odd1,
                                                           "team2": odd2,
                                                           "draw": oddD
                                                           })
                                except json.JSONDecodeError as e:
                                    print(f"Error reading line: {line}. Error: {str(e)}")
                            date, time = match_date[0].split('T')
                            match = {
                            "match_date": date,
                            "start_time": time,
                            "team1_name": team1_name,
                            "team2_name": team2_name,
                            "match_odds": match_odds
                            }
                            data.append(match)
                except Exception as e:
                    if e.args[0] == "Team not in the list":
                        continue
                    else:
                        print(f"Error reading file: {member.name}")
    return data

file_name = "GB_m_data.tar"

jsonData = extract_data(file_name)

#time in UTC

# Save jsonData to a JSON file
with open('output.json', 'w') as json_file:
    # for item in jsonData:
    #     item['match_odds'] = json.dumps(item['match_odds'])
    json.dump(jsonData, json_file, indent=4)

