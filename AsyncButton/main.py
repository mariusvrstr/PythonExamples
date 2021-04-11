
from modules.module_one import ModuleOne
from modules.module_two import ModuleTwo
from modules.monitoring import Monitoring
from main_gui import Ui_MainWindow


import time
import asyncio

module_one = None
module_two = None

counters = []

async def initialize(gui_module, display_module, module_one, module_two):
    asyncio.ensure_future(module_one.start_monitoring())
    asyncio.ensure_future(module_two.start_monitoring())

    # Open GUI Window
    gui_module.start_gui()

    # TODO: Why does the ASYNCIO only kick in when the GUI is closed? Blokking the main thread?
    # it seem like all the asyncio is properly registered and starts executing but only if the GUI thread is stopped
    await display_module.start_display(counters)

def main():
    display_module =  Monitoring()
    gui_module = Ui_MainWindow()

    module_one = ModuleOne(3)
    module_two = ModuleTwo(8)

    counters.append(module_one.counter_summary)
    counters.append(module_two.counter_summary) 

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(initialize(gui_module, display_module, module_one, module_two))

    except KeyboardInterrupt:
        module_one.dispose()
        module_two.dispose()
        display_module.dispose()
        gui_module.dispose()

main()
time.sleep(5)   