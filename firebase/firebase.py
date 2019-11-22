import pyrebase
import yaml

with open('firebase-config.yaml', 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print('Could not load YAML file')
    print(exc)

print(config)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# print(db.child('devices').get().val())

def get_matches(event: str, team: int) -> list:
  """
  A function that queries the database for the match data of a team for a specific event or all 
  events

  :param event: The event ID of the event in the Firebase database. Use 'all' for all events in
  the year.
  :param team: The team number of the team that you want to query.

  :returns: A list of all the match data a team has for the specified event.
  """
  # The database has a space before team numbers less than 4 in length
  team = f'{team:04d}'.replace('0', ' ')
  matches = list()
  if event == 'all':
    events = list(db.child('match-data').shallow().get().val())
    for event in events:
      for match in get_matches(event, int(team)):
        matches.append(match)
  else:
    # We can realistically expect less than 150 matches per event
    for match in range(1, 150):
      data = db.child('match-data').child(event).child(f'{match:03d}-{team}').get().val()
      if data != None:
        matches.append(data)
  return matches

def get_raw_percents(event: str, team: int):
  pass

# for x in get_matches('gal', 5414):
#   print(x['final_comment'])
# print(db.child('match-data').child('ftcmp').child('012-5414').get().val())
print(get_matches('all', 5414))