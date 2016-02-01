import csv
import json
import pprint

rawcsv = 'sports_worth.csv'
final = 'sports_worth.json'

m_sports = ['Baseball', 'Football', "Men's basketball", "Men's golf", "Men's gymnastics", 
			"Men's tennis", "Men's track"]
f_sports = ['Soccer', 'Softball', 'Swimming', 'Volleyball', "Women's basketball",
			"Women's golf", "Women's gymnastics", "Women's tennis", "Women's track"]

sports_map = {'name' : 'All UIUC Sports',
			 'children' : [{
			 		'name' : "Men's sports",
			 		'children': []},
			 		{'name': "Women's sports",
			 		'children': []}
			 	]}

#For gender:
with open(rawcsv, 'r') as csvfile:
	reader = csv.reader(csvfile)
	allsports = sports_map['children']
	msports = allsports[0]
	wsports = allsports[1]
	for row in reader:
		if row[0] in m_sports:
			msports['children'].append({
				'name' : row[0],
				'size' : row[1]
				})
		else:
			wsports['children'].append({
				'name' : row[0],
				'size' : row[1]
				})
			


# with open(rawcsv, 'r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		sports_map['children'].append({
# 			'name' : row[0],
# 			'size' : float(row[1])
# 			})

with open(final, 'w') as output:
	json.dump(sports_map, output)

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(sports_map)