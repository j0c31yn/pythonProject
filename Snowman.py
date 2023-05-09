import arcade

window = arcade.Window(800, 600, "My Arcade Window")

arcade.draw_rectangle_filled(400, 200, 1000, 500, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(400, 450, 1000, 500, arcade.color.DARK_BLUE)


def snowman(x,y):
    arcade.draw_circle_filled(250, 250, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(250, 330, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(250, 400, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(265, 410, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(235, 410, 5, arcade.color.BLACK)
def main():
    snowman(250,250)

arcade.finish_render()
arcade.run()