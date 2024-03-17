import json
import os

def get_final_matchweek(season):
    files = os.listdir(f"raw_data/{season}")
    matchweeks = [int(file.split(".")[0]) for file in files]
    return max(matchweeks)

with open("labeled_examples.jsonl", "w") as f_out:
    # raw_data directory structure: raw_data/{year season started}/{matchweek of data}.txt
    for season in range(1995, 2023):
        final_table = dict() # team name -> points after last matchweek
        final_matchweek = get_final_matchweek(season)
        for matchweek in range(final_matchweek, 0, -1):
            data_filename = f"raw_data/{season}/{matchweek}.txt"
            if not os.path.exists(data_filename):
                continue
            with open(data_filename) as f_in:
                lines = [line.strip("\n") for line in f_in.readlines()]
            for i in range(len(lines)):
                # the only lines in raw data that end with tab are the ones containing a team's record,
                # this line is preceded by a line containing team's name
                if lines[i].endswith("\t"):
                    team = lines[i-1].strip()
                    position = int(lines[i-4])
                    stats = [int(stat) for stat in lines[i].split("\t")[:8]]
                    entry = {
                        "season": season,
                        "matchweek": matchweek,
                        "team": team,
                        "position": position,
                        "games_played": stats[0],
                        "wins": stats[1],
                        "draws": stats[2],
                        "losses": stats[3],
                        "goals_for": stats[4],
                        "goals_against": stats[5],
                        "goal_difference": stats[6],
                        "points": stats[7],
                    }
                    if matchweek == final_matchweek:
                        final_table[team] = entry["points"]
                    entry["final_points"] = final_table[team]
                    f_out.write(json.dumps(entry) + "\n")

season_to_predict = 2023
matchweek_to_predict = 28
with open("unlabeled_examples.jsonl", "w") as f_out, \
     open(f"raw_data/{season_to_predict}/{matchweek_to_predict}.txt") as f_in:
    lines = [line.strip("\n") for line in f_in.readlines()]
    for i in range(len(lines)):
        if lines[i].endswith("\t"):
            team = lines[i-1].strip()
            position = int(lines[i-4])
            stats = [int(stat) for stat in lines[i].split("\t")[:8]]
            entry = {
                "season": season_to_predict,
                "matchweek": matchweek_to_predict,
                "team": team,
                "position": position,
                "games_played": stats[0],
                "wins": stats[1],
                "draws": stats[2],
                "losses": stats[3],
                "goals_for": stats[4],
                "goals_against": stats[5],
                "goal_difference": stats[6],
                "points": stats[7],
            }
            f_out.write(json.dumps(entry) + "\n")
