import geojson

with open("stops.geojson") as f:
    gj = geojson.load(f)

for line in gj['features']:
    print(f"INSERT INTO stops VALUES ( \'{line['properties']['stop_I']}\'")
    char = line['properties']['name'].replace("\'"," ")
    print(f", \'{char}\');")
  

#with open("routes.geojson") as f:
 #	   gj = geojson.load(f)

#for line in gj['features']:
 #   items = line.rstrip("\n").split(";")
  #  print(f"INSERT INTO network_bus VALUES ( \'{items[0]}\'", end='')
    
   # print(f"{line['properties']['route_I']};{line['properties']['route_name']};{line['properties']['route_type']}"
    
#    f = open("network_bus.csv", 'r')
#next(f)
#for line in f:
 #   items = line.rstrip("\n").split(";")
  #  print(f"INSERT INTO network_bus VALUES ( \'{items[0]}\'", end='')
   # for item in items[1:] :
    #    item = item.replace("'", "''")
     #   print(f", \'{item}\'", end='')
    #print(");")
