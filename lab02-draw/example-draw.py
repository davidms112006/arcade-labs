"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 700, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# --- Draw the barn ---

# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)

# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 550, 210, arcade.color.GRAY)

# Left-bottom window
arcade.draw_rectangle_filled(70, 375, 50, 300, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 375, 30, 250, arcade.color.LIGHT_SKY_BLUE)

# Right-bottom window
arcade.draw_rectangle_filled(310, 375, 50, 300, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 375, 30, 250, arcade.color.LIGHT_SKY_BLUE)

# Barn door
arcade.draw_rectangle_filled(190, 220, 75, 100, arcade.color.DARK_BROWN)
# POMO DE LA PUERTA
arcade.draw_circle_filled(170, 220, 5, arcade.color.BLACK)
# separacion entre ventanas
arcade.draw_rectangle_filled(310, 280, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 320, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 360, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 400, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 440, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 480, 50, 5, arcade.color.BONE)

arcade.draw_rectangle_filled(70, 280, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 320, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled( 70, 360, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 400, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 440, 50, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 480, 50, 5, arcade.color.BONE)
# Draw second level of barn
arcade.draw_polygon_filled([[140, 600],
                            [27, 550],
                            [350, 550],
                            [250, 600]],
                            arcade.color.GRAY)



# MID- window
arcade.draw_rectangle_filled(190, 460, 100, 225, arcade.color.BONE)
arcade.draw_rectangle_filled(190, 460, 75, 200, arcade.color.LIGHT_SKY_BLUE)

#bottom window
arcade.draw_circle_filled(190, 300, 20, arcade.color.BONE)
arcade.draw_circle_filled(190, 300, 15, arcade.color.LIGHT_SKY_BLUE)

arcade.draw_rectangle_filled(190, 300, 40, 5, arcade.color.BONE)
arcade.draw_rectangle_filled(190, 300, 5, 40, arcade.color.BONE)

# --- Draw the tractor ---

# Draw the engine
arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)

# Draw the smoke stack
arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)

# Back wheel
arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
arcade.draw_circle_filled(490, 110, 10, arcade.color.RED)

# Front wheel
arcade.draw_circle_filled(650, 90, 30, arcade.color.BLACK)
arcade.draw_circle_filled(650, 90, 25, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(650, 90, 18, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 90, 5, arcade.color.RED)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

