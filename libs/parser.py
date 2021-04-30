from logging import Handler
from nonebot.rule import ArgumentParser
from .handler import *

wowsParser = ArgumentParser("wows")
wowsParser.add_argument('server',default='asia',help='which server you are in?')

wowSubParserList = wowsParser.add_subparsers()

PlayerParser = wowSubParserList.add_parser('player',help='player info')
PlayerParser.add_argument('name')
PlayerParser.set_defaults(handle = handle_player)



