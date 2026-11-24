# F1-Data-Analysis
This program analyzes the data from Formula 1 to create graphs and compare differences in tire degradation over different stints.

## The Problem
Create an easy to use F1 data analysis tool

## How it Works
1. The user selects a year, Grand prix, session, and a driver
2. FastF1 retrieves the requested weekend data
3. Pandas filters and organizes the driver's data
4. The program calculates the average lap times and compares tire performance between stints
5. Matplotlib creates a graph of the driver's lap times.

## Tech Stack
Language: Python 3.12

Libraries:
- FastF1 – Retrieves Formula 1 race data.
- Pandas – Organizes and analyzes race data.
- Matplotlib – Creates graphs and visualizations.

External data source: Formula 1 timing data through FastF1.

## Setup Instructions
#### Prerequisites
- Python 3.12
- Git
- A Python IDE
- An F1 account
  - Unfortunately FastF1 requires an F1 account to get the data

#### Installation
- Clone the repository
- Install FastF1, Pandas, and Matplotlib
- Run the program using an IDE

## Example
Welcome, please input the year, Grand Prix, session, and driver you want data from  
Enter a year: 2026  
Enter a Grand Prix: las vegas
Enter a session (Practice 1, Practice 2, Practice 3, Qualifying, Race): r  
Please wait while the weekend data is loaded  
What driver do you want to analyze (Ex: Ham, Ver)? pia  

Stint #1 was on the soft tire had an average laptime of 1:38.641  
Stint #2 was on the medium tire had an average laptime of 1:37.273  

Stint #1 was on the soft: Average lap time change of -0.125 seconds per lap  
Stint #2 was on the medium: Average lap time change of -0.157 seconds per lap  

## Roadmap
- [x] Retrieve Formula 1 race data
- [x] Validate user inputs
- [x] Filter lap data by driver
- [x] Filter inaccurate laps
- [x] Calculate average lap times per stint
- [x] Calculate average lap-time change per lap
- [x] Create lap-time visualizations
- [ ] Compare tire degradation across multiple drivers
- [ ] Improve data visualization and presentation

## Demo
