#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
from dotenv import load_dotenv
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")
load_dotenv(".env", override=True)
# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION", default="AQAJdzyT251vRumJGKTue2RstE4d-D57jmf9jetLKGWLBlVyh78nviv-ZiZBqihT2R9OVLxtujh3nYJdvulrWvLSvNwzdkxa2tgKYwwbM2btJrAjMIvTeNQW_aP1lzYVdAFuJSSEN8Re1teveTHTHRrLp9BsIBth-GbT6tD77kylrca_xiJqVGbP_qOGuqwrti5LOYjzFDfOWzD3PQPJi3tajeRxe66OSNfIGthBii2-IzXSD0DAp97McNPRr_98Gsr5ARb533iDBW2t_Bc0QWdR61mpSjsxbU3_HijnQTMsmeDmfzmU5aOMJF7QEEh8A-0FXcM9r9ydec4eBk0tepcLAAAAAVxMrfEA")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
