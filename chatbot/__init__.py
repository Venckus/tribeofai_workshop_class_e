#!/usr/local/bin/python3
from .chatbot import EpicApp
try:
    import nlp
except ImportError:
    from .nlp import *

# def show_error(message):
#     chat_app.info_page.update_info(message)
#     chat_app.screen_manager.current = 'Info'
#     Clock.schedule_once(sys.exit, 10)

# GUI module taken from:
# https://pythonprogramming.net/finishing-chat-application-kivy-application-python-tutorial/?completed=/chat-application-kivy-application-python-tutorial/
if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()