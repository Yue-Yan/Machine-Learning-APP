# Author: Feiyue
# Date: 2022-08-20
# I love :coffe :pizza and :dancer

import os
import numpy as np
import pandas as pd


def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def dev(x, y):
  try:
    return x / y
  except Exception as e:
    print(e)
    return None

def data_to_df(ls):
    if isinstance(ls, list):
        df = pd.DataFrame(ls)
    else:
        df = pd.DataFrame(list(ls))
    return df
