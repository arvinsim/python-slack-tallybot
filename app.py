import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')

print('SLACK_BOT_TOKEN', SLACK_BOT_TOKEN)
print('SLACK_APP_TOKEN', SLACK_APP_TOKEN)
