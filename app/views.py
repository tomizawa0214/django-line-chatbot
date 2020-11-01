from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
import os

line_bot_api = LineBotApi("r0rk3aFNtvFRfwE + ICHRhUInvDVX9cWjzeLoATW1WRqj7gP / FO5xRhLH / C3CD3n0aSVbuCYTgevsj6HIL41w0 / lAMw4qCh67hE77Dfuke2NFQbJl7zxHbaSxLTuE0Td")
handler = WebhookHandler("e6fed109ff1597ea497e4ab45a861abb")


@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=500)


# オウム返し
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))