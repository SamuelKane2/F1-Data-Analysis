import fastf1
from fastf1 import plotting
from fastf1 import utils
from fastf1.exceptions import FuzzyMatchError

from matplotlib import pyplot
from matplotlib.pyplot import figure
from matplotlib.ticker import FuncFormatter

def format_laptime(seconds, position):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f'{minutes}:{remaining_seconds:06.3f}'

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
    grand_prix = input('Enter a Grand Prix: ').strip()

    try:
        event = fastf1.get_event(year, grand_prix)
        break
    except FuzzyMatchError:
        print('Grand Prix data not found, try again.')

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

driver_laps = race.laps.pick_drivers(driver).pick_accurate()

# -----------Analyzing the data----------- #
driver_laps = driver_laps[['LapNumber', 'LapTime', 'Stint', 'Compound', 'TyreLife']]

stints = driver_laps.groupby('Stint')

# Average lap time per stint #
for stint_num, stint_data in stints:
    secs = stint_data['LapTime'].mean().total_seconds()
    mins = secs // 60
    average_lap_time = f'{mins:g}:{secs-mins*60:.3f}'
    compound = str(stint_data['Compound'].iloc[0]).lower()
    print(f'Stint #{stint_num} was on the {compound} tire had an average laptime of {average_lap_time}')

print()

# Difference in average lap time for each stint #
for stint_num, stint_data in stints:
    stint_data = stint_data.sort_values('LapNumber')

    lap_times = stint_data['LapTime'].dt.total_seconds()
    average_change = lap_times.diff().mean()

    compound = str(stint_data['Compound'].iloc[0]).lower()
    print(f'Stint #{stint_num} was on the {compound}: Average lap time change of {average_change:+.3f} seconds per lap')

# Saves the laps to a CSV file
driver_laps.to_csv(f'../data/{driver}_laps.csv', index=False)

# -----------Creating the graph----------- #

#Enabling something
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

fig, ax = pyplot.subplots()
style = plotting.get_driver_style(identifier=driver,style=['color','linestyle'], session=race)
lap_times = driver_laps['LapTime'].dt.total_seconds()
ax.plot(driver_laps['LapNumber'], lap_times, **style, label=driver)

ax.set_xlabel('Lap Number')
ax.set_ylabel('Lap Time')
ax.legend()
pyplot.show()