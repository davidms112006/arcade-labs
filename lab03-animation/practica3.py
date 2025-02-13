

# Import the "arcade" library
import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
def suelo ():
    # Draw the SUELO
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(250, 90, 4000, 120, arcade.color.BLACK)
    arcade.draw_rectangle_filled(0, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(100, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(200, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(300, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(400, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(500, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(600, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(700, 90, 40, 10, arcade.color.PLATINUM)
    arcade.draw_rectangle_filled(800, 90, 40, 10, arcade.color.PLATINUM)

def nube(x,y):
    # draw nube

    arcade.draw_ellipse_filled(550+x, 510+y, 95, 250, [255, 255, 255], 90, 75)
    arcade.draw_circle_filled(550+x, 540+y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(500+x, 520+y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(600+x, 520+y, 50, arcade.color.WHITE)

    arcade.draw_ellipse_filled(600, 510, 95, 250, arcade.color.WHITE, 90, 75)
    arcade.draw_circle_filled(600, 540, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(550, 520, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(650, 520, 50, arcade.color.WHITE)

def edificio ():
    # Barn cement base
    # Bottom half
    arcade.draw_lrtb_rectangle_filled(30, 350, 550, 210, arcade.color.GRAY)

    arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)
    arcade.draw_polygon_filled([[140, 600],[27, 550],[350, 550], [250, 600]],arcade.color.GRAY)

def ventanas ():
    # Left-bottom window
    arcade.draw_rectangle_filled(70, 375, 50, 300, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 375, 30, 250, arcade.color.LIGHT_SKY_BLUE)

    # Right-bottom window
    arcade.draw_rectangle_filled(310, 375, 50, 300, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 375, 30, 250, arcade.color.LIGHT_SKY_BLUE)
    # separacion entre ventanas
    arcade.draw_rectangle_filled(310, 280, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 320, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 360, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 400, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 440, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 480, 50, 5, arcade.color.BONE)

    arcade.draw_rectangle_filled(70, 280, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 320, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 360, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 400, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 440, 50, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 480, 50, 5, arcade.color.BONE)

    # MID- window
    arcade.draw_rectangle_filled(190, 460, 100, 225, arcade.color.BONE)
    arcade.draw_rectangle_filled(190, 460, 75, 200, arcade.color.LIGHT_SKY_BLUE)

    # bottom window
    arcade.draw_circle_filled(190, 300, 20, arcade.color.BONE)
    arcade.draw_circle_filled(190, 300, 15, arcade.color.LIGHT_SKY_BLUE)

    arcade.draw_rectangle_filled(190, 300, 40, 5, arcade.color.BONE)
    arcade.draw_rectangle_filled(190, 300, 5, 40, arcade.color.BONE)

def puerta():
    # Barn door
    arcade.draw_rectangle_filled(190, 220, 75, 100, arcade.color.DARK_BROWN)
    # POMO DE LA PUERTA
    arcade.draw_circle_filled(170, 220, 5, arcade.color.BLACK)

def on_draw(delta_time)

def main ():
        arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.start_render()

        suelo()
        nube(100,200)
        edificio()
        ventanas()
        puerta()

        arcade.finish_render()
        arcade.run()

main()