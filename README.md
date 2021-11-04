# PyPixel - Game engine
### Based on PyGame

# Import

```py
import pyPixel as pp
```

# Init the game
```py
def update(dt): # dt - delta value
    pass

def draw(drawer):
    # drawer.screen - pygame's screen object
    pass

# Init the game
pp.initGame(update, draw, "My Game", (640, 480))
```

# Load resources
```py
# Load image
img = pp.load_image("test.png")

# Returns resized image
img2 = pp.resize_image(img, width, height)
```

# Draw inside `draw(drawer)`
```py
# Draws a rectangle
drawer.rect(x, y, w, h, color)

# Draws a line
drawer.line(x1, y1, x2, y2, width, color)

# Draws an image
drawer.image(img, x, y)

# Draws an resized image (Not recomended in case of perfomance. Better use resize_image(img, newWidth, newHeight))
drawer.image_resized(img, x, y, width, height)

# Draws a single pixel on the screen
drawer.pix(x, y, color)
```

# Signal
* Used as an event system
* Inspired by Godot
```py
sig = pp.Signal()

# Emit the signal
sig.emit(DATA)

# Block's anync until signal emitted. Returns data
sig.wait()

# Connect function to a signal
sig.connect(func)

# Connect function to a signal via decorator
@sig.connect
def someFunc(data):
    pass

# Disconnect function from a signal
sig.disconnect(func)
```

# Signals (events)
```py
# Emits when key is pressed (key_code)
# Can be compared with pp.K_ ... constants
pp.on_key

# Emits when key is released (key_code)
# Can be compared with pp.K_ ... constants
pp.on_key_release

# Emits when mouse moved (x, y)
pp.on_mouse

# Emits on mouse down (button_number 1=LEFT 2=MIDDLE 3=RIGHT)
pp.on_mouse_down

# Emits on mouse up (button_number 1=LEFT 2=MIDDLE 3=RIGHT)
pp.on_mouse_up
```