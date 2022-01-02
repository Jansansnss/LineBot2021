import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *#MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message
#from gevent import pywsgi

load_dotenv()

machines = {}
machine = TocMachine(
    states=["user", "state1", "state2","united_state","pokemon_name","search","developer","sql","help"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "advance",
            "source": "state2",
            "dest": "united_state",
            "conditions": "is_going_to_united_state",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "pokemon_name",
            "conditions": "is_going_to_pokemon_name",
        },
        {
            "trigger": "advance",
            "source": "pokemon_name",
            "dest": "search",
            "conditions": "is_going_to_search",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "developer",
            "conditions": "is_going_to_developer",
        },
        {
            "trigger": "advance",
            "source": "developer",
            "dest": "sql",
            "conditions": "is_going_to_sql",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "help",
            "conditions": "is_going_to_help",
        },
        {"trigger": "go_back", "source": ["state1","united_state","search","sql","help"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
#app.config['ENV'] = 'production'


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
print("U can start!")
#line_bot_api.push_message('U80e435170a374fb9947bef3d5d6a571e', TextSendMessage(text='你可以開始了'))
#line_bot_api.push_message('Ue038cc7b82e7b48e81b78b525ce6cbf1', TextSendMessage(text='振嘉比你帥'))


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        
        #print("?????????????????????????????????????????")
        #print(event)
        #webhook_handler()


        """if event.source['userId']=='Ue038cc7b82e7b48e81b78b525ce6cbf1':
            line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="518閉嘴讓我靜靜")
        )"""
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        print(f"\nFSM STATE: {machine.state}")
        if response == False:
            send_text_message(event.reply_token, "Insert help for instructions")

        """line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )"""

    return "OK"


"""@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"
    """


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

"""@parser.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)"""

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)

    """server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
    server.serve_forever()"""
