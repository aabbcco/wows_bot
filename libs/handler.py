from argparse import Namespace
from .network_basic import GetClanInfo, GetPersonalInfo

def handle_player(args:Namespace)->Namespace:
    args.function = GetPersonalInfo
    return args

def handle_clan(args:Namespace)->Namespace:
    args.function = GetClanInfo
    return args