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
'oauth_token': '-'
'bot_user_token': '-'
```

Run the start script again.