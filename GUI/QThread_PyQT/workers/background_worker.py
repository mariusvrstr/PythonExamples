from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
from sensors.sensor_one import SensorOne
from contracts.counter import Counter
import asyncio

class BackgroundWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    enabled = False

    async def run_all(self):
        self.enabled = True

        counter = Counter("Sensor One")
        SensorOne(counter)

        while True:
            self.progress.emit(counter.get_value()) ## Can't process complex objects yet
            # Keep main thread alive
            await asyncio.sleep(1)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:            
            loop.run_until_complete(self.run_all())
        
        except KeyboardInterrupt:
            print (f'stopped')
            
        self.finished.emit()   