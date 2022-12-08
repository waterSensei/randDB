from pprint import pprint
from random import randrange
import googlemaps

#GOOGLE API KEY
API_KEY = 'AIzaSyDAFjc7-YR7r4nL7w6DT67yTYMlQSIIYqM'
#Canberra coordinate range
lo_range = [149.001436,149.187774]
la_range = [-35.475038,-35.151304]

def getaddress():
    #Generate random longitude and latitude within the range
    randlo = randrange(int(1000000*(lo_range[1]-lo_range[0])))/1000000+lo_range[0]
    randla = randrange(int(1000000*(la_range[1]-la_range[0])))/1000000+la_range[0]
    coordinate = str(randla)+','+str(randlo)
    #Initialise geocode
    map_client = googlemaps.Client(API_KEY)
    response = map_client.geocode(coordinate)
    print(coordinate)
    #Only reture location
    if response[0]['geometry']['location_type'] == 'ROOFTOP':
        print(response[0]['geometry']['location_type'])
        return {'Address':response[0]['formatted_address']}
    else:
        getaddress()



# map_client = googlemaps.Client(API_KEY)
# response = map_client.geocode('-35.461985,149.06133300000002')
# print(response[0]['geometry']['location_type']!= 'ROOFTOP')