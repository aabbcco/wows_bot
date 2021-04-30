# import nonebot
from enum import unique
from nonebot import get_driver
from nonebot import on_command,on_startswith,on_shell_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Event
from libs.parser import wowsParser
import sys
sys.path.append(os.path.dirname(__file__))
from libs.network_basic import GetPersonalInfo

from .config import Config

repeater = on_startswith('快说',rule=to_me(),priority=5)

#basic wows info temporary
wows_info = on_command('wows',aliases={'窝窝屎'},rule=to_me(),priority=5)
wows_info_test = on_shell_command('wowst',rule=to_me(),parser=wowsParser,priority=5)

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

@wows_info.handle()
async def wows_handler(bot:Bot,event:Event,state:T_State):
    args = str(event.get_message()).strip()
    if args:
        try:
            pdict = await GetPersonalInfo('asia',args)
        except:
            wows_info.finish('木有找到这个玩家')
        res = '姓名:{:}\nid:{:}\n场次:{:}\nkd:{:.2f}\n胜率:{:.2f}'.format(args,pdict['account_id'],pdict['battles'],pdict['kd'],pdict['winrate'])
        await repeater.finish(res)

@wows_info_test.handle()
async def wows_t_handler(bot:Bot,event:Event,state:T_State):
    args = state['args']
    if args.subparser_name=='PlayerParser':
        pdict = await GetPersonalInfo(args.server,args.name)
        res = '姓名:{:}\nid:{:}\n场次:{:}\nkd:{:.2f}\n胜率:{:.2f}'.format(args,pdict['account_id'],pdict['battles'],pdict['kd'],pdict['winrate'])
        await repeater.finish(res)
    else:
        repeater.finish("啊，我被主人玩坏了")
