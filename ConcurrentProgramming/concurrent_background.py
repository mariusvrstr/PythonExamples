import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

class ConcurrentBackgroundExample(object):

    async def sample_async_method_a(self):
        for k in range(10):
            print(f"Running asyncronous method a - {k}")
            await asyncio.sleep(1)


    async def sample_async_method_b(self):
        for k in range(10):            
            print(f"Running asyncronous method b - {k}")
            await asyncio.sleep(1)

    async def start(self):
        asyncio.ensure_future(self.sample_async_method_a())        
        asyncio.ensure_future(self.sample_async_method_b())

        for k in range(10):            
            print(f"Main menu normal processes - {k}")
            await asyncio.sleep(1)

 
    def run(self):
        print("Start example")

        asyncio.run(self.start())
       
        print("End example")
        pass









