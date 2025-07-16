'''
use pyglet to create hello world application 
'''


import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label(
        'Hello, World!',
        font_name='Arial',
        font_size=24,
        x=window.width//2, y=window.height//2,
        anchor_x='center', anchor_y='center'
)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()