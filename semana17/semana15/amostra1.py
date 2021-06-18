def abre_csv(file):
	for linha in open(file):
		yield linha

candidatura = abre_csv("./projeto/candidatura.csv")

headers = next(candidatura)
cand_ano = {}

while True:
	try:
		cand = next(candidatura)
	except StopIteration:
		del candidatura
		break

	ano = cand.split(",")[0]
	if ano not in cand_ano:
		cand_ano[ano] = []
	cand_ano[ano].append(cand)


for ano,cand in cand_ano.items():
	csv_data = "".join(cand)
	with open(f"projeto/eleicao_{ano}.csv", "w") as csv:
		csv.write(headers + csv_data)
