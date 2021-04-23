import httpx
import asyncio
from nonebot import get_driver
from pydantic.utils import unique_list


async def PostRequestAsync(dest):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(dest)
            resp.raise_for_status()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
    res=resp.json()
    if res['status']=='error':
        raise Exception(res['error']['code'],res['error']['message'])

    return res

async def GetTargetIdByRequest(server:str,field:str,name:str)->str:
    assert field in ['clans','account']
    url = WowsRequestGenerater(server,[field,'list'],{'search':name})
    res = await PostRequestAsync(url)
    return res['data'][0]['clan_id'] if field=='clans' else res['data'][0]['account_id'] 

async def GetClanInfo(server:str,name:str):
    if name.isdigit():
        id = name
    else:
        id = await GetTargetIdByRequest(server,'clans',name)
        id = str(id)
    url = WowsRequestGenerater(server,['clans','info'],{'clan_id':id})
    claninfo= (await PostRequestAsync(url))['data'][id]

    return {
        'name':claninfo['name'],
        'members_count':claninfo['members_count'],
        'creator_name':claninfo['creator_name'],
        'clan_id':claninfo['clan_id'],
        'updated_at':claninfo['updated_at'],
        'leader_name':claninfo['leader_name'],
        'tag':claninfo['tag'],
        'description':claninfo['description']
    }



#http(s)://<server>/<API_name>/<method block>/<method name>/?<get params>
def WowsRequestGenerater(server:str,api:list,func:dict)->str:

    url="https://api.worldofwarships.{:}/wows/".format(server)
    for _,key in enumerate(api):
        url+="{:}/".format(key)
    
    try:
        #appkey = get_driver().config.wargamingappkey
        appkey = "41eea5422846e9db1871963330a1ae04"
    #personal key will delete after release
    except:
        raise Exception('key error');
    url+="?application_id={:s}".format(appkey)

    for ele in func.keys():
        url+='&{:}={:}'.format(ele,func[ele])
    
    return url




