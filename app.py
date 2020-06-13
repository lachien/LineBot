# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('AxBw8vdskHz9Gr6Jjt4/MMt94NQiJ3Tn9m2BuoXRKlYMQCJlZBI0fHfXheRS/EZr2L8xcIQC69EsaRyKJHGBSEztWQ0ZswMm6iPRIcNq20954TrBCFskCac7Q+kscK+HzJ9XPVWCBjV4bngeulTNXAdB04t89/1O/w1cDnyilFU=')
# Channel access token (long-lived)
handler = WebhookHandler('f2da671e3e4fd085e7940ee78ed55a33')
# Channel secret 



@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)