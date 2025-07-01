# Augmented Travel API
A backend service for autonomous ridesharing routing, built using the Google Maps Platform. Supports multi-stop routing, dynamic ride insertion, and route cost estimation.

## Features
- Dynamic multi-stop route updates
- Real-time trip insertion and rerouting
- Trip cost (time/distance) evaluation and management for fleet level management
- 3D Visualization of POI landmarks (e.g., chapels, markets)
- Narration service that updates users on:
  - Current route progress
  - Local weather forecasts
  - Nearby POI history and fun facts

## Tech Stack
- Python 3.11+
- Google Maps Platform
- Frontend (planned) : currently optimized for laptop display
- Scalability using parallel server architecture for route computation.

### Notes
- This service is a hybrid between continuous-time- and event- driven application. 
- From the frontend and local device, the service should take the user(driver)'s current position. This is simulated in this application.
- User trip data is currently stored in local database using SQLite. 

### Pre-requisites
- Python 3.11+
- Google Maps API Key

### Installation
```bash
git clone https://github.com/Andrew-JH-Park/augmented-travel-api.git
cd augmented-travel-api
pip install -r requirements.txt
```

### .env file
Save environmental variable file .env in the following format in the root folder.
```bash
# .env
GOOGLE_MAPS_API_KEY=AI...YOUR KEY HERE
DEBUG=True
PORT=8000
```