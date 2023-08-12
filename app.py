#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#必須放上自己的Channel Access Token
line_bot_api = LineBotApi('sEpE5vuhy2h+XkGpfQVBD20zcA+W447lazkf1aBaUGXTcoD/ER2cIXTmKkSqfJIMEAwEVlN6PwQKtAm1MYRbdUKpJHu3JAD5O63y0zQicvG93Ns9R/D4KFSTflkYPmpAma4UZHG7SiYUEJnHAHmnqwdB04t89/1O/w1cDnyilFU=')
#必須放上自己的Channel Secret
handler = WebhookHandler('0ffd902e1705ee2f4c0fc23d0e132d03')

#監聽所有來自/ callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    #get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    #getrequest body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
