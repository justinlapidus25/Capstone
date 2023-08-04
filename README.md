# Capstone
NBA Regression
# NBA All-Star Selection Prediction
![nbaasg-feat1](https://github.com/justinlapidus25/Capstone/assets/130884190/3650e5c2-5a3a-4e4e-8593-9cb7445790e9)


## Overview

This project aims to predict whether NBA players will be selected as All-Stars based on historical NBA statistics and All-Star team selection data. It utilizes machine learning algorithms, data cleaning techniques, feature selection, and visualization to build a predictive model for identifying potential All-Stars in the NBA.

## Requirements

Before running the code, you need to have the following Python libraries installed:

- pandas: For data manipulation and analysis.
- seaborn: For data visualization.
- numpy: For numerical computations.
- matplotlib: For creating plots and charts.
- scikit-learn: For machine learning algorithms.
- imbalanced-learn: For dealing with class imbalance in the data.
- xgboost: For using the XGBoost algorithm.

You can install these libraries using pip:

```bash
pip install pandas seaborn numpy matplotlib scikit-learn imbalanced-learn xgboost
```

## Dataset

The dataset used in this project consists of two main parts:

1. NBA Player Statistics: Contains statistics of NBA players for various seasons, including points, rebounds, assists, shooting percentages, etc. The data is loaded from CSV files, and missing values are filled to ensure data integrity.

2. All-Star Team Selection Data: Contains information about the players selected as All-Stars for different seasons. The data is also loaded from CSV files.

Additionally, RAPTOR scores are imported, which are a measure of a player's contributions to team offense and defense per 100 possessions, relative to a league-average player.

## Workflow

The code performs the following steps to predict All-Star selections:

1. Data Cleaning: NBA player statistics and All-Star data are read from CSV files and cleaned by handling missing values and dropping irrelevant columns. Here is an example of a heatmap showing missing values in the NBA Player Statistics dataset:


2. Data Merging: The cleaned data is merged based on player names and seasons to create a final dataframe that includes player stats and whether they were selected as All-Stars or not.

3. Feature Selection: The top 15 columns with the highest correlation to the target variable "Was_Allstar" are selected as features for model building. Here is an example of a heatmap showing the correlation between different features and the target variable:


4. Data Scaling: Numerical features are scaled using MinMaxScaler to ensure all features are on the same scale, which helps improve model performance.

5. Model Building: Several machine learning pipelines are created using different classifiers such as DecisionTreeClassifier, RandomForestClassifier, XGBClassifier, ExtraTreesClassifier, and SVC. SMOTE is used to handle class imbalance, and GridSearchCV is used for hyperparameter tuning.

6. Model Evaluation: Each pipeline is fitted to the training data, and hyperparameter tuning is performed using GridSearchCV. The models are evaluated on the test data to identify the best-performing model.

7. Saving the Model: The best-performing model is saved using pickle for future use.

## Visualization

To better understand the data and model performance, the code includes several visualizations:

1. Heatmap: A heatmap is used to visualize the top 15 columns with the highest correlation to the target variable "Was_Allstar."

2. Confusion Matrix: Confusion matrices are plotted to visualize the model's performance in predicting All-Star selections.


