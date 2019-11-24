DIRECTORY=./venv

FILE=./firebase-config.yaml
if [ ! -f FILE ]; then
  touch firebase-config.yaml
fi
FILE=./slackbot-config.yaml
if [ ! -f FILE ]; then
  touch slackbot-config.yaml
fi
if [ ! -d DIRECTORY ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
python3 ./slackbot/slackbot.py