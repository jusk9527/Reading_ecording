import httpx
import asyncio


async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.get('http://127.0.0.1:8000/')
        result = resp.json()
        print(result)


asyncio.run(main())