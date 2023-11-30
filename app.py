import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.getenv('SLACK_BOT_TOKEN'))

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.getenv('SLACK_APP_TOKEN')).start()
