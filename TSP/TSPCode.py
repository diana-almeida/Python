# TSP SOLVED FOR GPMOBILE

#WHAT YOU NEED
#     - API Key from Map Developer  ----> MyAppKey
#     - URL for map --------------------> Map
#     - Locations: latitudes and longitudes
import requests
import json

MyAppKey = "CcSdg2wnTcoUicENGXU0woOQmCigTzLk"

#-------------------------ROUTE POINTS---------------------------------
#--------- MAKE   IT  AN  API  WITH  XLSX  OR  GOOGLESHEETS -----------

route = {"locations":[]}
route['locations'].append( {"latLng":{"lat":36.1,"lng": -80.2412}})   # x es el numero de elementos que existen aqui
route['locations'].append( {"latLng":{"lat":35.9554,"lng":-80.0052}}) #325, Greensboro NC
route['locations'].append( {"latLng":{"lat":36.069,"lng":-79.7947}}) #327, High Point NC
route['locations'].append( {"latLng":{"lat":35.7989,"lng":-81.4337}})
#----------------------------------------------------------------------


#......................UPLOADING DATA FROM API...........................

url_Op = "http://open.mapquestapi.com/directions/v2/optimizedroute?key=" + MyAppKey
url_Ba = "http://open.mapquestapi.com/directions/v2/route?key=" + MyAppKey

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# making request #
r_Op = requests.post(url_Op, data=json.dumps(route), headers=headers)
r_Ba = requests.post(url_Ba, data=json.dumps(route), headers=headers)

# load json into praser #
r_json_Op = json.dumps(r_Op.json(), indent=2)
r_json_Ba = json.dumps(r_Ba.json(), indent=2)

# convert to python data structure #
data_Op = json.loads(r_json_Op)
data_Ba = json.loads(r_json_Ba)

# .......................................................................

#---------------------------MAP FEATURES---------------------------------

# Bounding Box #
def BoundingBox(data_Op):

	fit = "{lat1},{long1},{lat2},{long2}"
	bestfit = fit.format(lat1=data_Op['ul']['lat'],
		long1=data_Op['ul']['lng'], lat2=data_Op['lr']['lat'],
		long2=data_Op['lr']['lng'])

	return bestfit


# Shape #
def GetShape(data_Op):

	for x in data_Op['locations']:
		latLng = str(x['displayLatLng']['lat']) + ',' + str(x['displayLatLng']['lng'])

	return  latLng


# Changing variables #
shape_Ba = GetShape(data_Ba['route'])
shape_Op = GetShape(data_Op['route'])
bestfit_Ba = BoundingBox(data_Ba['route']['boundingBox'])
bestfit_Op = BoundingBox(data_Op['route']['boundingBox'])

# Map #
map_draft = "http://open.mapquestapi.com/staticmap/v4/getmap?key={my_app_key}&bestfit={bestfit}&shape={shape}&size=600,600&type=map&imagetype=jpeg"
map_Ba = map_draft.format(my_app_key=MyAppKey, bestfit=bestfit_Ba, shape=shape_Ba)
map_Op = map_draft.format(my_app_key=MyAppKey, bestfit=bestfit_Op, shape=shape_Op)

#-----------------------------------------------------------------------------

#...............................PRINT.........................................


print ('>------------<')
print ('ORIGINAL ROUTE')
print ('>------------<')


for x in data_Ba['route']['locationSequence']:
	print (route['locations'][int(x)])
print ("Total Distance " + str(data_Ba['route']['distance']) + ' miles')
print ("Total Fuel Used " + str(data_Ba['route']['fuelUsed']) + ' litres')
print ("Total Time " +  str(data_Ba['route']['formattedTime']))
print ('Map ' + map_Ba)
print ('')
print ('>-------------<')
print ('Optimised Route')
print ('>-------------<')
# Show optimised order
for x in data_Op['route']['locationSequence']:
	print (route['locations'][int(x)])
print ("Total Distance " + str(data_Op['route']['distance']) + ' miles')
print ("Total Fuel Used " + str(data_Op['route']['fuelUsed']) + ' litres')
print ("Total Time " +  str(data_Op['route']['formattedTime']))
print ('Map ' + map_Op)
