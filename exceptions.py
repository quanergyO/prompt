from telegramm import telegram_send_text
import time


def exception_handler(value):
    def decorate(func):
        def applicator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                telegram_send_text("prompt have a problem. Leather freak go fix it!!")
                print(e)
                # TODO add LOGURU
                # TODO reload to OS
                return value
        return applicator
    return decorate
