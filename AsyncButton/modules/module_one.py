from models.counter_summary import CounterSummary
import random
import asyncio

class ModuleOne():
    counter_summary = None
    is_monitoring = False
    _frequency_in_seconds = 10
    
    def __init__(self, frequency_in_seconds):
        self.counter_summary = CounterSummary("Module One")
        self._frequency_in_seconds = frequency_in_seconds
        pass

    def get_value(self):
        random_value = random.randint(0, 50)

        return random_value
    
    def dispose(self):
        self.is_monitoring = False
        pass

    async def start_monitoring(self):        
        self.is_monitoring = True

        while self.is_monitoring:
            new_value = self.get_value()
            self.counter_summary.update_value(new_value)
            await asyncio.sleep(self._frequency_in_seconds)
        pass