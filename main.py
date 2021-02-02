from pprint import pprint
import requests

token = '1638979366:AAFQm6BUe8OebzcXzKPFso_-JUUdejfWsrI'


def getUpdates():
    data = []
    url_Updates = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.get(url_Updates)
    updates = res.json()['result']
    pprint(updates)
    final_msg = updates[-1]
    up_id = final_msg['update_id']
    message_id = final_msg['message']['message_id']
    msg_text = final_msg['message']['text']
    chat_id = final_msg['message']['from']['id']
    data = [up_id, msg_text, chat_id, message_id]

    return data


def sendMessage(chatId, text, upid):
    payload = {
        'chat_id': chatId,
        'text': text,
        'reply_to_message_id': upid
    }
    url_sendMsg = f'https://api.telegram.org/bot{token}/sendMessage'
    r = requests.get(url=url_sendMsg, params=payload)


def echo_bot():
    final_update_id = 0
    while True:
        data = getUpdates()
        msg_id = data[3]
        chatId = data[2]
        text = data[1]
        update_id = data[0]

        if final_update_id != update_id:
            sendMessage(chatId, text, msg_id)
            final_update_id = update_id

        else:
            continue


echo_bot()
