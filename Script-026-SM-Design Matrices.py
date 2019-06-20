#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import os
%matplotlib inline
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = df.dropna()
df[-10:]

y, X = dmatrices('profile ~ sedim_thick + igneous_volc + slope_angle',
                 data=df, return_type='dataframe')
y[:7]
X[:7]
