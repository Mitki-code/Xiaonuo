from enum import Flag
import imp
from json.tool import main
import turtle
import qq
import logging
import random
from qq.ext import commands
from xiaonuo_config import appid,token
from xiaonuo_language import joke
from xiaonuo_game_language import xng_language


logging.basicConfig(level = logging.DEBUG)
client = qq.Client()
intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix = "/",owner_id = 114514,intents = intent)

@bot.command(name = "游戏介绍")
async def game_welcome(ctx:commands.Context):
    await ctx.channel.send(content = "欢迎游玩小诺的小游戏",msg_id = ctx.message,mention_author=ctx.message.author)
    await ctx.channel.send(content = "在这一款游戏中，你可以打怪升级，最后打败大boss",msg_id=ctx.message)
    await ctx.channel.send(content = "本游戏使用纯文字驱动，如果出现Bug，请发送 /bug [出现位置][详细状况]，小诺会记录下来的哦",msg_id=ctx.message)
    await ctx.channel.send(content = "输入 /初始化游戏 以正式开始游戏",msg_id=ctx.message)

@bot.command(name = "初始化游戏")
async def game_start(ctx:commands.Context):
    await ctx.channel.send(content = "成功！" , msg_id = ctx.message,mention_author=ctx.message.author)

@bot.command(name = "讲个笑话",aliases = ["笑话"])
async def speak_joke(ctx:commands.Context):
    await ctx.channel.send(content = joke[random.randint(0,10)],msg_id = ctx.message,mention_author=ctx.message.author)

if __name__ == '__main__':
    bot.run(token = f"{appid}.{token}")