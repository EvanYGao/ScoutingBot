DIRECTORY=./venv

if [ ! -d DIRECTORY ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
python3 ./slackbot/slackbot.py