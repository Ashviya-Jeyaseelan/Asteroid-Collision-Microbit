count = 0 
score = 0 
my_position = 2 # Reset position to default middle column
asteroid = randint(0, 4) # Ensure asteroid falls from a random column each time   
	

def on_forever(): 

  global my_position 
  global count 
  global score 
  global asteroid

  my_position = Math.constrain(Math.round(((input.acceleration(Dimension.X) + 500) / 250)), 0, 4) # Position changes depending on direction of tilt 

  basic.clear_screen() # Hide position for a moment 

  led.plot(my_position, 4) # Position reappears where it was moved with 4 being the y position in the last row  

  led.plot_brightness(asteroid, (count % 5), 50) 

  count = ((count + 1) % 5) 

  basic.pause(250) 

  if count == 4: # Asteroid reached the bottom of the grid so must be in last row now 

    if my_position == asteroid: # Current position is same spot where the asteroid was 

      basic.show_leds(""" 

        . . . . . 

        . # . # . 

        . . . . . 

        . # # # . 

        # . . . # 

        """) 

      my_position = 2 # Restart in the last row in the middle column of the grid  

      score = 0 # Reset score 

      basic.pause(2000) 

    else: # Plays up to 10 points but can be modified

      score += 1 

      if score == 10: 

        basic.show_leds(""" 

          . . . . . 

          . # . # . 

          . . . . . 

          # . . . # 

          . # # # . 

          """) 

        score = 0 

        basic.pause(2000) 

  if count == 0: # Asteroid did not collide and was successfully dodged so drop another one 

    asteroid = randint(0, 4) 

basic.forever(on_forever) 
