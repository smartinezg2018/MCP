import pandas as pd
import numpy as np
import datetime
import xarray as xr
import os
class analysis:
    def __init__(
            self,
            path,
            latitude,  
            longitude,  
        ):
        # Definicion de las variables
        self.path = path
        self.latitude =  latitude
        self.longitude =  longitude

    # funciones
    def files_read(self,):
        files = os.listdir(self.path)
        # Solo se retienen archivos nc
        dict_files = {
            'date':list(),
            'link':list()
        }

        for file in files:
            if '.nc' in file:
                # generacion link
                link = os.path.join(
                    self.path,
                    file
                )
                #Formateo fecha
                year = file.split('_')[2]
                month = file.split('_')[3].split('.')[0]
                date = pd.to_datetime(year + '/' + month)
                # Almacenamiento
                dict_files['date'].append(date)
                dict_files['link'].append(link)
        # Creacion del dataframe
        df_files_reference = pd.DataFrame(dict_files)
        df_files_reference.set_index(
            'date',
            drop=True,
            inplace=True
        )
        return df_files_reference.sort_index()
    
    def retrieveData(
            self,
        ):
        """
        gets initial year, final year, latitude and longitude,
        after that it creates a data frame with all the information required
        by the parameters
        """
        # Archivos a leer
        mask = self.files_read()
        final = xr.DataArray()
        for link in mask['link'].to_numpy():
            xr.open_dataset(link)




        






        
        

          

