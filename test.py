import numpy as np
import xarray as xr
import pygrib

# Open the GFS GRIB2 file
gfs_file = 'gfs_data.grb2'
grbs = pygrib.open(gfs_file)

# Extract 2m temperature data
temp_grb = grbs.select(name='2 metre temperature')[0]
temp_data = temp_grb.values - 273.15  # Convert to Celsius

# Get latitude and longitude arrays
lats, lons = temp_grb.latlons()

# Save the temperature data, latitude, and longitude to a NetCDF file
output_file = 'gfs_temp_data.nc'
ds = xr.Dataset(
    {'temperature': (['lat', 'lon'], temp_data)},
    coords={'lat': (['lat'], lats[:, 0]), 'lon': (['lon'], lons[0, :])},
)
ds.to_netcdf(output_file)
