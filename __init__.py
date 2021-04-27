# import nonebot
from nonebot import get_driver
from nonebot import on_command,on_keyword,on_startswith
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Event

from .config import Config

repeater = on_startswith('快说',rule=to_me(),priority=5)

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