f = open("network_temporal_week.csv", 'r')
next(f)
for line in f:
    items = line.rstrip("\n").split(";")
    print(f"INSERT INTO network_temporal_week VALUES ( \'{items[0]}\'", end='')
    for item in items[1:] :
        item = item.replace("'", "''")
        print(f", \'{item}\'", end='')
    print(");")
