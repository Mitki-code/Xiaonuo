import qq
import logging
import random
from qq.ext import commands
from xiaonuo_config import appid,token
from xiaonuo_language import joke
from xiaonuo_game_language import xng_language
from xiaonuo_game_data import xng_ud


logging.basicConfig(level = logging.DEBUG)
client = qq.Client()
intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix = "/",owner_id = 114514,intents = intent)

@bot.command(name = "游戏介绍")
async def game_welcome(ctx:commands.Context):
    await ctx.channel.send(content = xng_language["welcome1"],msg_id = ctx.message,mention_author=ctx.message.author)
    t_tempn = 1
    for i in range(3):
        t_tempn = t_tempn+1
        await ctx.channel.send(content = xng_language["welcome"+str(t_tempn)],msg_id=ctx.message)
    
@bot.command(name = "初始化游戏")
async def game_start(ctx:commands.Context):
    print(xng_ud)
    for xng_ud in xng_ud:
    if xng_ud
        await ctx.channel.send(content = "成功！" , msg_id = ctx.message,mention_author=ctx.message.author)
        xng_ud.append(str(ctx.message.author))
    else:
        await ctx.channel.send(content = "错误：不能重复初始化" , msg_id = ctx.message,mention_author=ctx.message.author)
    

@bot.command(name = "讲个笑话",aliases = ["笑话"])
async def speak_joke(ctx:commands.Context):
    await ctx.channel.send(content = joke[random.randint(0,10)],msg_id = ctx.message,mention_author=ctx.message.author)

if __name__ == '__main__':
    bot.run(token = f"{appid}.{token}")