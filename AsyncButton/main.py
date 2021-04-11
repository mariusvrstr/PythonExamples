
from modules.module_one import ModuleOne
from modules.module_two import ModuleTwo
from modules.monitoring import Monitoring

import time
import asyncio

module_one = None
module_two = None

counters = []

async def initialize(display_module, module_one, module_two):
    asyncio.ensure_future(module_one.start_monitoring())
    asyncio.ensure_future(module_two.start_monitoring())

    # Main thread is the display thread
    await display_module.start_display(counters)
    pass

def main():
    display_module =  Monitoring()
    module_one = ModuleOne(3)
    module_two = ModuleTwo(8)

    counters.append(module_one.counter_summary)
    counters.append(module_two.counter_summary) 

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(initialize(display_module, module_one, module_two))

    except KeyboardInterrupt:
        module_one.dispose()
        module_two.dispose()
        display_module.dispose()

main()
time.sleep(5)   