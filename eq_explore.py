""" A script to rewrite a JSON file of earthquake data to make the data
    more readable to human eyes. """

from pathlib import Path      # for directory operations
import json                   # for JSON file I/O

# Read the earthquake data as a JSON string and convert it to 
# a Python object.

path        = Path( 'eq_data/eq_data_1_day_m1.geojson' )
contents    = path.read_text( encoding='utf-8' )        # read the data
all_eq_data = json.loads( contents )                    # convert to a Python object, a dictionary

# Now output a more readable version of the data
path              = Path( 'eq_data/readable_eq_data.geojson' )
readable_contents = json.dumps( all_eq_data, indent=4 ) # create a string with a JSON representation of the data
path.write_text( readable_contents )
