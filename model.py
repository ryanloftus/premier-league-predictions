import json
import random
from sklearn.linear_model import LinearRegression

# Define hyperparameters
FILTERED_MATCHWEEKS = 18 # n means ignore the first n matchweeks of each season
CROSS_TEAM_WITH_SEASON = True # if True, the team vector will be crossed with the season number
INCLUDE_POSITION = True # if True, the team's position will be included in the feature vector
FORCE_POSITIVE_COEFFICIENTS = True # if True, the model will be trained with positive coefficients
print(f"FILTERED_MATCHWEEKS: {FILTERED_MATCHWEEKS}")
print(f"CROSS_TEAM_WITH_SEASON: {CROSS_TEAM_WITH_SEASON}")
print(f"INCLUDE_POSITION: {INCLUDE_POSITION}")
print(f"FORCE_POSITIVE_COEFFICIENTS: {FORCE_POSITIVE_COEFFICIENTS}")

# Load data
labeled_examples = [json.loads(line) for line in open("labeled_examples.jsonl")]
labeled_examples = list(filter(lambda example: example["matchweek"] > FILTERED_MATCHWEEKS, labeled_examples))
teams = [team.strip() for team in open("teams.txt")]

# Define training and testing sets
random.seed(10)
random.shuffle(labeled_examples)
training_set_size = int(0.8 * len(labeled_examples))
training_set = labeled_examples[:training_set_size]
testing_set = labeled_examples[training_set_size:]

# Define helper functions
def get_team_one_hot_vector(team, season):
    one_hot_value = season if CROSS_TEAM_WITH_SEASON else 1
    return [one_hot_value if team == t else 0 for t in teams]

def get_feature_vector(example):
    normalized_season = example["season"] - 1994
    games_played = example["games_played"]
    normalized_wins = example["wins"] / games_played
    normalized_draws = example["draws"] / games_played
    normalized_losses = example["losses"] / games_played
    normalized_goals_for = example["goals_for"] / games_played
    normalized_goals_against = example["goals_against"] / games_played
    normalized_points = example["points"] / games_played
    feature_vector = [
        normalized_season,
        normalized_wins,
        normalized_draws,
        normalized_losses,
        normalized_goals_for,
        normalized_goals_against,
        normalized_points,
    ] + get_team_one_hot_vector(example["team"], example["season"])
    if INCLUDE_POSITION:
        normalized_position = example["position"] / 20
        feature_vector.append(normalized_position)
    return feature_vector

def calculate_loss(predictions, actual):
    N = len(predictions)
    return sum([(actual[i] - predictions[i]) ** 2 for i in range(N)]) / N # mean squared error

def get_features_and_labels(examples):
    X = [get_feature_vector(example) for example in examples]
    y = [example["final_points"] for example in examples]
    return X, y

# Train model
X, y = get_features_and_labels(training_set)
model = LinearRegression(positive=True).fit(X, y)

# Test model
training_set_predictions = model.predict(X)
training_loss = calculate_loss(training_set_predictions, y)
print(f"Training loss: {training_loss:.5f}")
test_X, test_y = get_features_and_labels(testing_set)
testing_set_predictions = model.predict(test_X)
testing_loss = calculate_loss(testing_set_predictions, test_y)
print(f"Testing loss: {testing_loss:.5f}")

# Predict
teams_to_predict = [json.loads(line) for line in open("unlabeled_examples.jsonl")]
prediction_input = list(map(get_feature_vector, teams_to_predict))
predictions = model.predict(prediction_input)
for team, predicted_points in zip(teams_to_predict, predictions):
    print(f"{team['team']}: {predicted_points:.2f}")
