import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from xgboost import XGBClassifier


# Load the data for each standard
scores_5th = pd.read_csv("Data/Growth5th.csv")
scores_6th = pd.read_csv("Data/Growth6th.csv")
scores_7th = pd.read_csv("Data/Growth7th.csv")
scores_8th = pd.read_csv("Data/Growth8th.csv")
scores_9th = pd.read_csv("Data/Growth9th.csv")
scores_10th = pd.read_csv("Data/Growth10th.csv")

# Rename columns to include the year for easier merging
scores_5th = scores_5th.add_suffix("_5").rename(columns={"Unique_ID_5": "Unique_ID"})
scores_6th = scores_6th.add_suffix("_6").rename(columns={"Unique_ID_6": "Unique_ID"})
scores_7th = scores_7th.add_suffix("_7").rename(columns={"Unique_ID_7": "Unique_ID"})
scores_8th = scores_8th.add_suffix("_8").rename(columns={"Unique_ID_8": "Unique_ID"})
scores_9th = scores_9th.add_suffix("_9").rename(columns={"Unique_ID_9": "Unique_ID"})
scores_10th = scores_10th.add_suffix("_10").rename(columns={"Unique_ID_10": "Unique_ID"})

# Merge datasets on Unique_ID
df_growthrate = scores_5th.merge(scores_6th, on="Unique_ID") \
               .merge(scores_7th, on="Unique_ID") \
               .merge(scores_8th, on="Unique_ID") \
               .merge(scores_9th, on="Unique_ID") \
               .merge(scores_10th, on="Unique_ID")
df_growthrate

# df_growthrate = df_growthrate.drop(columns=["Interest_5", "Interest_6", "Interest_7", "Interest_8", "Interest_9", "Interest_10"])
# df_growthrate

