import httpx
import asyncio



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