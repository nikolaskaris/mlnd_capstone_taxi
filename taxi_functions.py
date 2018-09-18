import numpy as np

# Haversine distance formula
def distance(lat1, lat2, lon1,lon2):
    p = 0.017453292519943295 # Pi/180
    a = 0.5 - np.cos((lat2 - lat1) * p)/2 + np.cos(lat1 * p) * np.cos(lat2 * p) * (1 - np.cos((lon2 - lon1) * p)) / 2
    return 0.6213712 * 12742 * np.arcsin(np.sqrt(a))

# Eliminate samples with latitude/longitude coordinates outside NYC boundary
def boundaryBox(df, BB):
    return (df.pickup_longitude >= BB['min_lng']) & (df.pickup_longitude <= BB['max_lng']) & \
           (df.pickup_latitude >= BB['min_lat']) & (df.pickup_latitude <= BB['max_lat']) & \
           (df.dropoff_longitude >= BB['min_lng']) & (df.dropoff_longitude <= BB['max_lng']) & \
           (df.dropoff_latitude >= BB['min_lat']) & (df.dropoff_latitude <= BB['max_lat'])


# Is location
# Used to create airport pickup/dropoff features
# takes as argument 'location', which is a dictionary with keys:
#               'min_lng', 
#               'max_lng', 
#               'min_lat', 
#               'max_lat'

def isLocation(lat, lng, location, range = 0.5):
    return (distance(location['lat'], location['lng'], lat, lng) < range)

    
def isAirport(lat, lng, airport_name):
    
    if lat>=nyc_airports[airport_name]['min_lat'] and lat<=nyc_airports[airport_name]['max_lat'] and lng>=nyc_airports[airport_name]['min_lng'] and lng<=nyc_airports[airport_name]['max_lng']:
        return 1
    else:
        return 0