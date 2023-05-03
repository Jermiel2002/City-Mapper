import geojson

with open("routes.geojson") as f:
    gj = geojson.load(f)

for line in gj['features']:
    print(f"{line['properties']['route_I']};{line['properties']['route_name']};{line['properties']['route_type']}")

