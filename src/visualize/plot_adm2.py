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


import geopandas as gpd
from pathlib import Path
import pandas as pd
import sys
from shapely.geometry import Polygon
from matplotlib.lines import Line2D
import contextily as cx
import matplotlib.pyplot as plt
import folium


FLEXI = Path(r"C:\Users\fs.egb\mine_mapper_project")

sys.path.insert(0, str(FLEXI/Path("src", "features")))

def get_giant_fields(current_iso, HERE):  
    
    JMP = FLEXI = Path(r"C:\Users\fs.egb\jmp")
 
    df = (pd
            .read_csv(JMP/Path("data","external","nat_resources",
                             "giant_gas_discoveries",
                               "giant_fields_2018.csv"))
                 .query('ISO in @current_iso')
                .rename(columns = {'ISO':"iso3",
                                   "FLD_NAME": "mine_name"})
                )
    
    giant_fields =  (gpd.GeoDataFrame(df, geometry = 
                                    gpd.points_from_xy(df['LON_DD'], df['LAT_DD']),
                                    crs = 4326)
                    .drop(columns = ['REG_CODE', 'REG_NAME',
                            'WB_REGION', 'COUNTRY', 
                            'CountrynameWEO', 'weo_code', 'STATE',
                            'LAT_DD', 'LON_DD', 'SIZE_CLASS_CODE'])
                    [['FIELD_ID',"mine_name",'iso3', 'ON_OFF_LOC',
                      'year',"geometry",'FIELD_TYPE']]
                        .rename(columns = {'ON_OFF_LOC':"type_"})
                        .to_crs(3857)
                        .assign(type_ = 'discovery')
        
                    )

    
    return  giant_fields


def get_drilling_holes(HERE):
    drilling_path = HERE/Path("data","interim", "nat_resources","inp_drilling_holes.geojson")


    drilling_holes = (gpd
                      .read_file(drilling_path).to_crs(3857)
                      .assign(type_ = 'drilling_holes')
                       # .assign(compl_dat = lambda x: 
                       #         x['Completion\rdate']
                       #          .apply(lambda y: '01-Jan-' + y  if len(x) == 2 else y))
                      .assign(compl_dat = lambda x: 
                              pd.to_datetime(x['Completion\rdate']), 
                                             format='%d-%b-%y')
                          
                    .assign(year = lambda x: x['compl_dat'].dt.year)
                   
                      )


    drilling_holes.loc[drilling_holes['year'] > 2018, 'year'] -= 100
    
    return drilling_holes

                      


df = pd.read_parquet(HERE/Path("data","processed","adm2.parquet.gzip")  )

adm = HERE/Path("data","external","adm",  "moz_admbnda_adm2_ine_20190607.json")


panel = (gpd.read_file(adm)
        .merge(df, left_on ='ADM2_PT' , right_on = 'district')
        [['private_companies','frelimo','time2natcap_roads',"y", 
          'geometry','population_density', 'district']]
        )


gas_fields = get_giant_fields( "MOZ", HERE)

drilling_holes =  get_drilling_holes(HERE)




# ,2020

for year in [2008,2020]:

    m =     (panel
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
            ).explore(column = "Private Companies",
                      legend=True,  # show legend
                      k=10,  # use 10 bins
                       legend_kwds=dict(colorbar=False),  # do not use colorbar
                       name="District activities",  # name of the layer in the map
                      )
                      
                      
    mm = (gas_fields
              .query(f"year <= {year}")
               .explore(
             m=m,  # pass the map object
             color="#DB444B",  
             marker_kwds=dict(radius=5, fill=True),  # make marker radius 10px with fill
             tooltip="mine_name",  # show "name" column in the tooltip
             tooltip_kwds=dict(labels=False),  # do not show column label in the tooltip
             name= "Gas fields",  # name of the layer in the map
            )
            )
    
    
    (drilling_holes.query(f"year <= {year}")
              [['geometry','Well long\rname']]
             .dropna(how = "any")
             .rename(columns = {"Well long\rname":"Well name"})
                .explore(
             m= mm,  # pass the map object
             color= "#006BA2",  
             marker_kwds=dict(radius=5, fill=True),  # make marker radius 10px with fill
             tooltip="Well name",  # show "name" column in the tooltip
             tooltip_kwds=dict(labels=False),  # do not show column label in the tooltip
             name="Drilling holess",  # name of the layer in the map
            ))
                
    folium.TileLayer("CartoDB positron", show=False).add_to(
    mm
    )  # use folium to add alternative tiles
    folium.LayerControl().add_to(mm)  # 
                    
    
                    
                
    mm.save(HERE/Path("assets",
                             "maps",
                            f"adm2_{year}.html"))
  
    
    


    
                      
#     groceries.explore(
#     m=m,  # pass the map object
#     color="red",  # use red color on all points
#     marker_kwds=dict(radius=5, fill=True),  # make marker radius 10px with fill
#     tooltip="Address",  # show "name" column in the tooltip
#     tooltip_kwds=dict(labels=False),  # do not show column label in the tooltip
#     name="groceries",  # name of the layer in the map
# )              
                      
    
    
    
    
    
    
#     .save(HERE/Path("assets",
#                                                           "maps",
#                                                           f"adm2_{year}.html"))
    


