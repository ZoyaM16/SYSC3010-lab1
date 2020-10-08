from sense_hat import SenseHat
import time

"""

  Sense HAT Sensors Display
  
  Toggle between Z and M
  
  Note: Requires sense_hat 2.2.0 or later

"""

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


def show_z():
  sense.show_letter("Z", back_colour = red)
  time.sleep(.5)

def show_m():
  sense.show_letter("M", back_colour = green)
  time.sleep(.5)

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        if sense.show_letter:
           show_z()
           sense.show_letter("M") 
        else:
            sense.show_letter("Z") 
          
              
      elif event.direction == "down":
        if sense.show_letter:
           show_z()
           sense.show_letter("L") 
        else:
            sense.show_letter("Z")      # Down arrow
      elif event.direction == "left": 
        if sense.show_letter:
          show_z() 
          sense.show_letter("M") 
        else:
            sense.show_letter("Z")     # Left arrow
      elif event.direction == "right":
        if sense.show_letter:
           show_z()
           sense.show_letter("M") 
        else:
            sense.show_letter("Z")     # Right arrow
      elif event.direction == "middle":
       if sense.show_letter:
          show_z()
          sense.show_letter("M") 
       else:
            sense.show_letter("Z")     # Enter key

