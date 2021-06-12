from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
from sensors.sensor_one import SensorOne
from contracts.counter import Counter
import asyncio

class BackgroundWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(Counter)
    enabled = False
    counters = []

    async def run_all(self):
        self.enabled = True

        counter_alpha = Counter("Alpha Sensor")
        self.counters.append(counter_alpha)

        counter_bravo = Counter("Bravo Sensor")   
        self.counters.append(counter_bravo)

        asyncio.ensure_future(self.AlphaProcess(counter_alpha))        
        asyncio.ensure_future(self.BravoProcess(counter_bravo))

        while True:  
            # Keep main thread alive
            await asyncio.sleep(1)


    async def AlphaProcess(self, counter):
        frequency = 1

        while self.enabled:
            counter.incriment()
            self.progress.emit(counter)
            await asyncio.sleep(frequency)

        
    async def BravoProcess(self, counter):
        frequency = 3

        while self.enabled:
            counter.incriment()
            self.progress.emit(counter)
            await asyncio.sleep(frequency)


    def run(self): 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:            
            loop.run_until_complete(self.run_all())
        
        except KeyboardInterrupt:
            print (f'stopped')
            
        self.finished.emit()   