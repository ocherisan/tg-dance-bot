import asyncio
import os
from aiogramm import Bot
from aiogramm.methods import SendPoll

async def send_poll():
  token = os.getenv("BOT_TOKEN")
  chat_id = os.getenv("CHAT_ID")
  question = os.getenv("QUESTION")

  options = os.getenv("OPTIONS").split(",")

  if not all([token, chat_id, question, options]):
    raise ValueError("Не все переменные окружения заданы")

  bot = Bot(token=token)
  await bot(SendPoll(chat_id=chat_id, question=question, options=options, is_anonymmous=True, type="regular"))
  await bot.session.close()

if __name__ == "__main__":
  asyncio.run(send_poll())