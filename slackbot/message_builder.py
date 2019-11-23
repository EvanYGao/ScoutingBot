from collections import OrderedDict

def match_data(data: OrderedDict) -> str:
  message = ''
  if data == None:
    return 'The event/match/team combo entered is not valid.'
  for key, value in data.items():
    message += f'*{key}*: {value}\n'
  return message

