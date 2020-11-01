import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 2.0
    while True:
        t='True'
        print(t)
        r=''
        if (loop.time() + 1.0) >= end_time:
            r='False'
            break
        print(r)
        await asyncio.sleep(5)
    else:
        print(r)
asyncio.run(display_date())
