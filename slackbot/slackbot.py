from slack import RTMClient
from yaml import safe_load
import message_builder
from firebase import firebase

with open('slackbot-config.yaml', 'r') as stream:
  config = safe_load(stream)
  oauth_token = config['oauth_token']
  bot_token = config['bot_user_token']

client = RTMClient(token = bot_token)

@RTMClient.run_on(event = 'message')
def parse_commands(**payload):
  data = payload['data']
  # This lets the bot ignore its own messages
  try:
    data['user']
  except:
    return
  text = str(data['text'])
  print(text)

  if text.startswith('<@UQWDVSDNH>'):
    # if text.startswith('match', text.find(' ')):
    
    args = text.split(' ')
    if args[1] == 'match':
      match_command(payload, args[2:])

def match_command(payload: dict, args: list):
  data = payload['data']
  web_client = payload['web_client']
  if len(args) != 3:
    web_client.chat_postMessage(
      channel = data['channel'],
      text = 'Usage: <@UQWDVSDNH> [event ID] [match #] [team #]'
    )
    return
  try:
    match_data = firebase.get_match_data(args[0], int(args[1]), int(args[2]))
  except:
    web_client.chat_postMessage(
      channel = data['channel'],
      text = 'Usage: <@UQWDVSDNH> [event ID] [match #] [team #]'
    )
    return
  message = message_builder.match_data(match_data)
  web_client.chat_postMessage(
    channel = data['channel'],
    text = message,
    mrkdwn = True
  )

print('client set')
client.start()