# $`\textcolor{blue}{\text{Data Work}}`$
A set of scripts and files illustrating working with data sets. This includes
CSV and JSON files.
Richard Ay (March 2024, *updated March 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Images](#Images)

## Setup

## Envirionment
A virtual environment is created so that the installation of matplotlib 
remains local to this subdirectory, and does affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "DataWork" --upgrade-deps --prompt="DataWork"'**

To start/stop the virtual environment, use the commands: **'DataWork\scripts\activate'** 
or **'deactivate'**. Once activated, the virtual environment will change the (terminal) 
prompt from (PS) to (DataWork).

After starting the virtual environment, matplotlib  can be installed 
with the commands:  
**'python -m pip install matplotlib'**  

Subsequently the installations can be verified with the command:   
**'python -m pip show matplotlib'**  


## Usage
From VSCode, by issuing the commands (note the suffix ".py' is required)  
- 'python sitka_highs.py'  
  


## References
1. Python Crash Course, Eric Matthes, No Starch Press, 2023. Chapters 12-15.  


## File List
**sitka_highs.py** - a script to manipulate weather data from Sitka, Alaska.  

**/weather_data** - a subdirectory containing data files used by the scripts.


## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- csv 
- matplotlib

 