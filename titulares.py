import json
import requests
import csv

class worldcupinfo:
	def __init__(self):
		self.req = requests.get('http://worldcup.sfg.io/matches')
		self.data = json.loads(self.req.content)
	def playersinfo(self):
		with open('worldcup.csv','w+') as f:
			writer = csv.writer(f)
			x = []
			for i in self.data:
				if i['status'] == 'completed':
					if i['home_team_statistics']['country'].upper() not in x:
						writer.writerow(('','','%s'%(i['home_team_statistics']['country'].upper())))
						x.append(i['home_team_statistics']['country'].upper())
						writer.writerow(('NAME','POSITION','SHIRT-NUMBER'))
						for s in i['home_team_statistics']['starting_eleven']:
							writer.writerow((f"{s['name']}",f"{s['position']}",f"{s['shirt_number']}"))
					else:
						pass
x = worldcupinfo()
x.playersinfo()
