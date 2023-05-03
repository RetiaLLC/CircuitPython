# 2023 by Skickar for Retia LLC
# Write text on the screen one character at a time with a delay. 

# Import the necessary libraries
import displayio # Allows us to use DisplayIO
import terminalio # Allows us to use TerminalIO
from adafruit_display_text import label # Allows us to use Label
import adafruit_displayio_sh1106 # Allows us to use SH1106
import board # Allows us to use board
import time # Allows us to use time.sleep()

# Define the text we want to display
text = "Heck yes"

# Initialize the display
displayio.release_displays() # Release any displays that might be in use
i2c = board.I2C() # Create a new I2C object for the display
oled_bus = displayio.I2CDisplay(i2c, device_address=0x3C) # Create a new I2CDisplay object for the display with address 0x3C
display = adafruit_displayio_sh1106.SH1106(oled_bus, width=128, height=64, colstart=2) # Create a new SH1106 object for the display with correct width and height

# Create a new group for the text and add it to the display
group = displayio.Group() # Create a new Group object for the text

# Wait for 1 second before starting animation
time.sleep(1)

# Animate text one character at a time
for i in range(len(text)):
    label_text = label.Label(terminalio.FONT, text=text[:i+1]) # Create a new Label object with the text and TerminalIO font
    label_text.x = 0 # Set the x position of the label to 0 (left side of screen)
    label_text.y = 20 # Set the y position of the label to 20 (20 pixels down from the top of screen)
    group.append(label_text) # Add the label to the group
    display.show(group) # Show the group on the display
    time.sleep(.25) # Wait for 1 second before updating again

# Wait forever (or until you reset or power off)
while True:
    pass # Do nothing (wait forever)
