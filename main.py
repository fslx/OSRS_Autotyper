import pyautogui as pygui
import time

pgui.FAILSAFE = True

def automate_messages(message: str):
    """
    Is passed a message, utilizes the pyautogui keyboard control functions & methods to perform
    copy paste functionality.
    :param message: Outputs the message it is passed on input
    :type message: str
    :rtype: function
    """
    message = get_message()
    copy_content = pygui.hotkey("ctrl", "c")
    paste_content = pygui.hotkey("ctrl", "v")

def get_message():
    pass
