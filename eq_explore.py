""" A script to rewrite a JSON file of earthquake data to make the data
    more readable to human eyes. """

from pathlib import Path      # for directory operations
import json                   # for JSON file I/O
import plotly.express as px   # for plotting the data on the world map

# Set our 'debug' flag to control status printing.
debug = True

# Read the earthquake data as a JSON string and convert it to 
# a Python object.

path        = Path( 'eq_data/eq_data_30_day_m1.geojson' )
contents    = path.read_text( encoding='utf-8' )        # read the data
all_eq_data = json.loads( contents )                    # convert to a Python object, a dictionary

# Generate a list of all the earthquakes, and output the length of the list
all_eq_dicts = all_eq_data[ 'features' ]
if debug:
    print( f"There are {len(all_eq_dicts)} earthquake records in this file." )

# Generate a list of all of the earthquake magnitudes, longitudes, and latitudes.  
# Print the list and its length.
magnitudes, longitudes, latitudes, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    tit = eq_dict['properties']['title']

    magnitudes.append( mag )
    longitudes.append( lon )
    latitudes.append( lat )
    eq_titles.append( tit )

if debug:
    print( f"There are {len(magnitudes)} magnitude records in this file, they are:" )
    print( magnitudes[:15] )   # Print just the first 15 magnitude values using a 'slice'
    print( 'The first five longitudes & latitudes are:' )
    print( longitudes[:5] )
    print( latitudes[:5] )

# Now output a more readable version of the data
if debug:
    path              = Path( 'eq_data/readable_eq_data.geojson' )
    readable_contents = json.dumps( all_eq_data, indent=4 ) # create a string with a JSON representation of the data
    path.write_text( readable_contents )

# Setup the plot
title = 'Global Earthquakes'
fig = px.scatter_geo( lat=latitudes, lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,
                     color_continuous_scale='Viridis',
                     labels={'color: Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles, )
fig.show()
