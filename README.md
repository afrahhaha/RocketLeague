# RocketLeague
Assignment submission for Rocket League -Avionics sig

The link to my tinkercad submissions are here:
Task_1: https://www.tinkercad.com/things/eawZW6LQ0fM/editel?returnTo=%2Fdashboard&sharecode=fOnbhJLf8IrwkB0u4JmM-FzWl5wEIzXrhUbVIpVkmIQ 
Task_2: https://www.tinkercad.com/things/lKAOquQibA7/editel?sharecode=B3Yp8Zofydtt71hg8PQi2FqUPbz468YAo9Oj-WLG6Yk
Task_3: https://www.tinkercad.com/things/k4Hwa6etq5L/editel?sharecode=ai5RcPW1sPqFH2a5IRL0nhPPKm2wDeBtQbfo308rRis
Task_4: https://www.tinkercad.com/things/9C9aE0aqXwJ/editel?sharecode=rn6gZdgCpDnyOH6bd62WIiIB33__HyEneyWRjF0F7VM

x=numpy.array(0,100,1) - creates an array x containing numbers from 1 to 100
array- optimized for numerical computation; 
ax= figure.add_subplot(nrows,ncloumns,index)- adds axes to the figure
tab=np.eye(100,100)= creates I matrix
temperature=random.uniform(20,40)- returns a random floating number between 20 and 40

1.download TLE data from Space-track.org
 	- the TLE data is obtained from ELSET(element set)
 	- ISS(Zarya)-25544-Low Earth Orbit~400 km
TLE- contains orbital elements of a satellite
 	Inclination (°) ; RAAN (°); Eccentricity ;Argument of perigee (°); Mean; anomaly (°);Mean motion (rev/day); Epoch (Julian date)

2. Propogate the orbit
**-** use skyfield.api

 	1) define the TLE data of the satellite
 	sat=EarthSatellite(line1,line2,"ISS(ZARYA)"
 	2) define the timescale for propagation by loading UTC times
 	3)find position of the satellite at t in timescale
 		geocentric = the satellite’s ECI position vectors at the given times.

different coordinates for the representation of position vector of the satellite
1.Earth-Centered,Earth-Fixed(ECEF): the x,y,z coordinates taking the centre of earth as origin
2.Geodetic Coordinates:(Latitude, Longitude,Height):
uses reference ellipsoid like WGS 84.
 	Latitude (lat/Φ): The angle north or south of the equator.
 	Longitude (lon/λ): The angle east or west of the prime meridian.
 	Ellipsoidal height (h): The altitude above the reference ellipsoid surface
3.Keplerian Elements: Inclination (°) ; RAAN (°); Eccentricity ;Argument of perigee (°); Mean; anomaly (°);Mean motion (rev/day); Epoch (Julian date)

The degree of visibility of satellite from any ground station:
⦁	topocentric.at() : includes the position of the satellite in the staion's reference frame; stores in the form of 3D vectors(x,y,z)
⦁	in theory: visibility exists above 0 degree. but practically for a LEO 5-10 is a safe region to assume visibility at.


