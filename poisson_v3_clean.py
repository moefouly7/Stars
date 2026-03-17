# Poisson Football Model v3 - EPL
# change HOME_TEAM, AWAY_TEAM, ODDS before running
import subprocess
subprocess.run(["pip", "install", "requests", "pandas", "scipy", "-q"])
import pandas as pd
import numpy as np
from scipy.stats import poisson
from io import StringIO
import requests, json, warnings
warnings.filterwarnings("ignore")
HOME_TEAM = "Aston Villa"
AWAY_TEAM = "West Ham"
LEAGUE_CODE = "E0"
LEAGUE_NAME = "EPL"
MATCH_DATE = "2026-03-16"
SEASONS = ["2223", "2324", "2425"]
MAX_GOALS = 8
EV_THRESHOLD = 0.05
API_KEY = "800b1acde6f159daf20639370929b660"
ODDS = {
    "home": 2.02,
    "draw": 3.63,
    "away": 4.07,
    "over2.5": "N/A",
    "under2.5": "N/A",
    "btts_yes": "N/A",
    "btts_no": "N/A",
}
# full version in colab
