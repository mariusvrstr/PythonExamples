
import asyncio

class SensorOne():
    counter = None
    enabled = False
    frequency_in_seconds = 1

    def __init__(self, counter):
        self.counter = counter
        asyncio.ensure_future(self.run())

    async def run(self):
        self.enabled = True

        while self.enabled:
            self.counter.incriment(1)           
            await asyncio.sleep(self.frequency_in_seconds)
    