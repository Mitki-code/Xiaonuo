import imp
import qq
import logging
import random
from xiaonuo_config import appid,token
from xiaonuo_language import joke

logging.basicConfig(level=logging.DEBUG)
client = qq.Client()

@client.event
async def on_message(message:qq.Message):
    print(message.content)

    if message.author == client.user:
        return

    if "笑话" in message.content:
        await message.channel.send(content=joke[random.randint(0,10)],msg_id=message,mention_author=message.author)
    else:
        await message.channel.send(content="hello",msg_id=message,mention_author=message.author)

@client.event
async def on_reday():
    print("初始化成功")

if __name__ == '__main__':
    client.run(token = f"{appid}.{token}")

