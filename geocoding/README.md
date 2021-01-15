About geoload.py:
1) It read addresses from local file
2) update database table (Locations.address)
3) send request to Google Maps API (if api_key != False) 
3) push the result to database table (Locations.geodata)

About geodump.py:
1) Connect to database table with the results from Google Maps API
2) open where.js
3) push latitude, longitude and formatted address from database to where.js

About where.html:
Creates a single page with the markers of our addresses on map


  
