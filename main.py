import logging

logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from pyrogram.types import Message

m_api_id = 12345 # my.telegram.org/
m_api_hash = "12345abcd" # my.telegram.org/

m_sender_chat_id = [12345] # Where from
m_chat_id = 12345 # Where

app = Client("bot", m_api_id, m_api_hash)

@app.on_message(filters.chat(m_sender_chat_id))
async def post(app, msg: Message):
	await msg.forward(m_chat_id)

app.run()