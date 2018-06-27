# -*- coding: utf-8 -*-
import json
import requests
import csv

class worldcupinfo:
	def __init__(self):
		self.req = requests.get('http://worldcup.sfg.io/matches')
		self.data = json.loads(self.req.content)
	def playersinfo(self):
		with open('titulares.csv','w+') as f:
			writer = csv.writer(f)
			for i in self.data:
				if i['status'] == 'completed':
					writer.writerow(('','','%s x %s'%(i['home_team_country'],i['away_team_country']),'\n'))
					writer.writerow(('','%s'%(i['home_team_statistics']['country'].upper()),'\n'))
					writer.writerow(('NAME','POSITION','SHIRT-NUMBER'))
					for s in i['home_team_statistics']['starting_eleven']:
						writer.writerow((f"{s['name']}",f"{s['position']}",f"{s['shirt_number']}"))
					writer.writerow(('','%s'%(i['away_team_statistics']['country'].upper()),'\n'))
					for s in i['away_team_statistics']['starting_eleven']:
						writer.writerow((f"{s['name']}",f"{s['position']}",f"{s['shirt_number']}"))
				else:
					pass

	def substitutions(self):
		with open('substitutions.csv','w') as f:
			writer = csv.writer(f)
			for i in self.data:
				if i['status'] == 'completed':
					writer.writerow(('','','%s x %s'%(i['home_team_country'],i['away_team_country'])))
					writer.writerow(('','%s'%(i['home_team_country']),'\n'))
					writer.writerow(('IN','OUT'))
					x = [s['player'] for s in i['home_team_events'] if s['type_of_event']== 'substitution-in']
					y = [s['player'] for s in i['home_team_events'] if s['type_of_event']== 'substitution-out']
					for c in zip(x,y):
						writer.writerow((c))
					writer.writerow(('','%s'%(i['away_team_country']),'\n'))
					writer.writerow(('IN','OUT'))
					x = [s['player'] for s in i['away_team_events'] if s['type_of_event']== 'substitution-in']
					y = [s['player'] for s in i['away_team_events'] if s['type_of_event']== 'substitution-out']
					for c in zip(x,y):
						writer.writerow((c))
					writer.writerow((''))
						
x = worldcupinfo()
x.substitutions()
