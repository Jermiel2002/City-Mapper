import geojson

with open("sections.geojson") as f:
    gj = geojson.load(f)

for line in gj['features']:
	items = line['properties']['route_I_counts']
	#char = str(items)
	#char = char.replace("'","")
	#char = char.replace("{","")
	#char = char.replace("}","")
	#char = char.replace(" ","")
	for(key,value) in items.items():
		print(f"INSERT INTO sections VALUES ( \'{line['properties']['from_stop_I']}','{line['properties']['duration_avg']}\'")
		print(f",\'{key}\',")
	#print(f",\'{char}\',")
		print(f"\'{line['properties']['to_stop_I']}','{line['properties']['route_type']}','{line['properties']['n_vehicles']}\');")
