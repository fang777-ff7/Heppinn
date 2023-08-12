from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#必須放上自己的Channel Access Token
line_bot_api = LineBotApi('sEpE5vuhy2h+XkGpfQVBD20zcA+W447lazkf1aBaUGXTcoD/ER2cIXTmKkSqfJIMEAwEVlN6PwQKtAm1MYRbdUKpJHu3JAD5O63y0zQicvG93Ns9R/D4KFSTflkYPmpAma4UZHG7SiYUEJnHAHmnqwdB04t89/1O/w1cDnyilFU=')
#必須放上自己的Channel Secret
handler = WebhookHandler('0ffd902e1705ee2f4c0fc23d0e132d03')
