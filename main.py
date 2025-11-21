import xarray as xr

xrds = xr.open_dataset("era5_wind_1980_01.nc")

# ['number', 'valid_time', 'latitude', 'longitude', 'expver', 'u10', 'v10', 'u100', 'v100']
xrds.data_vars
df = xrds.to_dataframe()
# salen los datos teniendo variables tiempo, latitud y longitud como indice
df = df.reset_index()

xrds.variables()

xrds['v10'][:,13,74].plot()