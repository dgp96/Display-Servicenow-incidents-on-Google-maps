Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from geopy.geocoders import Nominatim
>>> geolocator = Nominatim(user_agent="myarsenal96@gmail.com")
>>> location = geolocator.geocode("324 South State Street, Salt Lake City,UT")
>>> print(location.address)
324, State Street, The Granary, Rose Park, Salt Lake City, Salt Lake County, Utah, 84111, United States of America
>>> print((location.latitude, location.longitude))
(40.76216361467712, -111.88833364912172)
>>> print(location.raw)
{'place_id': 269606625, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way', 'osm_id': 287312895, 'boundingbox': ['40.762113614677', '40.762213614677', '-111.88838364912', '-111.88828364912'], 'lat': '40.76216361467712', 'lon': '-111.88833364912172', 'display_name': '324, State Street, The Granary, Rose Park, Salt Lake City, Salt Lake County, Utah, 84111, United States of America', 'class': 'place', 'type': 'house', 'importance': 0.711}
>>> print(location)
324, State Street, The Granary, Rose Park, Salt Lake City, Salt Lake County, Utah, 84111, United States of America
>>> 
