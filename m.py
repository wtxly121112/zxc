import pickle
import asyncio
from time import sleep
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
	
from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

import textwrap
import os
import json, pickle

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
	
app = Client('admin', api_id=18413850, api_hash='598aac24b5cf0a1b4632485f5f33c4c7')
with Client('admin', api_id=18413850, api_hash='598aac24b5cf0a1b4632485f5f33c4c7') as app:
    while True:
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweeffe"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweeff"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweef"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweeff"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweef"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qwee"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qwe"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qw"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="q"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qw"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qwe"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qwee"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweef"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweff"))
        time.sleep(3)
        app.invoke(functions.account.UpdateProfile(first_name="qweeffe"))
	
# ?????????????? type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "???"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) 

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

 # ???????????? ???????????? ?? ??????????????
@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>?????????? step, ???????? ???????? ??????????</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>?????? ?????????????? ?????? ???????? ???? ????????</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>?? ?????? ?? ?????????? ???????? preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>?? ???????????? ???????????????????? ????????</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>???? ???? ?????????? ????????, ?? ??????????????</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>?? ?????????????????? ?? dissmilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>?? ???? ?????????????? ???? ?? ??????????</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>???? ???????????????? ?????????? ?? late</b>
	''')

	sleep(0.2)
	global number
	number = number + 1
	
	 # ???????????? ???????????? ?? ?????????????? 2
@app.on_message(filters.command("??????", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	??
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????????? ?????? ??????-????????
	''')
	
		 # ???????????? ???????????? ?? ?????????????? 3
@app.on_message(filters.command("??????1", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	??????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?? ????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	???? ?????? ??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????????
	''')
	
	 # ???????????? ???????????? ?? ?????????????? 4
@app.on_message(filters.command("????????", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	???? ????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????????
	''')
	
	 # ???????????? ???????????? ?? ?????????????? 5
@app.on_message(filters.command("??????2", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	?? ???????? ???????? ?????????????? ?????????????? ??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????????????????????? ???????????? ?????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????????? ??????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????? ?????????????????????????????????? ???????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????? ?????? ?????????? ????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	???????? ???????? ?????????????????? ?? ???????? ???? ??????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	???????????????????? ???????????????????? ?????????????? ???????????? ???????????????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	??????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????????
	''')
	
	 # ???????????? ???????????? ?? ?????????????? 6
@app.on_message(filters.command("??????3", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	???????????? ???????????? ???????????? ?????????????????????? ?? ?????????? ??????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????? ???? ???????????????? ?????????????? ???????? ?? ???????????????? ???????? ???????????????????????? ?????? ????????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????? ?????????????? ?????????????? ?? ???????? ???????????? ?? ?????????????? ?????? ???? ??????????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?? ???????????????? ???? ???????? ?????????????? ???????????? ????????, ???????????? ?????? ????????????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	????????????????????????????
	''') 
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?? ?????? ???????????? ?????????? ?????????? ?????????????? ?? ?????? ???????? ????????????????
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?????????????????? ?????????? ???????????? ?????????? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	?? ???????? ???????? ???????????????? ???????????????????? ?? ???????????? ?????????????????? ??????
	''')
	
#??????????????????????
@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> ?????????????????? ??????????: </b>'

#1000-7
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)

#????????????
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number

	if not spams:
		msg.edit(f'''
			**Error: ??????-???? ?????????? ???? ??????...\n??????????????????????????: .spam <??????-???? ??????????> <??????????>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

#????????????/????????
@app.on_message(filters.command("tf", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[????????????]", "[????????]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: ???? ???? ?????????? ????????????!\n??????????????????????????: .tf <????????????>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1		

@app.on_message(filters.command("help", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>?????? ?????? ?? ???????????? ?? ????????????: ??????(1-3)(??????-???????? ???? ?????????????? ???????????????? ????????????); ghoul(???????????????? ?? ???????????? ????????); type [??????????] (???????????????? ????????????); tf [??????????] (????????????/????????); spam [??????-???? ??????????????????] [??????????] (?????????????????? ?????????? ???? ????????)</b>
	''')
	
@app.on_message(filters.command("????????", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>?????? ?????? ?? ???????????? ?? ????????????: ??????(1-3)(??????-???????? ???? ?????????????? ???????????????? ????????????); ghoul(???????????????? ?? ???????????? ????????); type [??????????] (???????????????? ????????????); tf [??????????] (????????????/????????); spam [??????-???? ??????????????????] [??????????] (?????????????????? ?????????? ???? ????????)</b>
	''')
	
@app.on_message(filters.command("????????????", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>?????? ?????? ?? ???????????? ?? ????????????: ??????(1-3)(??????-???????? ???? ?????????????? ???????????????? ????????????); ghoul(???????????????? ?? ???????????? ????????); type [??????????] (???????????????? ????????????); tf [??????????] (????????????/????????); spam [??????-???? ??????????????????] [??????????] (?????????????????? ?????????? ???? ????????)</b>
	''')
	
app.run()