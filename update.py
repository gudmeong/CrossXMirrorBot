import asyncio

async def Run() -> None:
    while True:
        await asyncio.sleep(2)
        print("Crot dalem waduh")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Run())