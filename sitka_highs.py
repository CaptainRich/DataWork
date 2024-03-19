""" A script to work with weather data from Sitka, Alaska. """

from pathlib import Path         # Needed for directory operations
import csv                       # Needed for CSV operations
import matplotlib.pyplot as plt  # For data visualization


# Set the pathname and read the entire file into a "list" (lines), breaking on 
# each line.
path = Path( 'weather_data/sitka_weather_07-2021_simple.csv' )
lines = path.read_text( encoding='utf-8' ).splitlines()

# Create a 'reader' object that can be used to parse each line from the file.
reader = csv.reader( lines )

# Get the next line (the first) from the file, which contains the headers.
header_row = next( reader )      # Data is returned as a "list"
print( header_row )

# Extract the 'high' temperatures from each line of the file.  This data is
# item 4 (zero based) on each line.
highs = []           # Start with an empty list
for row in reader:
    high = int( row[4] )
    highs.append( high )

print( 'Daily high temperatures are: \n', highs )

# Plot the high temperature data
plt.style.use(  'seaborn-v0_8' )
fig, ax = plt.subplots()
ax.plot( highs, color='red' )

# Format the plot
ax.set_title( "Daily High Temperatures, July 2021", fontsize=24 )
ax.set_xlabel( '', fontsize=16 )
ax.set_ylabel( 'Temperature (F)', fontsize=16 )
ax.tick_params( labelsize=16)

plt.show()

