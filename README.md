# F1-Data-Analysis
This program analyzes the data from Formula 1 to create graphs and compare differences in tire degradation over different stints.

# Project Goal
Create an easy to use F1 data analysis tool

# MVP
- Retrieve and verify F1 data
- Determine which data is needed for analysis
- Allow use of the product

# Future plans
- Compare tire compounds and stints
- Analyze tire degradation trends
- Create a ranking of drivers based on average lap times

# Tech Stack
- What language are you writing in?
Python
- What libraries, packages, or external tools do you need?
I will need the following libraries:
FastF1: Retrieve Formula 1 race data, including lap times, tyre compounds, and tyre age.
Pandas: Organize, filter, and analyze the race data.
Matplotlib: Create graphs and visualizations to compare lap times and tire degradation.
Python
- How will you store data? For an MVP, a plain text / JSON / CSV file is often enough, so there's no need to jump to a full database.
I will store the data using CSV files
- If you're pulling data from an external source, what is it and how will you access it? (See the APIs & External Data Sources post on Ed.)
I will use FastF1 to retrieve historical race information, and I can access it through Python by installing and importing the FastF1 library.
