
f = open("network_combined.csv", 'r')
next(f)
for line in f:
    item = line.rstrip("\n").split(";")
    a = item[5].split(",")
    for i in a:
    	b = i.split(":")
    	print(f"INSERT INTO network_combined VALUES ( \'{item[0]}\',\'{item[1]}\',\'{item[2]}\',\'{item[3]}\',\'{item[4]}\',\'{b[0]}\',\'{item[6]}\');")
