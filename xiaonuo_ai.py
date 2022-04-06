from dis import Instruction
import imp
import logging
import random
import time

import qq
import json
from qq.ext import commands

from xiaonuo_config import appid, token
from xiaonuo_game_language import xng_language,xng_gps
from xiaonuo_language import joke

logging.basicConfig(level = logging.DEBUG)
client = qq.Client()
intent = qq.Intents.default()
intent.guild_messages = True
intent.at_guild_messages = False
bot = commands.Bot(command_prefix = "/",owner_id = 114514,intents = intent)

class xngame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    
    async def ginfo(ctx:commands.Context):
        with open("data/xngame_user_gdata.json", "r") as f:
            xng_ud_json = json.load(f)
        tgps = "x"+str(xng_ud_json["user"+str(ctx.message.author.id)]["x"])+"|"+"y"+str(xng_ud_json["user"+str(ctx.message.author.id)]["y"])
        await ctx.channel.send(content = xng_language["info_desc_0"]+"\n"+xng_language["info_desc_h"]+str(xng_ud_json["user"+str(ctx.message.author.id)]["max_h"])+"/"+str(xng_ud_json["user"+str(ctx.message.author.id)]["h"])+"   "+xng_language["info_desc_m"]+str(xng_ud_json["user"+str(ctx.message.author.id)]["max_m"])+"/"+str(xng_ud_json["user"+str(ctx.message.author.id)]["m"])+"\n"+xng_language["info_desc_xy"]+"   "+str(xng_gps[tgps]+"   x"+str(xng_ud_json["user"+str(ctx.message.author.id)]["x"])+"   y"+str(xng_ud_json["user"+str(ctx.message.author.id)]["y"])), msg_id = ctx.message)

#+xng_language["info_desc_xy"]+str(xng_ud_json["user"+str(ctx.message.author.id)]["x"])+"/"+str(xng_ud_json["user"+str(ctx.message.author.id)]["y"])


    async def check_game_guild(ctx:commands.Context):
        return ctx.message.channel.name == "小游戏" or "小游戏厕所"

    @commands.check(check_game_guild)
    @commands.command(name = "关于")
    async def game_about(self,ctx:commands.Context):
        await ctx.channel.send(content= xng_language["about"],msg_id = ctx.message)
        
    @commands.check(check_game_guild)
    @commands.command(name = "介绍")
    async def game_welcome(self,ctx:commands.Context):
        await ctx.channel.send(content = xng_language["welcome0"],msg_id = ctx.message,mention_author=ctx.message.author)
        for i in range(3):
            await ctx.channel.send(content = xng_language["welcome"+str(i+1)],msg_id=ctx.message)
        
    @commands.check(check_game_guild)
    @commands.command(name = "初始化")
    async def game_start(self,ctx:commands.Context):
        xng_ud_json = {}
        with open("data/xngame_user_data.json", "r") as f:
            xng_ud_json = json.load(f)
        xng_ud_if = xng_ud_json
        for i in range(len(xng_ud_if["id"])):
            if xng_ud_if["id"][i] == ctx.message.author.id:
                await ctx.channel.send(content = xng_language["welcome_start0_error"], msg_id = ctx.message,mention_author=ctx.message.author)
                break
        else:
            await ctx.channel.send(content = xng_language["welcome_start0"], msg_id = ctx.message,mention_author=ctx.message.author)
            xng_ud_json["id"].append(int(ctx.message.author.id))
            with open('data/xngame_user_data.json', 'w') as f:
                json.dump(xng_ud_json, f)

    @commands.check(check_game_guild)
    @commands.command(name = "开局设定")
    async def game_start(self,ctx:commands.Context,command:str,a0:int,a1:int,a2:int,a3:int):
        if command == xng_language["gstart_title_0"]:
            await ctx.channel.send(content = xng_language["gstart_desc_0"], msg_id = ctx.message,mention_author=ctx.message.author)
            for i in range(6):
                await ctx.channel.send(content = xng_language["gstart_desc_"+str(i)],msg_id=ctx.message)
        elif command == xng_language["gstart_title_1"]:
            xng_ud_json = {}
            with open("data/xngame_user_gdata.json", "r") as f:
                xng_ud_json = json.load(f)
            xng_ud_if = xng_ud_json
            for key in xng_ud_if:
                if key == "user"+str(ctx.message.author.id):
                    await ctx.channel.send(content = xng_language["gstart_start0_error"], msg_id = ctx.message,mention_author=ctx.message.author)
                    break
            else:
                if (a0 >= 0 and a0 <= 1) and (a1 >= 18 and a1 <= 60) and (a2 >= 0 and a2 <= 2) and (a3 >=0 and a3<= 3):
                    xng_ud_json["user"+str(ctx.message.author.id)] = {"gender":a0,"age":a1,"job":a2,"feature":a3,"x": 0 , "y": 0 ,"bag" :[], "bag_magic" : [],"gold": 0, "parms": 0 , "pmagic" : 0,"parmor" :[],"max_h" : 100,"h" : 100,"max_m" : 100,"m" : 100}
                    if xng_ud_json["user"+str(ctx.message.author.id)]["feature"] == 2:
                        xng_ud_json["user"+str(ctx.message.author.id)]["max_h"] = 200
                        xng_ud_json["user"+str(ctx.message.author.id)]["h"] = 200
                    elif xng_ud_json["user"+str(ctx.message.author.id)]["feature"] == 3:
                        xng_ud_json["user"+str(ctx.message.author.id)]["max_m"] = 200
                        xng_ud_json["user"+str(ctx.message.author.id)]["m"] = 200
                    with open('data/xngame_user_gdata.json', 'w') as f:
                        json.dump(xng_ud_json, f)
                    await ctx.channel.send(content = xng_language["gstart_start0"], msg_id = ctx.message,mention_author=ctx.message.author)
                else:
                    raise commands.BadArgument

    @game_start.error
    async def game_start_error(self,ctx:commands.Context,error):
        if isinstance(error,commands.BadArgument):
            await ctx.reply(content= xng_language["terror"])
        else:
            await ctx.reply(content= xng_language["terror"])

    @commands.check(check_game_guild)
    @commands.command(name = "开始")
    async def right_game_start(self,ctx:commands.Context):
        ttemp = random.randint(0,2)
        xng_ud_json = {}
        with open("data/xngame_user_gdata.json", "r") as f:
            xng_ud_json = json.load(f)
        if ttemp == 0:
            xng_ud_json["user"+str(ctx.message.author.id)]["x"] = -1
            xng_ud_json["user"+str(ctx.message.author.id)]["y"] = 999
        elif ttemp == 1:
            xng_ud_json["user"+str(ctx.message.author.id)]["x"] = 0
            xng_ud_json["user"+str(ctx.message.author.id)]["y"] = 999
        elif ttemp == 2:
            xng_ud_json["user"+str(ctx.message.author.id)]["x"] = 1
            xng_ud_json["user"+str(ctx.message.author.id)]["y"] = 999
        with open('data/xngame_user_gdata.json', 'w') as f:
            json.dump(xng_ud_json, f)
        await ctx.channel.send(content = xng_language["gstart_play_desc"][ttemp], msg_id = ctx.message,mention_author=ctx.message.author)
        await xngame.ginfo(ctx)
        






@bot.command(name = "讲个笑话",aliases = ["笑话"])
async def speak_joke(ctx:commands.Context):
    await ctx.channel.send(content = joke[random.randint(0,10)],msg_id = ctx.message,mention_author=ctx.message.author)

if __name__ == '__main__':
    bot.add_cog(xngame(bot))
    bot.run(token = f"{appid}.{token}")
