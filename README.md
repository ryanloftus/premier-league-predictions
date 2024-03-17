# premier-league-predictions

## Data

The raw data used in this project come from [https://www.premierleague.com/tables](https://www.premierleague.com/tables). The data are parsed into jsonl format where each line represents a team's current standing after a particular matchweek in a particular season. The season is given as the year that the season started. So, the 1995/96 season is given as 1995 in the jsonl file.

The data used come from the start of the 1995/96 season until the end of the 2022/23 season. This represents all completed premier league seasons which have had 20 teams.

## Model

A linear regression model is used to predict how many points a team will finish with given the team's current standing. Below are variations of the model and how they performed. Note that the large loss decrease when increasing `FILTERED_MATCHWEEKS` is expected because those data are the most uncertain (in other words, the first $n$ games of a season do not provide enough information to draw meaningful conclusions if $n$ is too small).

For Model 11, a fourth hyperparamter, `FORCE_POSITIVE_COEFFICIENTS` is introduced. With this hyperparamter set to False, we will get ridiculous predictions for any teams the model has not seen in the training data.

### Model 1
```
FILTERED_MATCHWEEKS: 0
CROSS_TEAM_WITH_SEASON: False
INCLUDE_POSITION: False
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 63.65357
Testing loss: 65.80031
```

### Model 2
```
FILTERED_MATCHWEEKS: 10
CROSS_TEAM_WITH_SEASON: False
INCLUDE_POSITION: False
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 28.16830
Testing loss: 28.82463
```

### Model 3
```
FILTERED_MATCHWEEKS: 0
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: False
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 63.63075
Testing loss: 65.75298
```

### Model 4
```
FILTERED_MATCHWEEKS: 0
CROSS_TEAM_WITH_SEASON: False
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 57.41220
Testing loss: 58.26012
```

### Model 5
```
FILTERED_MATCHWEEKS: 10
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: False
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 28.16754
Testing loss: 28.82420
```

### Model 6
```
FILTERED_MATCHWEEKS: 10
CROSS_TEAM_WITH_SEASON: False
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 28.16361
Testing loss: 28.83692
```

### Model 7
```
FILTERED_MATCHWEEKS: 0
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 57.38159
Testing loss: 58.22144
```

### Model 8
```
FILTERED_MATCHWEEKS: 10
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 28.16345
Testing loss: 28.83237
```

### Model 9
```
FILTERED_MATCHWEEKS: 12
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 24.99744
Testing loss: 24.70484
```

### Model 10
```
FILTERED_MATCHWEEKS: 18
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: False
Training loss: 17.05715
Testing loss: 16.74384
```

### Model 11
```
FILTERED_MATCHWEEKS: 18
CROSS_TEAM_WITH_SEASON: True
INCLUDE_POSITION: True
FORCE_POSITIVE_COEFFICIENTS: True
Training loss: 17.14186
Testing loss: 16.80325
```

## Predictions
Using Model 11, we get the following prediction for the final standings in the premier league 2023/24 season (predicted from the table after matchweek 29):

| Position | Team | Points |
| --- | --- | --- |
1 | Arsenal | 86.43
2 | Liverpool | 86.05
3 | Manchester City | 83.11
4 | Aston Villa | 71.49
5 | Tottenham Hotspur | 70.96
6 | Manchester United | 64.07
7 | Chelsea | 57.96
8 | West Ham United | 57.72
9 | Brighton And Hove Albion | 56.06
10 | Newcastle United | 55.71
11 | Wolverhampton Wanderers | 54.31
12 | Fulham | 50.00
13 | Bournemouth | 48.10
14 | Crystal Palace | 42.22
15 | Brentford | 40.49
16 | Everton | 37.11
17 | Nottingham Forest | 35.50
18 | Luton Town | 28.11
19 | Burnley | 26.16
20 | Sheffield United | 23.47
