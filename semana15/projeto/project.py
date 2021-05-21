
def open_csv(csv):
	for row in open(csv):
		yield row

file = open_csv("candidatura.csv")
headers = next(file)

# [year] = row
map_year = {}

while True:
	try:
		row = next(file)
	except StopIteration:
		del file
		break

	row_dict = dict(zip(headers.split(','), row.split(',')))

	year = row_dict['ano_eleicao']
	if year not in map_year:
		map_year[year] = []
	map_year[year].append(row)

for year, data in map_year.items():
	data = "".join(data)
	with open(f'eleicao_{year}.csv', "w") as csv:
		csv.write(headers + data)
