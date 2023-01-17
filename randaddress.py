from random import randrange
import googlemaps

# GOOGLE API KEY
API_KEY = 'YOUR API KEY'
# Canberra coordinate range
lo_range = [149.001436, 149.187774]
la_range = [-35.475038, -35.151304]


def getaddress():
    """Generate random real address with Google geocode API

    Returns:
        String: Real address in Canberra
    """
    # Generate random longitude and latitude within the range
    randlo = randrange(
        int(1000000*(lo_range[1]-lo_range[0])))/1000000+lo_range[0]
    randla = randrange(
        int(1000000*(la_range[1]-la_range[0])))/1000000+la_range[0]
    coordinate = str(randla)+','+str(randlo)

    # Initialise geocode
    map_client = googlemaps.Client(API_KEY)
    response = map_client.geocode(coordinate)
    # pprint(response)
    # Only reture the address if the location type is 'ROOFTOP'
    if response[0]['geometry']['location_type'] == 'ROOFTOP' and response[0]['types'][0] == 'premise':
        return {'Address': response[0]['formatted_address']}
    else:
        return getaddress()
