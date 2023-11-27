# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:30:51 2023

@author: fs.egb
"""

from pathlib import Path
import pickle
import sys
HERE = Path(r"C:\Users\fs.egb\moz_structural")
sys.path.insert(0, str(HERE/Path("src", "features")))


import baci



iso3_cntry  = "MOZ"

baci_mz = baci.get_total_trade(HERE,iso3_cntry) 
