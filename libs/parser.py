from logging import Handler
from nonebot.rule import ArgumentParser
from .handler import *

wowsParser = ArgumentParser("wows")

wowSubParserList = wowsParser.add_subparsers(dest='subname')

PlayerParser = wowSubParserList.add_parser('player',help='player info')
PlayerParser.add_argument('server')
PlayerParser.add_argument('name')
PlayerParser.set_defaults(handle = handle_player)



