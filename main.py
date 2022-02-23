# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
data = "processed.cleveland.data"

# %%
names = ['col-1', 'col-2', 'col-3', 'col-4', 'col-5','col-6', 'col-7', 'col-8', 'col-9', 'col-10','col-11', 'col-12', 'col-13', 'col-14']

# %%
dataset = pd.read_csv(data, names=names)

# %%
dataset.head()


