import json

with open("parsed_data.jsonl", "w") as f_out:
    # raw_data directory structure: raw_data/{year season started}/{matchweek of data}.txt
    for season in range(1995, 1996):
        final_table = dict() # team name -> points after last matchweek
        for matchweek in range(38, 0, -1):
            with open(f"raw_data/{season}/{matchweek}.txt") as f_in:
                lines = [line.strip("\n") for line in f_in.readlines()]
            for i in range(len(lines)):
                # the only lines in raw data that end with tab are the ones containing a team's record,
                # this line is preceded by a line containing team's name
                if lines[i].endswith("\t"):
                    team = lines[i-1].strip()
                    stats = [int(stat) for stat in lines[i].split("\t")[:8]]
                    entry = {
                        "season": season,
                        "matchweek": matchweek,
                        "team": team,
                        "games_played": stats[0],
                        "wins": stats[1],
                        "draws": stats[2],
                        "losses": stats[3],
                        "goals_for": stats[4],
                        "goals_against": stats[5],
                        "goal_difference": stats[6],
                        "points": stats[7],
                    }
                    if matchweek == 38:
                        final_table[team] = entry["points"]
                    entry["final_points"] = final_table[team]
                    f_out.write(json.dumps(entry) + "\n")
