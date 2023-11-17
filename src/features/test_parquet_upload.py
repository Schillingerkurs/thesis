# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:47:43 2023

@author: fs.egb
"""

import pandas as pd
from pathlib import Path
HERE = Path(__file__).parent.parent.parent.absolute()



df = pd.read_parquet('https://github.com/Schillingerkurs/thesis/raw/main/uploads/mission_statements_full.parquet')