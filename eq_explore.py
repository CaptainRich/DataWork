""" A script to rewrite a JSON file of earthquake data to make the data
    more readable to human eyes. """

from pathlib import Path      # for directory operations
import json                   # for JSON file I/O
import plotly.express as px   # for plotting the data on the world map
import datetime               # for date labeling of the plot

# Set our 'debug' flag to control status printing.
debug = True

# Read the earthquake data as a JSON string and convert it to 
# a Python object.

path        = Path( 'eq_data/eq_data_30_day_m1.geojson' )
contents    = path.read_text( encoding='utf-8' )        # read the data
all_eq_data = json.loads( contents )                    # convert to a Python object, a dictionary

# Generate a list of all the earthquakes, and output the length of the list
all_eq_dicts = all_eq_data[ 'features' ]
num_quakes = len(all_eq_dicts)
if debug:
    print( f"There are {num_quakes} earthquake records in this file." )

# Generate a list of all of the earthquake magnitudes, longitudes, and latitudes.  
# Print the list and its length.
magnitudes, longitudes, latitudes, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    magnitudes.append( eq_dict['properties']['mag'] )             # magnitude
    longitudes.append( eq_dict['geometry']['coordinates'][0] )    # longitude
    latitudes.append( eq_dict['geometry']['coordinates'][1] )     # latitude
    eq_titles.append( eq_dict['properties']['title'] )            # title (location)

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


# Get the first and last timestamps from the file of earthquake data
time1 = all_eq_dicts[0]['properties']['time']
time2 = all_eq_dicts[num_quakes-1]['properties']['time']

date1 = datetime.datetime.fromtimestamp( time1/1e3 )
date2 = datetime.datetime.fromtimestamp( time2/1e3 )

date_label = str(date2)[:10] + ' to ' + str(date1)[:10]

if debug:
    print( f"Earthquake 1 time/date: {time1}, {date1}" )
    print( f"Earthquake 2 time/date: {time2}, {date2}" )

# Setup the plot
title = 'Global Earthquakes: ' + date_label
fig = px.scatter_geo( lat=latitudes, lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,
                     color_continuous_scale='Viridis',
                     labels={'color: Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles, )
fig.show()
