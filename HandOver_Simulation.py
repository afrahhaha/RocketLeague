from skyfield.api import EarthSatellite,load,wgs84
import numpy as np
import matplotlib.pyplot as plt

# TLE for ISS 
line1 = "1 25544U 98067A   25305.52050362  .00011974  00000-0  21987-3 0  9990"
line2 = "2 25544  51.6344 346.5423 0004933   5.4437 354.6605 15.49679820536468"
sat = EarthSatellite(line1, line2, "ISS (ZARYA)") #defines the satellite

#initialize vectors
t=[]
sat_latitude=[]
sat_longitude=[]
current_visible=[]
previous_visible=[]
handover_log=[]

# Load TLE file
# stations_url = 'iss.tle'
# satellites = load.tle_file(stations_url)
# satellite = satellites[0]

# Load timescale
ts = load.timescale()
# t0 = ts.utc(2025, 11, 2, 0, 0)
# t_end = ts.utc(2025, 11, 2, 3, 0)

# Define ground stations 
station_A = wgs84.latlon(12.9716, 77.5946, 0.9)   # Bengaluru
station_B = wgs84.latlon(8.5421, 76.9366, 0.9)   # Trivandrum
stations = {'Bengaluru': station_A, 'Trivandrum': station_B}

#plotting in real time
plt.ion()
fig, ax = plt.subplots()

i=1;
for i in range(1,181):
    t = ts.utc(2025, 11, 7,23,i) 

    # Compute positions
    geocentric = sat.at(t)
    subpoint = geocentric.subpoint()

    lat = subpoint.latitude.degrees
    lon = subpoint.longitude.degrees
    alt = subpoint.elevation.km

    sat_latitude.append(lat)
    sat_longitude.append(lon)

    # create new frame
    # ax.clear()
    # ax.plot(sat_longitude,sat_latitude)
    # ax.legend()
    # ax.grid(True)
    # ax.set_xlabel('Latitude')
    # ax.set_ylabel('Longitude')
    # ax.set_title("ISS Ground Track for 3 Hours")

    #plt.show()

    visibility={}
    for name, station in stations.items():
        difference = sat - station      #finds the relative position of the sat with respect to the station.
        topocentric = difference.at(t)
        alt, az, distance = topocentric.altaz() 
        visibility[name] = alt.degrees> 10  # visible if above 10° elevation
    
    print(f"Time: {t.utc_datetime()}, Visibility: {visibility}")
    
    current_visible = [name for name, v in visibility.items() if v] #stores the ground stations that can view the satellite.
    if current_visible != previous_visible:
        print(f"HANDOVER at {t.utc_datetime()} --> {current_visible}")
        handover_log.append((t.utc_datetime(), current_visible))
        previous_visible = current_visible

    # Plot
    ax.clear()
    ax.plot(sat_longitude, sat_latitude, 'b', label='ISS Ground Track')
    ax.scatter(lon, lat, color='red', label='Current Position')
    ax.scatter([77.5946, 76.9366], [12.9716, 8.5421], color='green', marker='^', label='Ground Stations')
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_title("Handover Graph between Ground Stations")
    
    plt.pause(0.1)
    continue;





# from skyfield.api import Topos

# # Define ground station (example: Bangalore)
# gs = Topos(latitude_degrees=12.9716, longitude_degrees=77.5946)

# difference = satellite - gs
# altaz = difference.at(times).altaz()

# elevation = altaz[0].degrees

# for t, e in zip(times, elevation):
#     if e > 0:
#         print(f"{t.utc_iso()} — Visible (elevation {e:.1f}°)")
