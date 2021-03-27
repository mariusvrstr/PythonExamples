
from resources.frame_component import HelloFrame

import time
import asyncio
import wx

app = wx.App()

## Custom Frame Wrapper
frm = HelloFrame(None, title='Hello World 2')

# Default Frame
# frm = wx.Frame(None, title="Hello World")

frm.Show()
app.MainLoop()



