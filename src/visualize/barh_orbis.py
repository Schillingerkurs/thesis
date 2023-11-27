# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:39:55 2023

@author: fs.egb
"""




import pandas as pd
from pathlib import Path
HERE = Path(__file__).parent.parent.parent.absolute()


from pathlib import Path
import pickle
import sys
MOZ_HERE = Path(r"C:\Users\fs.egb\moz_structural")
sys.path.insert(0, str(HERE/Path("src", "features")))
import matplotlib.pyplot as plt



with open(MOZ_HERE/Path("data","interim",
                "orbis_entries","orbis_data_MZ.pickle"), 'rb') as f:
    orbis_mz = pickle.load(f)


orbis_industry = (
    orbis_mz
    .drop_duplicates(subset = ["bvdid"])
    ['NACE_CODES'].value_counts()
    )



orbis_industry.plot.barh(stacked=True)


plt.savefig(HERE/Path("assets","orbis_moz",'barh_orbis.jpg'), 
            dpi=300, bbox_inches="tight")