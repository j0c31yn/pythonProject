import arcade

window = arcade.Window(800, 600, "My Arcade Window")

arcade.draw_rectangle_filled(400, 200, 1000, 500, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(400, 450, 1000, 500, arcade.color.DARK_BLUE)


def snowman(x, y, z):
    arcade.draw_circle_filled(x, y-150, z-((z/60)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x, y-70, z-((z/50)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, z-((z/40)*10), arcade.color.WHITE)
    arcade.draw_circle_filled(x+15, y+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x-15, y+10, 5, arcade.color.BLACK)

snowman(250,250,60)
snowman(550,250,120)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta=ime):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

# Call the main function to get the program started.
main()

arcade.finish_render()
arcade.run()