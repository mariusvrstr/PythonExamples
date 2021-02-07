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
        await asyncio.gather(*tasks)
 
    def run(self):
        print("Start example")

        asyncio.run(self.start())
        

        #executor = ProcessPoolExecutor(2)
        #loop = asyncio.get_event_loop()

        #asyncio.create_task(loop.run_in_executor(executor, self.sample_async_method_a))
        #asyncio.create_task(loop.run_in_executor(executor, self.sample_async_method_b))

        #loop.run_forever()

        print("End example")
        pass









