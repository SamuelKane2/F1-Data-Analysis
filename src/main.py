import fastf1
from fastf1 import plotting
from fastf1 import utils
from fastf1.exceptions import FuzzyMatchError

from matplotlib import pyplot
from matplotlib.pyplot import figure

import numpy
import pandas

fastf1.Cache.configure(cache_dir='cache')
fastf1.set_log_level('WARNING')

# User inputs, validates each input before moving to the next
print('Welcome, please input the year, Grand Prix, session, and driver you want data from')

# -----------Year validation----------- #
while True:
    try:
        year = int(input('Enter a year: ').strip())
        event = fastf1.get_event_schedule(year)
        if event.empty:
            print('No season data found for that year, try again.')
            continue
        else:
            break
    except ValueError:
        print('Please enter a valid year')

# -----------Grand Prix and validation----------- #
while True:
    grand_prix = input("Enter a Grand Prix: ").strip()

    try:
        event = fastf1.get_event(year, grand_prix)
        break
    except FuzzyMatchError:
        print("Grand Prix data not found, try again.")

# -----------Session validation----------- #
available_sessions = event.filter(regex='^Session[1-5]$').values.flatten()
available_sessions = [s for s in available_sessions if pandas.notna(s)]

session_options = ', '.join(available_sessions)

while True:
    session_name = input(f'Enter a session ({session_options}): ').strip().upper()

    try:
        session = event.get_session_name(session_name)
        break
    except ValueError:
        print('Session not available for this Grand Prix, try again.')

# Creating the race
print('Please wait while the weekend data is loaded')
race = fastf1.get_session(year, grand_prix, session)
race.load(laps=True, telemetry=True, weather=False, messages=False)

# -----------Driver validation----------- #
while True:
    driver = input('What driver do you want to analyze (Ex: Ham, Ver)? ').strip().upper()
    if driver not in race.laps['Driver'].unique():
        print('Driver not found in this session, try again.')
        continue
    break

while True:
    want_accurate = input('Do you want to exclude inaccurate laps (yes, no)? ')
    if (want_accurate.lower() == 'yes'):
        accurate = True
        break
    elif (want_accurate.lower() == 'no'):
        accurate = False
        break
    else:
        print('yes or no please')

# Picks out accurate laps for the driver
if (accurate):
    driver_laps = race.laps.pick_drivers(driver).pick_accurate()
else:
    driver_laps = race.laps.pick_drivers(driver)

# -----------Organize Data----------- #
# Need, 'LapTime', 'LapNumber', 'Stint', 'Compound'
#x = lap
#y = laptime divided up by stints also somehow
driver_laps = driver_laps[['LapNumber', 'LapTime', 'Stint', 'Compound']]
print(driver_laps)

# Saves the laps to a CSV file
driver_laps.to_csv(f'../data/{driver}_laps.csv', index=False)