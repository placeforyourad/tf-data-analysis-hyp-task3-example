import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 422633669 # Ваш chat ID, не меняйте название переменной

def solution(control: pd.Series, test: pd.Series) -> bool:
    result = ttest_ind(control, test, equal_var=False)

    return result.pvalue < 0.01
