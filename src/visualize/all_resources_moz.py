# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:58:18 2023

@author: fs.egb
"""

import geopandas as gpd
from pathlib import Path
import pandas as pd
import sys
from shapely.geometry import Polygon
from matplotlib.lines import Line2D
HERE = Path(__file__).parent.parent.parent.absolute()
import contextily as cx
import matplotlib.pyplot as plt



FLEXI = Path(r"C:\Users\fs.egb\mine_mapper_project")

sys.path.insert(0, str(FLEXI/Path("src", "features")))

import flexi 



def add_usgs_and_giants(current_iso, HERE):  
    
    JMP = FLEXI = Path(r"C:\Users\fs.egb\jmp")
    
    ugsg_facilities = (gpd.read_file(JMP/"data"/"external"/"usgs"/"Africa_GIS_full"/
                                      "a. Africa_GIS Shapefiles"/"AFR_Mineral_Facilities.shp"/
                                      "AFR_Mineral_Facilities.shp")
                          .drop_duplicates()
                          .to_crs(3857)
                          .assign(iso3 = lambda x: x['FeatureUID'].str[:3])
                          .query('iso3 in @current_iso')
                          .drop(columns = ['Latitude', 'Longitude'])
                          .assign(type_ = "USGS Year book 2017/2018")
                          .rename(columns = {'FeatureNam':"mine_name"})
                          .assign(type_ = 'mine')
                          )
    
    
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


    
    return  

