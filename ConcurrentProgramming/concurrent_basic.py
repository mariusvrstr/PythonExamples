import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

class ConcurrentMethodExample(object):

    async def sample_async_method_a(self):
        for k in range(3):
            print(f"Running asyncronous method a - {k}")
            await asyncio.sleep(1)


    async def sample_async_method_b(self):
        for k in range(3):            
            print(f"Running asyncronous method b - {k}")
            await asyncio.sleep(1)

    async def start(self):
        tasks = [self.sample_async_method_a(), self.sample_async_method_b()]
        await asyncio.wait(tasks)
 
    def run(self):
        print("Start example")

        asyncio.run(self.start())
        
        print("End example")
        pass









