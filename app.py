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

    # emoji = [
    #         {
    #             "index": 0,
    #             "productId": "11537",
    #             "emojiId": "52002738"
    #         },
    #         {
    #             "index": 10,
    #             "productId": "11537",
    #             "emojiId": "52002738"
    #         }
    # ]

    text_message = TextSendMessage(text='''
Hello! 您好 歡迎您成為 Heppinn 的好友!

我是超級顧問 很高興為您服務
                                   
-這裡有股票、匯率資訊喔~
-直接點選下方【圖中】選單功能
                                   
-期待您的光臨!''')
    
    sticker_message = StickerSendMessage(
        package_id='11537',
        sticker_id='52002738'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])


    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
