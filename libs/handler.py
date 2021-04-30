from argparse import Namespace
from .network_basic import GetPersonalInfo


def handle_player(args:Namespace):
    args.function = GetPersonalInfo
    return args