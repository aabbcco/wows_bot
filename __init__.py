# import nonebot
from enum import unique
from nonebot import get_driver
from nonebot import on_command,on_startswith,on_shell_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Event
import sys
import os
sys.path.append(os.path.dirname(__file__))
from libs.network_basic import GetPersonalInfo
from libs.parser import wowsParser
from .config import Config

repeater = on_startswith('快说',rule=to_me(),priority=5)

#basic wows info temporary
wowsinfo = on_shell_command('wows',rule=to_me(),parser=wowsParser,priority=5)

global_config = get_driver().config
config = Config(**global_config.dict())

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

@repeater.handle()
async def setrepter(bot:Bot,event:Event,state:T_State):
    args = str(event.message).strip()
    if args:
        state['repeat']=args

@repeater.got('repeat',prompt='复读模式开启')
async def gotrepeat(bot:Bot,event:Event,state:T_State):
    strs = state['repeat'][2:]
    await repeater.finish(strs)


@wowsinfo.handle()
async def wows_t_handler(bot:Bot,event:Event,state:T_State):
    args = state['args']
    if args.subname=='player':
        try:
            pdict = await GetPersonalInfo(args.server,args.name)
        except:
            wowsinfo.finish('木有找到这个玩家')
        res = '姓名:{:}\nid:{:}\n场次:{:}\nkd:{:.2f}\n胜率:{:.2f}'.format(args.name,pdict['account_id'],pdict['battles'],pdict['kd'],pdict['winrate'])
        await repeater.finish(res)
    else:
        wowsinfo.finish("啊，我被主人玩坏了")
