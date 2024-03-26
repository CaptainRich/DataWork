""" A script to work with weather data from Sitka, Alaska. """

from pathlib import Path         # Needed for directory operations
import csv                       # Needed for CSV operations
import matplotlib.pyplot as plt  # For data visualization
from datetime import datetime    # To process date information


# Set the pathname and read the entire file into a "list" (lines), breaking on 
# each line.
#path = Path( 'weather_data/sitka_weather_07-2021_simple.csv' )
path = Path( 'weather_data/sitka_weather_2021_simple.csv' )
#path = Path( 'weather_data/death_valley_2021_simple.csv' )
lines = path.read_text( encoding='utf-8' ).splitlines()

# Create a 'reader' object that can be used to parse each line from the file.
reader = csv.reader( lines )

# Get the next line (the first) from the file, which contains the headers.
header_row = next( reader )      # Data is returned as a "list"
print( header_row )

# Extract the 'high' and 'low' temperatures from each line of the file.  This 
# data is item 4 & 5 (zero based) on each line. Also extract the dates for the 
# observations, which is item 2 on each line.
highs, lows, dates = [], [], []           # Start with an empty lists
for row in reader:
    current_date = datetime.strptime( row[2], '%Y-%m-%d' )  

    try:
        high = int( row[4] )
        low = int( row[5] )
    except ValueError:
        print( f"Missing data for {current_date}" )
    else:
        dates.append( current_date )
        highs.append( high )
        lows.append( low )

#print( 'Daily high temperatures are: \n', highs )

# Plot the high temperature data.  "fig" represents the entire figure (screen),
# which can contain a number of plots. "ax" represents a single plot.
plt.style.use(  'seaborn-v0_8' )
fig, ax = plt.subplots()
ax.plot( dates, highs, color='red', alpha=0.5 ) #Alpha sets the transparency(0-1)
ax.plot( dates, lows, color='blue', alpha=0.5 )
ax.fill_between( dates, highs, lows, facecolor='blue', alpha=0.1 )
#fig, ax2 = plt.subplots()

# Format the plot
#ax.set_title( "Daily High Temperatures, July 2021", fontsize=24 )
ax.set_title( "Daily High/Low Temperatures,  2021", fontsize=24 )
ax.set_xlabel( '', fontsize=16 )
fig.autofmt_xdate()        # Draw the dates diagonally to avoid overlap
ax.set_ylabel( 'Temperature (F)', fontsize=16 )
ax.tick_params( labelsize=16)

plt.show()

