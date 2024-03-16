import json

teams = set()
with open("labeled_examples.jsonl") as f_in:
    for line in f_in:
        example = json.loads(line)
        teams.add(example["team"])

with open("teams.txt", "w") as f_out:
    f_out.write("\n".join(sorted(teams)))
