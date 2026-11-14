import fastf1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot
from matplotlib.pyplot import figure

import numpy
import pandas

fastf1.Cache.enable_cache('cache')

# Loading Session Data
race = fastf1.get_session(2025, 'Monza', 'R')
race.load(laps=True, telemetry=False, weather=False, messages=False, livedata=None)

driver = 'PIA'

driver_laps = race.laps.pick_drivers('PIA').pick_quicklaps().reset_index()
driver_laps = driver_laps[['LapNumber', 'LapTime', 'IsAccurate']]

print(driver_laps)