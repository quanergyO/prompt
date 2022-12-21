import requests


def telegram_send_text(bot_message):
    bot_token = '5867008067:AAGNlf_wYjGxhFKIONCxG6D2CL9UHH5Yn_4'
    bot_chatID = '-889046734'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


