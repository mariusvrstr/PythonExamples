import os
import asyncio

class Monitoring:
    _is_displaying = False
    _show_pipe = True

    def __init__(self):
         os.system('initializing console display...')
         pass

    def display(self, counter_list):
        self._show_pipe = not self._show_pipe

        os.system('cls')
        print("Latest values")
        print("================================")
        print()

        for counter in counter_list:
            print(f"[{counter.name}] latest value is [{counter.current_value}] - {counter.last_execution}")

        print()
        tic_indicator = "|" if self._show_pipe else "-"

        print(f"Prest Cntr+C to exit [{tic_indicator}]")

        pass

    def dispose(self):
        self._is_displaying = False
        pass

    async def start_display(self, counter_list):
        self._is_displaying = True

        while self._is_displaying:
            self.display(counter_list)
            await asyncio.sleep(1)            
        pass
    

