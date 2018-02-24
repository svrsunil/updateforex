import json
import requests
import time
import urllib

from dbhelper import DBHelper

db = DBHelper()

TOKEN = "534624294:AAEwK5DA-yXbxvZXntnxbuJUC-UAjU-tmAw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = ''
    if("text" in updates["result"][last_update]["message"]):
        text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    print(text)
    type(text)
    text = urllib.parse.quote(text.encode('utf-8'))
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def main():
    db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = ''
            if('text' in update["message"]) :
                text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            chat_on = update["message"]["date"]
            username = update["message"]["from"]["username"]
            update_id = update["update_id"]
            items = db.get_items(update_id)
            """
            if text in items:
                db.delete_item(text,update_id)
                items = db.get_items(update_id)
            else:
                db.add_item(text,chat,chat_on,username,update_id)
                items = db.get_items(update_id)
            print(items)

            message = "\n".join(items)
            print(message)
            """
            msg = sendforex()[0]
            send_message(msg, chat)
        except KeyError:
            pass

def sendforex():
    str = "select desc,max(desc_on) from info_txt where label = 'forex' "
    return db.get_result(str)

if __name__ == '__main__':
    main()