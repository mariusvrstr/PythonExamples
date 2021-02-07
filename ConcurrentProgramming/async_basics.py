import time
import asyncio

class AsyncExample(object):
 
    async def sample_async_method(self):        
        for k in range(3):
            print(f"Running asyncronous method - {k}")
            time.sleep(1)
        pass


    def run(self):
        print("Start example")

        asyncio.run(self.sample_async_method())

        print("End example")
        pass















