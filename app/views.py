from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
import os
import requests


CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class CallbackView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')

    def post(self, request, *args, **kwargs):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseBadRequest()
        except LineBotApiError as e:
            print(e)
            return HttpResponseServerError()

        return HttpResponse('OK')

        # print("ここはポストの最初ー－－－－")
        # ACCESS_TOKEN = "6cPp1IrvZ96x5dTrsxKe6OMxX7sgp2TcaroPN6wbJRH"

        # headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

        # data = {
        #     "message": "こんにちは！\nLINE Notifyを使ってメッセージを送ってみたよ！"
        # }

        # requests.post(
        #     "https://notify-api.line.me/api/notify",
        #     headers=headers,
        #     data=data,
        # )
        # print("最後まで来たー－－－－")

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallbackView, self).dispatch(*args, **kwargs)


    # オウム返し
    @staticmethod
    @handler.add(MessageEvent, message=TextMessage)
    def message_event(event):
        if event.reply_token == "00000000000000000000000000000000":
            return
            
        line_bot_api.reply_message(
            event.reply_token,
            # TextSendMessage(text=event.message.text)
            TextSendMessage(text="商品情報が更新されたよー－－")
        )