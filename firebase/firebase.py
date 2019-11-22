import pyrebase
import yaml

with open('../config.yaml', 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print('Could not load YAML file')
    print(exc)

print(config)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# print(db.child('devices').get().val())

def get_matches(event: str, team : int):
  team = str(team) if len(str(team)) == 4 else ' ' + str(team)
  matches = list()
  for x in range(1, 150):
    data = db.child('match-data').child(event).child(f'{x:03d}-{team}').get().val()
    if data != None:
      matches.append(data)
  return matches

for x in get_matches('gal', 5414):
  print(x['final_comment'])
# print(db.child('match-data').child('ftcmp').child('012-5414').get().val())