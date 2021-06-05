from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
import asyncio

class BackgroundWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    enabled = False

    async def run_all(self):
        self.enabled = True
        asyncio.ensure_future(self.run_one())

        while True:
            # Keep main thread alive
            await asyncio.sleep(2)       

    async def run_one(self):
        count_sub = 0

        while self.enabled:
            count_sub += 1
            self.progress.emit(count_sub)  
            await asyncio.sleep(1)      

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:            
            loop.run_until_complete(self.run_all())
        
        except KeyboardInterrupt:
            print (f'stopped')
            
        self.finished.emit()   