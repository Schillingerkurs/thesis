# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:57:22 2022

@author: fs.egb
"""


from pathlib import Path
# import re
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'
import pickle
# import itertools
import geopandas as gpd

from shapely.geometry import shape, Point
import datetime
import sys

HERE = Path(__file__).parent.parent.parent.absolute()





df = pd.read_parquet(HERE/Path("data","processed","adm2.parquet.gzip")  )

adm = HERE/Path("data","external","adm",  "moz_admbnda_adm2_ine_20190607.json")


panel = (gpd.read_file(adm)
        .merge(df, left_on ='ADM2_PT' , right_on = 'district')
        [['private_companies','frelimo','time2natcap_roads',"y", 
          'geometry','population_density', 'district']]
        )


for year in [2008,2020]:

    (panel
        .query(f"y == '{year}'")
        .to_crs(3857)
        .drop(columns = ['frelimo'])
        .assign(geometry = lambda x: x['geometry'].simplify(
            tolerance= 1000 ))
        .assign(time2natcap_roads=  lambda x: x['time2natcap_roads'].round(3))
        .assign(population_density= lambda x: x['population_density'].round(3))
        .rename(columns = {'time2natcap_roads':"Travel time to capital (h)",
                           'private_companies':"Private Companies",
                           "population_density": "Population density",
                           "district": "District name",
                           "y":"Year"
                           })
        [['Year',"District name",'Population density',
         'Travel time to capital (h)', 'Private Companies', 
          "geometry"]]
        ).explore("Private Companies").save(HERE/Path("assets",
                                                      "maps",
                                                      f"adm2_{year}.html"))



