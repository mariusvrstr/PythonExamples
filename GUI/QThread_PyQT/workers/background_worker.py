from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
import asyncio

class BackgroundWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    async def run_one(self):
        for i in range(15):
            self.progress.emit(i)  
            sleep(1)
            # await asyncio.sleep(1) # Seems like asyncio sleep and threads are not working      

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            asyncio.ensure_future(self.run_one())
            loop.run_until_complete(self.run_one())
        
        except KeyboardInterrupt:
            print (f'stopped')
            
        self.finished.emit()   