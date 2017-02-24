import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from pandas import Series, DataFrame,Panel

today = datetime.datetime.now().strftime("%Y%m%d")

info = pd.read_csv(today + "-stats.txt", parse_dates=[0], header=None)

info.plot.line()


