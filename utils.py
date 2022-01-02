import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_multiple_text_message(reply_token, text1,text2,text3,text4,text5):
    reply_arr=[]
    reply_arr.append( TextSendMessage(text=text1) )
    reply_arr.append( TextSendMessage(text=text2) )
    reply_arr.append( TextSendMessage(text=text3) )
    reply_arr.append( TextSendMessage(text=text4) )
    reply_arr.append( TextSendMessage(text=text5) )
    line_bot_api.reply_message( reply_token, reply_arr )

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
