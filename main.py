import json
from sklearn import datasets, linear_model

# Load data
labeled_examples = [json.loads(line) for line in open("labeled_examples.jsonl")]
y = [example["final_points"] for example in labeled_examples]

