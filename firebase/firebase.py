import pyrebase
import yaml
from typing import Optional

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

def get_match_data(event: str, match: int, team: int) -> Optional[dict]:
  """
  A function that queries the database for the match data of a specific match for a team

  :param event: The event ID of the event in the Firebase database.
  :param match: The match ID of the event in the Firebase database.
  :param team: The team number of the team that you want to query.

  :returns: A dict of all the match data a team has for the specified event. Returns None if no data.
  """
  # Team is a 4 character string with a space for missing digits
  # Match is a 3 digit number with leading zeroes
  team = f'{team:04d}'.replace('0', ' ')
  match = f'{match:03d}'
  print(f'{match}-{team}')
  
  return db.child('match-data').child(event).child(f'{match}-{team}').get().val()

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
      # Matches show up as 3 digit numbers with trailing zeroes
      data = db.child('match-data').child(event).child(f'{match:03d}-{team}').get().val()
      if data != None:
        matches.append(data)
  return matches

def get_raw_percents(event: str, team: int) -> dict:
  """
  A function that calculates the percentages of each area scored per team

  :param event: The event ID of the event in the Firebase database. Use 'all' for all events in
  the year.
  :param team: The team number of the team that you want to analyze.

  :returns: Dictionary of (str, float) for all scoring areas or empty dictionary of no data found.
  """

  '''
  CS - Cargo Ship
  RKT - Rocket
  E - End
  L - Left
  P - Panel
  C - Cargo
  T - Top
  M - Middle
  B - Bottom
  1 - First from DS
  2 - Second from DS
  3 - Third from DS
  LVL - Level
  '''

  zones = {
    'CSELP': 0, 
    'CSERP': 0,
    'CSL1P': 0,
    'CSL2P': 0,
    'CSL3P': 0,
    'CSR1P': 0,
    'CSR2P': 0,
    'CSR3P': 0,
    'LR1BP': 0,
    'LR1MP': 0,

  }
  # TODO: Implement this


# for x in get_matches('gal', 5414):
#   print(x['final_comment'])
# print(db.child('match-data').child('ftcmp').child('012-5414').get().val())
print(get_match_data('ftcmp', 1, 2714))