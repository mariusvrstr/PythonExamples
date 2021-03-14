
from resources.frame_component import HelloFrame

import time
import asyncio
import wx


async def initialize():    
    print("Starting Initiatilization")

    
    app = wx.App()

    ## Custom Frame Wrapper
    frm = HelloFrame(None, title='Hello World 2')

    # Default Frame
    # frm = wx.Frame(None, title="Hello World")

    frm.Show()

    await asyncio.sleep(3)

    ## await doIt()


def main():
   
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(initialize())
    except KeyboardInterrupt:
        pass

main()




