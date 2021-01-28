import json
from os import name
from linebot import LineBotApi
import linebot
from linebot.models import TextSendMessage, messages

file = open("info.json", "r")
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def send_message():
  USER_ID = info['USER_ID']
  cute_messages = TextSendMessage(text="おはよう、今日も頑張ってね❤️ \n無理しないようにね❤️")
  line_bot_api.push_message(USER_ID, messages=cute_messages)


if __name__ == "__main__":
  send_message()