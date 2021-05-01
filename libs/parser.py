from logging import Handler
from nonebot.rule import ArgumentParser
from .handler import *

wowsParser = ArgumentParser("wows")

wowSubParserList = wowsParser.add_subparsers(dest='subname')

PlayerParser = wowSubParserList.add_parser('player',help='player info')
PlayerParser.add_argument('server')
PlayerParser.add_argument('name')
PlayerParser.set_defaults(handle = handle_player)

ClanParser = wowSubParserList.add_parser('clan',help='clan info')
ClanParser.add_argument('server')
ClanParser.add_argument('clan')
ClanParser.set_defaults(handle = handle_clan)

