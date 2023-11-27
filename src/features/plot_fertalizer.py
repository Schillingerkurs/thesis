# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:47:43 2023

@author: fs.egb
"""

import pandas as pd
from pathlib import Path
HERE = Path(__file__).parent.parent.parent.absolute()


from pathlib import Path
import pickle
import sys
HERE = Path(r"C:\Users\fs.egb\moz_structural")
sys.path.insert(0, str(HERE/Path("src", "features")))
import matplotlib.pyplot as plt

import baci



baci_mz = baci.get_total_trade(HERE,"MOZ") 



df = pd.read_parquet('https://github.com/Schillingerkurs/thesis/raw/main/uploads/mission_statements_full.parquet', engine='pyarrow')



search_term_baci = (baci_mz
            .query("product.str.lower().str.contains('fertilizer')")
            ['product'].value_counts()
            )




baci_imports = (baci_mz
                    .loc[baci_mz['product'] =="Fertilizers, animal or vegetable: whether or not mixed together or chemically treated: fertilizers, produced by the mixing or chemical treatment of animal or vegetable products"]                                                                                                                                    
                    .query("importer == 'MOZ'")
                    # .assign(t = lambda x: pd.to_datetime(x['t'], format='%Y'))
                    .groupby("t")["v"].sum()
                    )



# fertilizer

time_series = (df
            .query("corpus_en.str.lower().str.contains('fertilizer')")
           # .assign(y = lambda x: pd.to_datetime(x['y'], format='%Y'))
            .groupby(["y","orga_type"]).size()
            .reset_index()
            .pivot(index = "y", columns = "orga_type", values = 0)
            .assign(baci_imports = lambda x: x.index.map(baci_imports))

            )





# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.bar(time_series.index,
        time_series['sociedade por quotas'],
        color="#1E88E5",
        )
# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("Registerd companies\n that trade with fertilizer",
              color="#1E88E5",
              fontsize=14)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(time_series.index, 
         time_series["baci_imports"],
         color="#D81B60",
         # marker="o"
         )

ax2.set_ylabel('Value of fertilizer \n imports (BACI)',color="#D81B60",fontsize=14)



# discovery = pd.to_datetime(20080801, format = '%Y%m%d')
# ax.vlines(x = discovery, ymin=0, ymax= 20000, dashes = "--", label = "Discovery of \nWindjammer field \n", color = "navy" )

ax.legend(loc='upper left')

plt.subplots_adjust(bottom=0.15)

fig.patch.set_facecolor('white')

plt.savefig(Path(r"C:\Users\fs.egb\thesis\assets\baci_bdr\fertilizer.jpg"), 
            dpi=300, bbox_inches="tight")