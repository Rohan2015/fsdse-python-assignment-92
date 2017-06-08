import pandas as pd
import numpy as np


def solution(dat, ind):
    return pd.DataFrame(data = dat, index=ind)
