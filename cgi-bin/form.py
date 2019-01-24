#!/usr/bin/env python3
# coding: utf8
import cgi
import requests

form = cgi.FieldStorage()
text1 = form.getfirst(u"name", "не задано")
text2 = form.getfirst(u"email", "не задано")
text3 = form.getfirst(u"message", "не задано")


token = "405008999:AAG1zA8joYi29VSUpToSUt6r4waWvgKFwBY"
URL =  "https://api.telegram.org/bot" + token + "/"

def get_updates():                # всі результати
    url = URL + "getupdates"
    r = requests.get(url)
    return r.json()

def get_message():           # береться тільки  text і chat_id
    data = get_updates()
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    text = data["result"][-1]["message"]["text"]
    message = { "chat_id": chat_id,
                 "text": text  }
    return message

def send_message(chat_id,text):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id,text)
    requests.get(url)


answer = get_message()
chat_id = answer["chat_id"]
text = "name: " + text1 + " email: " + text2 + " message: " + text3
send_message(chat_id, text)
