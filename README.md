# ScoutingBot

A Slack bot designed to work in conjunction with Pearadox 5414's scouting database

## Dependencies:

* Python 3.7+
* PyPI and Pip installer
* Python3 VEnv

## Usage:

Clone this repository by using

```git clone https://github.com/Pearadox/ScoutingBot.git```

Change your working directory with

```cd Scoutingbot```

Run the start script:

```bash start.sh```

Edit the YAML files using your preferred text editor into these formats:

firebase-config.yaml:

```yaml
'apiKey': '-'
'authDomain': '-'
'databaseURL': '-'
'storageBucket': '-'
```

slackbot-config.yaml:

```yaml
'oauth_token': 'xoxp-16664820659-696781854487-848669167350-53c3f7d83664a50c54d9519a46a69761'
'bot_user_token': 'xoxb-16664820659-846471897765-ZFTBlvpymOWdE8uHxxPrurfz'
```

Run the start script again.