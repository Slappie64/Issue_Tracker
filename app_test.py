from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

buffer1 = Buffer()

root_container = VSplit([
    Window(content=BufferControl(buffer=buffer1)),
    Window(width=1,char='|'),
    Window(content=FormattedTextControl(text='Hello World')),
])

layout = Layout(root_container)

app = Application(layout=layout, full_screen=True)
app.run()
